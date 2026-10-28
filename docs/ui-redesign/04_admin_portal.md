# 🛡️ Keyframe Prompts 04 — Admin Command Center & Testing Hub

Dokumen ini memuat prompt perancangan keyframe UI/UX untuk seluruh modul Admin Command Center di platform **SkinCheck AI**:
1. **Admin Secure Gateway Login** ([app/views/pages/admin/login.html](../../app/views/pages/admin/login.html))
2. **Executive Analytics Dashboard** ([app/views/pages/admin/dashboard.html](../../app/views/pages/admin/dashboard.html))
3. **System Flow, AI Boundaries & Live Diagnostic Testing Hub** ([app/views/pages/admin/settings.html](../../app/views/pages/admin/settings.html))
4. **Admin AI Copilot & Catalog Syncer** ([app/views/pages/admin/ai_copilot.html](../../app/views/pages/admin/ai_copilot.html))
5. **User Management & Account Controls** ([app/views/pages/admin/users/index.html](../../app/views/pages/admin/users/index.html))
6. **Skincare Product Catalog & Ingredients Editor** ([app/views/pages/admin/products/index.html](../../app/views/pages/admin/products/index.html))
7. **Global Skin Scans Audit & Image Inspector** ([app/views/pages/admin/scans/index.html](../../app/views/pages/admin/scans/index.html))
8. **System Activity Audit Logs & Admin Profile** ([app/views/pages/admin/logs/index.html](../../app/views/pages/admin/logs/index.html))

---

## 📋 Prompt 04.1: Admin Secure Gateway Login (admin/login.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin Secure Gateway Login Portal (admin/login.html).

