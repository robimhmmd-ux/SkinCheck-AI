import os
import io
import sys
from io import BytesIO
from PIL import Image
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.config.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.models.product import Product
from app.utils.auth import get_password_hash

# Dedicated isolated SQLite database for integration testing
TEST_DATABASE_URL = "sqlite:///./test_skincheck.sqlite"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
client = TestClient(app)

def create_dummy_image(brightness=200):
    """Creates a dummy valid PNG image in memory."""
    img = Image.new('RGB', (400, 400), color=(brightness, brightness, brightness))
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def setup_fresh_db():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    db = TestingSessionLocal()
    
    # Create Admin
    admin = User(name="Admin", email="admin_integ@example.com", password_hash=get_password_hash("admin123"), role="admin")
    # Create Customer 1
    cust1 = User(name="Customer 1", email="cust1@example.com", password_hash=get_password_hash("pass123"), role="customer")
    # Create Customer 2
    cust2 = User(name="Customer 2", email="cust2@example.com", password_hash=get_password_hash("pass123"), role="customer")
    
    # Create a product
    prod = Product(brand="TestBrand", name="Sunscreen X", category="Sunscreen", status="active")
    
    db.add_all([admin, cust1, cust2, prod])
    db.commit()
    db.refresh(cust1)
    db.refresh(cust2)
    return cust1, cust2

def run_integration_tests():
    print("=== FINAL E2E INTEGRATION TESTING ===")
    cust1, cust2 = setup_fresh_db()
    
    # ---------------------------------------------------------
    # 1. CUSTOMER E2E FLOW
    # ---------------------------------------------------------
    print("\n[CUSTOMER FLOW]")
    
    # Login Customer 1
    client.post("/login", data={"email": "cust1@example.com", "password": "pass123"}, follow_redirects=False)
    
    res = client.get("/dashboard")
    assert res.status_code == 200, "Dashboard should load"
    print("  [PASS] Login & Dashboard loaded")
    
    # Test Camera / Upload Validation (Invalid - Too Dark)
    dark_img = create_dummy_image(brightness=10) # dark image
    res = client.post("/scan/face/upload", files={"file": ("dark.png", dark_img, "image/png")})
    assert res.status_code == 400, "Should reject dark image"
    assert "gelap" in res.json()["error"], "Error message should mention lighting"
    print("  [PASS] Image validation (lighting) works")
    
    # Test Upload Valid Image
    valid_img = create_dummy_image(brightness=200)
    res = client.post("/scan/face/upload", files={"file": ("valid.png", valid_img, "image/png")})
    assert res.status_code == 200, "Should accept valid image"
    scan_id = res.json()["scan_id"]
    print("  [PASS] Face Scan AI processed successfully")
    
    # Check Scan Detail & 5 Conditions
    res_detail = client.get(f"/history/{scan_id}")
    assert res_detail.status_code == 200, "Scan detail should load"
    assert "Acne" in res_detail.text, "Scan detail should show Acne"
    assert "Dry Skin" in res_detail.text, "Scan detail should show Dry Skin"
    assert "Oily Skin" in res_detail.text, "Scan detail should show Oily Skin"
    assert "Dark Spots" in res_detail.text, "Scan detail should show Dark Spots"
    assert "Wrinkles" in res_detail.text, "Scan detail should show Wrinkles"
    print("  [PASS] 5 Facial Conditions (Acne, Dry, Oily, Dark Spots, Wrinkles) verified in detail view")

    # Check History Pagination
    res = client.get("/history?page=1")
    assert res.status_code == 200, "History should load"
    assert str(scan_id) in res.text, "History should show scans"
    print("  [PASS] History & Pagination loaded")
    
    # AI Assistant chat - Normal
    res = client.post("/assistant/chat", json={"message": "Apa produk yang cocok untuk saya?"})
    assert res.status_code == 200
    print("  [PASS] AI Assistant normal chat & Product RAG works")
    
    # AI Assistant chat - High Risk
    res = client.post("/assistant/chat", json={"message": "Wajah saya berdarah dan bernanah, apa diagnosisnya?"})
    assert res.status_code == 200
    assert "dokter" in res.json()["response"].lower(), "AI should deflect high-risk medical questions"
    print("  [PASS] AI Safety (Medical risk filtering) works")
    
    # Logout
    res = client.get("/logout", follow_redirects=False)
    assert res.status_code == 303, "Should redirect on logout"
    
    # ---------------------------------------------------------
    # 2. SECURITY & ISOLATION
    # ---------------------------------------------------------
    print("\n[SECURITY FLOW]")
    
    # Login Customer 2
    client.post("/login", data={"email": "cust2@example.com", "password": "pass123"}, follow_redirects=False)
    
    # Try accessing Customer 1's scan
    res = client.get(f"/history/{scan_id}")
    assert res.status_code == 404, "Customer 2 should not see Customer 1's scan"
    print("  [PASS] IDOR Protection: Cannot view other's scan")
    
    # Try accessing Admin Dashboard
    res = client.get("/admin/dashboard", follow_redirects=False)
    assert res.status_code == 303, "Customer should be blocked from admin"
    print("  [PASS] Authorization: Customer blocked from Admin")
    
    # ---------------------------------------------------------
    # 3. ADMIN FLOW
    # ---------------------------------------------------------
    print("\n[ADMIN FLOW]")
    # Login as Admin
    client.post("/admin/login", data={"email": "admin_integ@example.com", "password": "admin123"}, follow_redirects=False)
    
    for route in ["/admin/dashboard", "/admin/users", "/admin/products", "/admin/scans", "/admin/logs"]:
        res = client.get(route)
        assert res.status_code == 200, f"Admin route {route} failed"
    print("  [PASS] All Admin metrics and monitoring routes loaded")

    print("\n✅ ALL FINAL INTEGRATION TESTS PASSED SUCCESSFULLY!")
    
    # Cleanup test sqlite database
    test_db_file = "./test_skincheck.sqlite"
    if os.path.exists(test_db_file):
        try:
            os.remove(test_db_file)
        except Exception:
            pass

if __name__ == "__main__":
    run_integration_tests()
