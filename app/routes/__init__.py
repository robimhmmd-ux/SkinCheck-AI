from .home_routes import router as home_router
from .auth_routes import router as auth_router
from .customer_routes import router as customer_router
from .admin_routes import router as admin_router
from .api_routes import router as api_router

__all__ = [
    "home_router",
    "auth_router",
    "customer_router",
    "admin_router",
    "api_router"
]
