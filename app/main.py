from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from app.config import settings
from app.routes import (
    home_router,
    auth_router,
    customer_router,
    admin_router,
    api_router
)

def create_app() -> FastAPI:
    """Application factory for SkinCheck Web Application."""
    app = FastAPI(
        title=settings.APP_NAME,
        description="AI-Powered Skin Health Monitoring & Skincare Assistant Web Platform",
        version="1.0.0-foundation",
        debug=settings.APP_DEBUG
    )

    # Add Session Middleware for Authentication with CSRF mitigation (SameSite Lax)
    app.add_middleware(
        SessionMiddleware,
        secret_key=settings.SECRET_KEY,
        session_cookie="skincheck_session",
        max_age=86400 * 7, # 7 days
        same_site="lax",
        https_only=not settings.APP_DEBUG
    )

    from fastapi import Request
    from fastapi.responses import RedirectResponse
    from app.middleware.auth_guard import AuthException

    @app.middleware("http")
    async def add_security_headers(request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response

    @app.exception_handler(AuthException)
    async def auth_exception_handler(request: Request, exc: AuthException):
        return RedirectResponse(url=exc.redirect_url, status_code=303)

    # Mount Static Files (CSS, JS, Images)
    app.mount("/static", StaticFiles(directory=str(settings.STATIC_DIR)), name="static")

    # Register Routers (MVC Web Routes & API)
    app.include_router(home_router)
    app.include_router(auth_router)
    app.include_router(customer_router)
    app.include_router(admin_router)
    app.include_router(api_router)

    # Favicon handler to suppress 404 errors
    from fastapi.responses import Response
    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon():
        return Response(status_code=204)

    return app

app = create_app()
