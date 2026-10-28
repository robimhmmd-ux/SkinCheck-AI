# 🎨 SkinCheck AI — UI Redesign Keyframe Prompts

Dokumen ini memuat kumpulan prompt terstruktur bagi UI/UX Designer / Generative AI Design Tool untuk merancang *keyframe* antarmuka seluruh halaman platform **SkinCheck AI**.

Seluruh prompt di direktori ini didasarkan secara ketat pada panduan desain di [DESIGN.md](../../DESIGN.md) dengan estetika **SkinCheck Lumière (Bright Minimalist)**:
* **Tema**: *Minimalis, Bright & Elegan (Clinical Precision meets Dermatological Luxury)*
* **Palet Warna**:
  * Primary: `#2563eb` (Sapphire Authority)
  * Secondary: `#0d9488` (Derm Teal)
  * Accent: `#8b5cf6` (AI Copilot Amethyst)
  * Canvas & Surface: `#ffffff` (Pure White Card) & `#f8fafc` (Soft Pearl Slate)
  * Outline: `#e2e8f0` (1px Hairline Crisp Border)
  * Text: `#0f172a` (High-Contrast Slate) & `#64748b` (Muted Slate)
* **Tipografi**: Heading `Outfit` (Bold, geometris) & Body `Plus Jakarta Sans` (Humanis, bersih, terstruktur).
* **Standar Sudut**: `8px` (Inputs & Buttons), `12px - 16px` (Cards & Viewfinders).

---

## 📂 Struktur Dokumen Prompt

1. **[Master Keyframe Prompts (Seluruh Halaman)](KEYFRAME_PROMPTS.md)**: Dokumen gabungan lengkap yang memuat 18 prompt keyframe halaman dari landing page, alur autentikasi, customer portal, hingga admin diagnostic hub.
2. **[01. Landing Page](01_landing_page.md)**: Prompt keyframe untuk Halaman Beranda Publik (`home.html`).
3. **[02. Auth Pages](02_auth_pages.md)**: Prompt keyframe untuk Login (`login.html`), Registrasi (`register.html`), dan Dual OTP Verification (`verify_otp.html`).
4. **[03. Customer Portal](03_customer_portal.md)**: Prompt keyframe untuk Dashboard, Face Scanner Kamera, Scan Detail Report, History Scan, AI Skincare Assistant, dan Profil Pelanggan.
5. **[04. Admin Management & Diagnostic Hub](04_admin_portal.md)**: Prompt keyframe untuk Admin Login, Executive Dashboard, Settings & Live Testing Hub, AI Copilot, User Management, Product Catalog, Scans Audit, Logs, dan Admin Profile.

---

## 📌 Kaidah Format Prompt
Setiap prompt wajib diawali dengan kalimat kunci:
```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for [Nama Halaman / Konteks Fitur] ...
```
Dan dilengkapi dengan:
- **Design Tokens**: Spesifikasi warna, tipografi, dan radius.
- **Layout Architecture**: Struktur grid, container, dan hierarki visual.
- **Key UI Components**: Elemen interaktif, data display, dan kartu status.
- **Micro-Interactions & States**: Default, hover, active, empty, dan error state.
- **Aesthetic Principles**: Panduan mempertahankan estetika *bright minimalist* tanpa visual noise.
