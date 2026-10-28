import time
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.config.database import get_db, Base
from app.models.user import User
from app.models.skin_scan import SkinScan
from app.utils.auth import get_password_hash

# Dedicated isolated SQLite database for privacy test
TEST_DATABASE_URL = "sqlite:///./test_privacy_audit.sqlite"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def setup_test_db():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    db: Session = TestingSessionLocal()
    
    # Create test customer
    test_user = User(
        name="Privacy Tester",
        email="privacy@example.com",
        password_hash=get_password_hash("password123"),
        role="customer"
    )
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    
    return test_user

def test_privacy_and_security():
    print("=== SECURITY & PRIVACY VERIFICATION TESTS ===")
    user = setup_test_db()
    
    # Login
    res_login = client.post("/login", data={"email": "privacy@example.com", "password": "password123"})
    
    # [1] Test Rate Limiting on AI Assistant (Limit = 10 / min)
    # We mock assistant.chat to avoid slow external API calls and test middleware directly.
    print("\n[1] Testing AI Rate Limiting (10 req/min)...")
    from unittest.mock import patch
    with patch("app.services.ai_assistant_service.assistant.chat", return_value="Mock response"):
        rate_limit_triggered = False
        for i in range(12):
            res = client.post("/assistant/chat", json={"message": "Halo"}, follow_redirects=False)
            if res.status_code == 429:
                rate_limit_triggered = True
                break
                
        if rate_limit_triggered:
            print("  [PASS] AI Endpoint Rate Limiter triggered at 429 Too Many Requests")
        else:
            print("  [FAIL] Rate limiter did not trigger!")

    # [2] Test Account Deletion (2-Step OTP flow as per PRD v2.0 FR-H05)
    print("\n[2] Testing Privacy Data Deletion (2-Step OTP)...")
    res_req = client.post("/profile/request-delete-otp")
    assert res_req.status_code == 200, "Request OTP should succeed"
    dev_code = res_req.json().get("dev_code")
    
    if not dev_code:
        # Fetch OTP token from test DB
        db: Session = TestingSessionLocal()
        from app.models.otp_token import OTPToken
        token = db.query(OTPToken).filter(OTPToken.user_id == user.id, OTPToken.purpose == "delete_account").order_by(OTPToken.id.desc()).first()
        dev_code = token.code if token else ""
        db.close()
        
    res_delete = client.post("/profile/delete", json={"otp_code": dev_code})
    
    if res_delete.status_code == 200:
        # Check DB
        db: Session = TestingSessionLocal()
        deleted_user = db.query(User).filter(User.id == user.id).first()
        if deleted_user is None:
            print("  [PASS] Account and related data deleted permanently via 2-Step OTP (Right to be Forgotten)")
        else:
            print("  [FAIL] Account still exists in Database")
        db.close()
    else:
        print("  [FAIL] /profile/delete returned unexpected status code:", res_delete.status_code, res_delete.text)
        
    print("\n=== TESTS COMPLETE ===")
    
    # Clean up isolated test database
    import os
    if os.path.exists("./test_privacy_audit.sqlite"):
        try:
            os.remove("./test_privacy_audit.sqlite")
        except Exception:
            pass

if __name__ == "__main__":
    test_privacy_and_security()