Visual Identity & Aesthetic:
- Ultra-clean, authoritative enterprise security portal with high visual discipline.
- Soft pearl slate canvas (#f8fafc), Pure white card (#ffffff) with high-contrast slate borders (#cbd5e1).
- Deep Sapphire (#1e40af), High-contrast slate typography (#0f172a), Crimson (#e11d48) for security alerts.

Component Layout:
1. Centered Enterprise Card (Max width: 420px):
   - Secure Emblem: 56px hexagonal emblem with icon bi-shield-lock-fill (#1e40af on soft tint #eff6ff).
   - System Title: "SkinCheck Admin Console" (Outfit 700, 24px, #0f172a).
   - Security Notice Pill: "Area Terbatas — Khusus Administrator Sistem" (Soft amber tint #fffbeb, text #b45309).
2. Input Fields:
   - Admin Username / Email: Input with bi-person-badge icon, border 1px solid #cbd5e1.
   - Master Password: Input with bi-key icon and eye toggle.
   - Security Key / 2FA Pin field (if enabled).
3. Login Action:
   - Primary Secure Button: "Autentikasi & Buka Konsol Admin" (background: #1e40af, height: 46px, rounded: 8px).
4. System Integrity Footer:
   - "Terhubung ke Database XAMPP MySQL (127.0.0.1:3306) • Sesi terenkripsi SHA-256".
```

---

## 📋 Prompt 04.2: Admin Executive Analytics Dashboard (admin/dashboard.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin Executive Analytics Dashboard (admin/dashboard.html).

Visual Identity & Aesthetic:
- High-density, crystal-clear operational command center for platform administrators.
- Pure white cards (#ffffff), hairline borders (#e2e8f0), soft pearl canvas (#f8fafc).
- Crisp data visualization with primary blue (#2563eb), teal (#0d9488), amethyst (#8b5cf6), and amber (#d97706).

Dashboard Architecture & Widgets:
1. Top KPI Metric Cards (Row of 4 Cards):
   - Card 1: Total Pengguna Terdaftar (Counter: 1,428 • Trend: +12% minggu ini) with icon bi-people-fill.
   - Card 2: Total Scan Wajah Selesai (Counter: 6,892 • Trend: +28% minggu ini) with icon bi-camera-fill.
   - Card 3: Rata-rata Latensi Gemini AI (Metric: 820 ms • Status: Optimal) with icon bi-cpu-fill.
   - Card 4: Status Database XAMPP (Metric: Online • MySQL 10.4 MariaDB) with icon bi-database-check (green dot).
2. Visual Charts Row:
   - Left Chart (65% width): Line/Area chart of Daily Scan Volume over the past 30 days (Smooth gradient fill in soft blue).
   - Right Chart (35% width): Donut chart of Diagnosed Skin Types (Oily: 38%, Combination: 32%, Dry: 18%, Sensitive: 12%).
3. Operational Status & Quick Actions:
   - Live System Status pill banner: "Semua Layanan Berjalan Normal (SMTP, WA Gateway, AI Engine)".
   - Quick Action buttons: "Kelola Pengguna", "Tambah Produk Skincare", "Pengaturan AI & Flow".
4. Recent User Activity & Scans Feed:
   - Compact table showing last 5 scans: Thumbnail, User Name, Skin Type, Sunscreen Score, Timestamp, and Inspect button.
```

---

## 📋 Prompt 04.3: System Flow, AI Boundaries & Live Diagnostic Testing Hub (admin/settings.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the System Flow, AI Boundaries & Live Diagnostic Testing Hub (admin/settings.html).

Visual Identity & Aesthetic:
- Enterprise configuration and diagnostic powerhouse for the Super User.
- Clean white modular cards (#ffffff), 1px hairline borders (#e2e8f0), clear functional groupings.
- Interactive AJAX testing cards with real-time spinners, status badges, and latency chips.

Layout & Module Breakdown:
1. Page Header:
   - Title: "Pengaturan Sistem, Batasan AI & Diagnostic Hub" (Outfit 700, 28px).
   - Subtitle: "Kelola API Key, tetapkan batasan model kecerdasan buatan, atur alur registrasi, dan uji koneksi gateway eksternal secara live."
2. Module 1: Konfigurasi AI & Batasan Parameter (Google Gemini):
   - API Key Field: Obfuscated input with visibility toggle and 'Update Key' button.
   - Pilihan Model AI: Segmented selector between [gemini-1.5-flash (Cepat & Hemat)] and [gemini-1.5-pro (Analisis Mendalam)].
   - Max Output Tokens: Slider & numeric input (Range: 512 s.d. 4096 tokens, default 2048).
   - AI Temperature (Kreativitas): Slider from 0.2 (Deterministik Medis) to 1.0 (Kreatif).
   - Kuota Scan Harian per Pengguna: Number input (e.g. 10 scan/hari).
   - Fallback Simulation Switch: Toggle switch "Otomatis beralih ke simulasi cerdas saat kuota API habis".
3. Module 2: Pengaturan Alur Registrasi & Pemeliharaan:
   - Alur Verifikasi Pendaftaran: 4-option radio card selector:
     1. [Dual OTP (Email + WhatsApp)] - Keamanan Maksimal.
     2. [Hanya Verifikasi Email].
     3. [Hanya Verifikasi WhatsApp].
     4. [Bypass OTP (Langsung Masuk)] - Mode Pengujian Cepat.
   - Mode Pemeliharaan Sistem (Maintenance Mode): Toggle switch with confirmation modal.
4. Module 3: Live Diagnostic Testing Hub (Interactive AJAX Test Cards):
   - Grid of 4 Diagnostic Cards:
     - Card A (Test SMTP Email OTP): Test button "Uji Kirim Email", target email input, status badge, latency display in ms.
     - Card B (Test WhatsApp Gateway): Test button "Uji Ping WA", endpoint display, authorization badge, latency display.
     - Card C (Test Google Gemini AI): Test button "Ping Model AI", prompt test input, live response preview box, latency display.
     - Card D (Test Database XAMPP MySQL): Test button "Cek Koneksi MySQL", table row counters (users, scans, products, logs), query latency display.
   - Interactive State: Clicking any test button shows a sleek spinner, followed by a soft green badge "Sukses (210ms)" or soft red badge "Gagal (Timeout)".
```

---

## 📋 Prompt 04.4: Admin AI Copilot & Catalog Syncer (admin/ai_copilot.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin AI Copilot & Catalog Syncer (admin/ai_copilot.html).

Visual Identity & Aesthetic:
- High-tech, clean intelligence dashboard for inspecting AI reasoning and catalog synchronization.
- Soft pearl canvas (#f8fafc), white cards (#ffffff), hairline borders (#e2e8f0), amethyst accents (#8b5cf6).

Interface Sections:
1. AI Intelligence Overview:
   - Model Card: "Gemini 1.5 Active", "Status: Sinkron", "Total Pemanggilan API: 14,820".
   - Token Consumption Gauge: Daily and monthly token usage progress bars.
2. Skincare Product Catalog Matching Engine:
   - Index Status: "520 Produk Terindeks untuk Rekomendasi Cerdas".
   - Re-index Button: "Sinkronkan Ulang Katalog Produk ke AI Engine" (with spinning gear icon).
3. Interactive Prompt Playground / Tester:
   - Textarea for input prompt: Test how the AI diagnoses a sample skin condition and checks sunscreen coverage.
   - Raw JSON Response Inspector: Collapsible code viewer with syntax highlighting showing confidence scores and active ingredients matches.
```

---

## 📋 Prompt 04.5: User Management & Account Controls (admin/users/index.html & form.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the User Management & Account Controls Screen (admin/users/index.html & form.html).

Visual Identity & Aesthetic:
- Clean, high-density tabular data management with instant filtering, sorting, and inline status toggles.
- Pure white container card (#ffffff), 1px hairline border (#e2e8f0), soft pearl background (#f8fafc).

Table & Management Components:
1. Header & Quick Actions:
   - Title: "Manajemen Pengguna" with user count badge (1,428 Users).
   - Search bar: Real-time search by name, email, or phone number.
   - Filter dropdowns: Role (Semua, Customer, Admin), Status (Aktif, Nonaktif, Belum Verifikasi).
   - Add User CTA: Button "Tambah Pengguna Baru" (#2563eb, rounded: 8px).
2. Data Table Structure:
   - Columns: [Avatar & Nama], [Email & Telepon], [Role Badge], [Status Verifikasi], [Jumlah Scan], [Tanggal Bergabung], [Aksi].
   - Badges: Role 'Admin' in soft red (#fff1f2, text #e11d48), 'Customer' in soft blue (#eff6ff, text #1d4ed8).
   - Status Badge: 'Terverifikasi' in soft green (#ecfdf5, text #059669).
3. Action Dropdown / Buttons:
   - Quick icons: Edit User (bi-pencil), Reset Password (bi-key), Toggle Status (bi-toggle-on), Delete User (bi-trash in soft red).
4. User Form Modal / Drawer (form.html):
   - Clean floating modal with fields for Name, Email, WhatsApp Phone, Password Override, and Role assignment switch.
```

---

## 📋 Prompt 04.6: Skincare Product Catalog & Ingredients Editor (admin/products/index.html & form.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Skincare Product Catalog & Ingredients Editor (admin/products/index.html & form.html).

Visual Identity & Aesthetic:
- Premium e-commerce inventory and dermatological ingredient database manager.
- Pure white cards (#ffffff), hairline borders (#e2e8f0), soft teal (#0d9488) accents for product efficacy.

Catalog & Form Architecture:
1. Product Inventory Table (index.html):
   - Search & Category Filter: Cleanser, Toner, Serum, Sunscreen, Moisturizer, Treatment.
   - Columns: [Thumbnail], [Nama Produk & Brand], [Kategori], [Target Tipe Kulit (Pill Tags)], [SPF/PA Rating], [Status Rekomendasi], [Aksi].
   - Add Product CTA: "Tambah Produk Baru" with plus icon.
2. Product Editor Form (form.html):
   - Two-column clean form:
     - Left Column: Product Name, Brand, Category, Price, Affiliate/Store Link, Image Upload Dropzone with live thumbnail preview.
     - Right Column:
       - Target Skin Types: Multi-checkbox (Oily, Dry, Combination, Sensitive, Acne-prone).
       - Key Active Ingredients: Interactive tag input (e.g. Niacinamide 10%, Hyaluronic Acid, Zinc PCA).
       - Sunscreen Metrics (if category = Sunscreen): SPF value (e.g. SPF 50+), PA rating (PA++++), UV Filter Type (Physical, Chemical, Hybrid).
       - Rekomendasi AI Toggle: "Sertakan dalam Rekomendasi Otomatis AI".
```

---

## 📋 Prompt 04.7: Global Skin Scans Audit & Image Inspector (admin/scans/index.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Global Skin Scans Audit & Image Inspector (admin/scans/index.html).

Visual Identity & Aesthetic:
- Clinical image inspection and quality assurance console for system administrators.
- Pure white cards (#ffffff), 1px hairline border (#e2e8f0), soft pearl canvas (#f8fafc).

Console Features & Layout:
1. Audit Header & Quality Stats:
   - Metrics: "Total Scan Bulan Ini: 2,410", "Tingkat Akurasi Rata-rata: 96.2%", "Scan dengan Coverage Sunscreen < 50%: 14%".
2. Scans Data Grid:
   - Thumbnail preview with hover zoom.
   - User Name & ID, Diagnosis Result (Skin Type & Acne count), Sunscreen Coverage %, Execution Time, Model Version.
3. Detailed Scan Inspector Drawer / Modal:
   - Side-by-side view: Original face photo vs AI Annotated Segmentation Overlay.
   - Raw parameter telemetry: Sebum index, hydration score, pore density.
   - Admin action: "Flag Scan" (for review), "Hapus Gambar (Privacy Compliance)", "Download Arsip".
```

---

## 📋 Prompt 04.8: System Activity Audit Logs & Admin Profile (admin/logs/index.html & admin/profile.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the System Activity Audit Logs & Admin Profile Screen (admin/logs/index.html & admin/profile.html).

Visual Identity & Aesthetic:
- High-security compliance audit trail and administrator credential management.
- Pure white cards (#ffffff), hairline borders (#e2e8f0), monospaced log text (#0f172a).
- Severity indicators: INFO (#0284c7), WARNING (#d97706), CRITICAL/ERROR (#e11d48), SUCCESS (#059669).

Layout & Functional Structure:
1. Audit Log Viewer (logs/index.html):
   - Real-time event stream table.
   - Filter bar: Event Category (AUTH, SCAN, AI_CALL, CONFIG_CHANGE, DB_QUERY), Date Range, Severity level.
   - Columns: [Timestamp (YYYY-MM-DD HH:mm:ss)], [Aktor / Admin IP], [Kategori Event], [Status / Severity], [Deskripsi Aktivitas], [Detail Payload JSON].
   - Expandable row revealing JSON payload and request headers.
   - Export Button: "Export CSV / JSON Log".
2. Admin Profile & Security Settings (admin/profile.html):
   - Administrator Identity Card: Name, Email, Role (Super User), Last Login Timestamp.
   - Security Credentials: Password change form with current password verification.
   - Active Sessions List: Active IP addresses and devices with "Revoke Other Sessions" button.
```
