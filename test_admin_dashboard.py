import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from fastapi.testclient import TestClient
from app.main import app
from app.config.database import SessionLocal
from app.models.user import User

client = TestClient(app)
db = SessionLocal()

print("=== ADMIN DASHBOARD VERIFICATION TESTS ===")

# Test 1: Authorization
print("\n[1] Test Authorization (Customer attempting to access admin)")
client.post('/login', data={'email': 'user@skincheck.internal', 'password': 'user123456'}, follow_redirects=False)
res_cust = client.get('/admin/dashboard', follow_redirects=False)
if res_cust.status_code == 303:
    print("  [PASS] Customer blocked from /admin/dashboard (Redirected)")
else:
    print(f"  [FAIL] Customer access gave status {res_cust.status_code}")

# Login as admin
client.post('/admin/login', data={'email': 'admin@skincheck.internal', 'password': 'adminsecurepassword'}, follow_redirects=False)

# Test 2: Dashboard Metrics
print("\n[2] Test Admin Dashboard Metrics")
res_dash = client.get('/admin/dashboard')
if res_dash.status_code == 200 and 'Admin Dashboard' in res_dash.text:
    print("  [PASS] Admin Dashboard loaded successfully")
else:
    print(f"  [FAIL] Admin Dashboard failed: {res_dash.status_code}")

# Test 3: User CRUD - Create & Read
print("\n[3] Test User CRUD - Create & Read")
res_create = client.post('/admin/users', data={
    'name': 'New Admin Test User',
    'email': 'admin_test_user@example.com',
    'password': 'password123',
    'status': 'active'
}, follow_redirects=False)

if res_create.status_code == 303:
    print("  [PASS] User created successfully")
else:
    print(f"  [FAIL] User creation failed: {res_create.status_code}")

res_users = client.get('/admin/users?search=New Admin')
if res_users.status_code == 200 and 'New Admin Test User' in res_users.text:
    print("  [PASS] User found in search results HTML")
else:
    print("  [FAIL] Search user failed")

new_user = db.query(User).filter(User.email == 'admin_test_user@example.com').first()

# Test 4: User CRUD - Update
print("\n[4] Test User CRUD - Update")
if new_user:
    res_update = client.post(f'/admin/users/{new_user.id}/edit', data={
        'name': 'New Admin Test User Edited',
        'email': 'admin_test_user@example.com',
        'password': '',
        'status': 'inactive'
    }, follow_redirects=False)
    
    db.expire_all()
    updated_user = db.query(User).filter(User.id == new_user.id).first()
    if updated_user and updated_user.name == 'New Admin Test User Edited' and updated_user.status == 'inactive':
        print("  [PASS] User updated and deactivated successfully")
    else:
        print("  [FAIL] User update failed")
        
    # Clean up created test user
    if updated_user:
        db.delete(updated_user)
        db.commit()

# Test 5: Monitoring Routes (Skin Scans, Logs)
print("\n[5] Test Monitoring Routes")
res_scans = client.get('/admin/scans')
if res_scans.status_code == 200 and 'Skin Scan Monitoring' in res_scans.text:
    print("  [PASS] Skin Scan Monitoring loaded successfully")
else:
    print(f"  [FAIL] Skin Scans Monitoring failed: {res_scans.status_code}")

res_logs = client.get('/admin/logs')
if res_logs.status_code == 200 and 'Activity Logs' in res_logs.text:
    print("  [PASS] Activity Logs loaded successfully")
else:
    print(f"  [FAIL] Activity Logs failed: {res_logs.status_code}")

print("\n=== TESTS COMPLETE ===")
db.close()
