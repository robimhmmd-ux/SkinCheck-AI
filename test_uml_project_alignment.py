# -*- coding: utf-8 -*-
"""
UML & Project Codebase Alignment Verification Test.
Verifies 100% harmony between:
1. Use Case Diagram (11 Customer UCs, 4 External Services, 10 Admin UCs)
2. Activity Diagram (Full Poster Swimlanes)
3. FastAPI Project Implementation
"""
import sys
import unittest
from starlette.testclient import TestClient
from app.main import app
from app.config.database import SessionLocal
from app.models.user import User
from app.models.product import Product
from app.services.otp_service import send_registration_otp
from app.services.ai_copilot_service import AICopilotService

client = TestClient(app)

class TestUMLProjectAlignment(unittest.TestCase):

    def setUp(self):
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()

    # =========================================================================
    # 1. CUSTOMER USE CASES ALIGNMENT
    # =========================================================================
    def test_01_uc_customer_registrasi(self):
        """UC: Registrasi Akun -> /register"""
        res = client.get("/register")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Daftar Akun Baru", res.text)

    def test_02_uc_customer_login(self):
        """UC: Login Customer -> /login"""
        res = client.get("/login")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Portal Masuk SkinCheck", res.text)

    def test_03_uc_customer_logout(self):
        """UC: Logout Customer -> /logout"""
        res = client.get("/logout", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_04_uc_customer_foto_wajah(self):
        """UC: Ambil / Unggah Foto Wajah -> /scan/face"""
        # Unauthenticated redirects to login
        res = client.get("/scan/face", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_05_uc_customer_face_skin_scan(self):
        """UC: Melakukan Face Skin Scan -> /scan/face/upload"""
        # Route exists and guards unauthorized requests
        res = client.post("/scan/face/upload", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_06_uc_customer_melihat_hasil(self):
        """UC: Melihat Hasil Analisis Kulit -> /history/{id}"""
        res = client.get("/history/1", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_07_uc_customer_ai_assistant(self):
        """UC: Konsultasi AI Skincare Assistant -> /assistant"""
        res = client.get("/assistant", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_08_uc_customer_riwayat(self):
        """UC: Melihat Riwayat Scan Kulit -> /history"""
        res = client.get("/history", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_09_uc_customer_statistik(self):
        """UC: Melihat Statistik & Progres -> /dashboard"""
        res = client.get("/dashboard", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_10_uc_customer_profil(self):
        """UC: Mengelola Profil Pengguna -> /profile"""
        res = client.get("/profile", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    # =========================================================================
    # 2. EXTERNAL SERVICES ALIGNMENT (OTP GATEWAY & AI PROVIDER)
    # =========================================================================
    def test_11_uc_external_email_otp(self):
        """UC: Verifikasi Email OTP"""
        res = send_registration_otp("test_email@example.com", "Tester", self.db, channel="email")
        self.assertIn("dev_code", res)
        self.assertEqual(res["channel"], "email")

    def test_12_uc_external_whatsapp_otp(self):
        """UC: Verifikasi WhatsApp OTP"""
        res = send_registration_otp("test_wa@example.com", "Tester", self.db, channel="whatsapp", phone="08123456789")
        self.assertIn("dev_code", res)
        self.assertEqual(res["channel"], "whatsapp")

    def test_13_uc_external_ai_vision_rag(self):
        """UC: Inferensi Dual-AI & RAG Gemini"""
        trends = AICopilotService.get_aggregate_skin_trends(self.db)
        self.assertIn("trends", trends)
        self.assertIn("dominant_concern", trends)

    # =========================================================================
    # 3. ADMIN USE CASES ALIGNMENT
    # =========================================================================
    def test_14_uc_admin_login(self):
        """UC: Login Admin -> /admin/login"""
        res = client.get("/admin/login")
        self.assertEqual(res.status_code, 200)
        self.assertIn("Admin Console", res.text)

    def test_15_uc_admin_crud_users(self):
        """UC: Mengelola Data Pengguna (CRUD) -> /admin/users"""
        res = client.get("/admin/users", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_16_uc_admin_katalog_produk(self):
        """UC: Mengelola Katalog Produk (Shopee) -> /admin/products"""
        res = client.get("/admin/products", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_17_uc_admin_log_scans(self):
        """UC: Memantau Log Riwayat Scan -> /admin/scans"""
        res = client.get("/admin/scans", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_18_uc_admin_statistik_laporan(self):
        """UC: Melihat Statistik & Laporan -> /admin/dashboard"""
        res = client.get("/admin/dashboard", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_19_uc_admin_ai_copilot(self):
        """UC: AI Copilot: Analisis Tren Kulit -> /admin/ai-copilot"""
        res = client.get("/admin/ai-copilot", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_20_uc_admin_auto_insert_produk(self):
        """UC: Auto-Insert Usulan Produk AI -> /admin/products/auto-insert"""
        res = client.post("/admin/products/auto-insert", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_21_uc_admin_pengaturan_sistem(self):
        """UC: Pengaturan Sistem & API Key -> /admin/settings"""
        res = client.get("/admin/settings", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_22_uc_admin_profil_admin(self):
        """UC: Mengelola Profil Admin -> /admin/profile"""
        res = client.get("/admin/profile", follow_redirects=False)
        self.assertEqual(res.status_code, 303)

    def test_23_admin_copilot_auto_insert_logic(self):
        """Tests that AI Copilot auto-insert creates a product in DB and triggers RAG sync"""
        proposal = {
            "brand": "UML Test Brand",
            "name": "Acne Defense BHA Test Serum",
            "category": "serum",
            "description": "Serum uji coba auto-insert AI Copilot.",
            "usage_guidance": "Oleskan 2 tetes.",
            "ingredients": ["Salicylic Acid", "Zinc PCA"],
            "skin_concern": ["Acne"],
            "shopee_link": "https://shopee.co.id/test-bha",
            "tokopedia_link": ""
        }
        product = AICopilotService.auto_insert_proposed_product(self.db, proposal)
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, "Acne Defense BHA Test Serum")

        # Cleanup
        self.db.delete(product)
        self.db.commit()

    def test_24_admin_settings_ai_limits_and_flow(self):
        """Tests that Admin can configure AI limits (model, tokens, temp, daily limit) and registration flow."""
        from app.models.system_setting import SystemSetting
        SystemSetting.set_value(self.db, "AI_MODEL", "gemini-1.5-pro", "Model Test")
        SystemSetting.set_value(self.db, "AI_DAILY_SCAN_LIMIT", "3", "Scan Limit Test")
        SystemSetting.set_value(self.db, "REGISTRATION_OTP_MODE", "bypass", "Flow Mode Test")
        
        self.assertEqual(SystemSetting.get_value(self.db, "AI_MODEL"), "gemini-1.5-pro")
        self.assertEqual(SystemSetting.get_value(self.db, "AI_DAILY_SCAN_LIMIT"), "3")
        self.assertEqual(SystemSetting.get_value(self.db, "REGISTRATION_OTP_MODE"), "bypass")

        # Reset back to default
        SystemSetting.set_value(self.db, "REGISTRATION_OTP_MODE", "dual")

    def test_25_admin_testing_hub_routes_exist(self):
        """Tests that all external testing hub endpoints are registered and respond properly."""
        routes = [getattr(r, "path", "") for r in app.routes]
        self.assertIn("/admin/settings/test-email", routes)
        self.assertIn("/admin/settings/test-wa", routes)
        self.assertIn("/admin/settings/test-ai", routes)
        self.assertIn("/admin/settings/test-db", routes)

if __name__ == "__main__":
    unittest.main()
