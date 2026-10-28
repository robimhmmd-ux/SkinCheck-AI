import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fastapi.testclient import TestClient
from app.main import app
from app.config.database import SessionLocal
from app.models.product import Product

client = TestClient(app)
db = SessionLocal()

print("=== PRODUCT CATALOG VERIFICATION TESTS ===")

# Test 1: Authorization (Customer shouldn't access Admin routes)
print("\n[1] Test Authorization (Customer vs Admin)")
client.post('/login', data={'email': 'user@skincheck.internal', 'password': 'user123456'}, follow_redirects=False) # Login as customer
res_cust = client.get('/admin/products', follow_redirects=False)
if res_cust.status_code == 303 and '/dashboard' in res_cust.headers.get('location', ''):
    print("  [PASS] Customer blocked from /admin/products (Redirected to /dashboard)")
else:
    print(f"  [FAIL] Customer access gave status {res_cust.status_code}, location: {res_cust.headers.get('location')}")

# Login as admin for remaining tests
# Assuming admin login route is /admin/login (from auth_guard)
res_admin_login = client.post('/admin/login', data={'email': 'admin@skincheck.internal', 'password': 'adminsecurepassword'}, follow_redirects=False)
if res_admin_login.status_code == 303:
    print(f"  [PASS] Admin login successful")
else:
    print(f"  [FAIL] Admin login failed: {res_admin_login.status_code}")

# Test 2: Admin CRUD - Create
print("\n[2] Test Admin CRUD - Create")
res_create = client.post('/admin/products', data={
    'brand': 'TestBrand',
    'name': 'Super Healing Salve',
    'category': 'treatment',
    'description': 'A nice salve',
    'usage_guidance': 'Use daily',
    'ingredients': 'Centella, Madecassoside',
    'skin_concern': 'luka, kemerahan',
    'status': 'active'
}, follow_redirects=False)

if res_create.status_code == 303:
    print("  [PASS] Product created successfully (redirect 303)")
else:
    print(f"  [FAIL] Product creation failed: {res_create.status_code}")

# Verify in DB
prod = db.query(Product).filter(Product.name == 'Super Healing Salve').first()
if prod and 'Centella' in prod.get_ingredients():
    print("  [PASS] Product found in DB with correct ingredients")
else:
    print("  [FAIL] Product not found in DB or wrong data")

# Test 3: Admin CRUD - Read (Search & Filter)
print("\n[3] Test Admin CRUD - Read (Search)")
res_search = client.get('/admin/products?search=Super Healing&category=treatment')
if res_search.status_code == 200 and 'Super Healing Salve' in res_search.text:
    print("  [PASS] Product found in search results HTML")
else:
    print("  [FAIL] Search failed")

# Test 4: Admin CRUD - Update
print("\n[4] Test Admin CRUD - Update")
if prod:
    res_update = client.post(f'/admin/products/{prod.id}/edit', data={
        'brand': 'TestBrand Updated',
        'name': 'Super Healing Salve',
        'category': 'treatment',
        'status': 'active',
        'ingredients': 'Centella'
    }, follow_redirects=False)

    db.refresh(prod)
    if prod.brand == 'TestBrand Updated':
        print("  [PASS] Product updated successfully")
    else:
        print("  [FAIL] Product update failed")

# Test 5: Admin CRUD - Delete/Deactivate
print("\n[5] Test Admin CRUD - Deactivate")
if prod:
    res_delete = client.post(f'/admin/products/{prod.id}/delete', follow_redirects=False)
    db.refresh(prod)
    if prod.status == 'inactive':
        print("  [PASS] Product deactivated successfully")
    else:
        print("  [FAIL] Product deactivation failed")

# Test 6: AI Recommendation (Product Catalog Context)
# Login back as customer
client.post('/login', data={'email': 'user@skincheck.internal', 'password': 'user123456'}, follow_redirects=False)
print("\n[6] Test AI Recommendation")
payload = {"message": "Tolong rekomendasikan produk untuk kemerahan."}
res_ai = client.post("/assistant/chat", json=payload)
if res_ai.status_code == 200:
    resp_text = res_ai.json().get('response', '')
    print(f"  AI: {resp_text[:150]}...")
    if "Produk yang dapat dipertimbangkan" in resp_text:
         print("  [PASS] Used correct framing wording ('Produk yang dapat dipertimbangkan')")
    else:
         print("  [WARNING] Framing wording not detected perfectly (check manually)")
         
    if "Niacinamide 5% Serum" in resp_text or "Centella" in resp_text or "TestBrand" in resp_text:
         print("  [PASS] Recommended correct product from catalog based on DB")
    else:
         print("  [WARNING] Expected product not found in response")
else:
    print(f"  [FAIL] AI Chat error: {res_ai.status_code}")

# Test 7: AI Empty State / Fake Product Search
print("\n[7] Test AI Empty/Fake Product")
payload = {"message": "Rekomendasikan produk merk FakeGlow Potion dong."}
res_ai_fake = client.post("/assistant/chat", json=payload)
if res_ai_fake.status_code == 200:
    resp_text = res_ai_fake.json().get('response', '')
    if "FakeGlow Potion" not in resp_text or "tidak memiliki" in resp_text.lower() or "tidak ada" in resp_text.lower() or "katalog" in resp_text.lower():
         print("  [PASS] AI handled fake product request correctly")
    else:
         print(f"  [WARNING] AI might have hallucinated: {resp_text[:100]}")
else:
    print(f"  [FAIL] AI Chat error")

print("\n=== TESTS COMPLETE ===")
db.close()
