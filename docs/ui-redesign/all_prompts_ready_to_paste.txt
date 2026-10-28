As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Public Landing Page of SkinCheck AI (home.html).
- Aesthetic: Bright Minimalist, clinical luxury digital wellness.
- Canvas: Soft pearl slate (#f8fafc), Surface cards: Pure white (#ffffff), 1px hairline border (#e2e8f0), ambient shadow (rgba(15, 23, 42, 0.04)).
- Palette: Primary Sapphire (#2563eb), Medical Teal (#0d9488), Deep Slate (#0f172a), Muted Slate (#64748b).
- Typography: Headings in 'Outfit' (bold, modern), Body text in 'Plus Jakarta Sans' (clean, human-centered).
- Keyframe Layout:
  1. Sticky frosted glass navigation bar with clinic emblem, links (Fitur, Cara Kerja, Sunscreen AI, Edukasi), Soft 'Masuk' button, and Primary 'Mulai Scan Gratis' button (#2563eb, rounded 8px).
  2. Hero Section: High-impact headline "Analisis Kulit Wajah & Cek Pemerataan Sunscreen Berbasis AI Cerdas", subtitle explaining camera-based browser scanning, primary CTA "Coba Scan Wajah Sekarang" with camera icon, secondary CTA "Pelajari Teknologi Sunscreen", trust badges ("98.4% Akurasi Diagnostik", "Diverifikasi Dermatologis", "Data Terenkripsi XAMPP MySQL"). Hero split visual showing a customer face with an AR mesh overlay on the left and a UV Sunscreen Coverage heatmap on the right.
  3. Feature Grid: 3 white cards with hairline borders for Skin Diagnostics (5 parameters), Sunscreen Protection AI, and Tailored Routine & Ingredients.
  4. 4-step progressive flow cards: Ambil Foto -> Verifikasi OTP -> Analisis Gemini AI -> Laporan Klinis.
  5. Metrics ticker banner: "15,000+ Scan", "500+ Produk Skincare", "0.8s Latensi AI".
  6. Clean minimal white footer with medical disclaimer and copyright.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Global Navigation Bar & Header Component (layouts/navbar.html).
- Aesthetic: Bright Minimalist, frosted glass sticky navigation header.
- Container: Height 72px, sticky top, background rgba(255, 255, 255, 0.85), backdrop-filter blur(12px), border-bottom 1px solid #e2e8f0.
- Keyframe Layout:
  1. Left: Brand Logo featuring a stylized medical cross/leaf emblem in Sapphire Blue (#2563eb) with bold typography 'SkinCheck' (Outfit 700, 20px, #0f172a) and a micro-pill badge 'AI' (Soft Purple #f5f3ff, text #8b5cf6).
  2. Center: Navigation menu links (Beranda, Scan Wajah, Asisten AI, Edukasi Tabir Surya) with 15px font, muted slate color (#64748b), active state in primary blue (#2563eb) with subtle bottom indicator dot.
  3. Right (Unauthenticated State): Outlined pill button 'Masuk' (#f1f5f9 background, #0f172a text, 1px border #e2e8f0) and Primary CTA button 'Mulai Analisis' (#2563eb fill, white text, height 40px, rounded 8px).
  4. Right (Authenticated State): Real-time notification bell icon with unread indicator dot, user avatar circle (36px) with status ring, name dropdown menu displaying 'Dashboard Pasien', 'Riwayat Scan', 'Profil & Preferensi', and 'Keluar'.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Global Public Footer Component (layouts/footer.html).
- Aesthetic: Clean, bright minimalist clinic footer on a pure white surface (#ffffff) with a 1px hairline top divider (#e2e8f0).
- Keyframe Layout:
  1. Top Columns Grid:
     - Column 1 (Brand & Mission): SkinCheck logotype, dermatological mission statement ("Platform evaluasi kesehatan kulit dan perlindungan tabir surya cerdas berbasis standar klinis internasional"), and certifications list (ISO 27001 Data Privacy, Dermatologically Tested AI Algorithm).
     - Column 2 (Fitur & Diagnostik): Links to Analisis 5 Parameter Kulit, Evaluasi UV Sunscreen, Rekomendasi Bahan Aktif Skincare, Konsultasi Gemini AI.
     - Column 3 (Dukungan & Legalitas): Ketentuan Layanan Medis, Kebijakan Privasi Pasien, Verifikasi Dual OTP, Kontak Dermatolog.
     - Column 4 (Sistem & Konektivitas): Status sistem real-time pill ("XAMPP Database: Online", "AI Latency: 0.8s"), pilihan bahasa (ID / EN).
  2. Medical Disclaimer Box: Soft pearl container (#f8fafc) with 1px border (#e2e8f0) stating: "Peringatan Medis: Hasil analisis SkinCheck AI ditujukan sebagai panduan awal evaluasi mandiri dan tidak menggantikan diagnosis resmi dokter spesialis kulit."
  3. Bottom Copyright Bar: Hairline border top, copyright statement, and secure encryption badge.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Login Page (auth/login.html).
- Aesthetic: Bright Minimalist, high-trust authentication card on a soft pearl slate canvas (#f8fafc).
- Card Container: Max width 440px, pure white (#ffffff), 1px hairline border (#e2e8f0), rounded 16px, ambient shadow.
- Keyframe Layout:
  1. Top emblem: 48px circle with person icon in soft blue (#eff6ff background, #2563eb icon).
  2. Header: Title "Selamat Datang Kembali" (Outfit 600, 26px, #0f172a) and subtitle "Masuk ke akun SkinCheck Anda."
  3. Form Inputs:
     - Email: Label, input with 1px border (#cbd5e1), left icon bi-envelope, placeholder "nama@email.com", focus ring glow (#2563eb).
     - Password: Label with "Lupa Kata Sandi?" blue link, right eye toggle icon.
     - Remember me custom rounded checkbox.
  4. Submit Button: Full-width primary button "Masuk ke Akun" (#2563eb, height 46px, rounded 8px).
  5. Secondary: Hairline divider with pill "Belum punya akun?", outlined button "Daftar Akun Baru".
  6. Footer note: Lock icon with text "Sesi terenkripsi & data riwayat tersimpan aman di server lokal."

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Registration Page (auth/register.html).
- Aesthetic: Bright Minimalist, reassuring onboarding experience on a soft pearl slate canvas (#f8fafc).
- Card Container: Max width 480px, pure white (#ffffff), 1px hairline border (#e2e8f0), rounded 16px.
- Keyframe Layout:
  1. Top emblem: 48px circle with user-plus icon in soft teal (#f0fdfa background, #0d9488 icon).
  2. Header: Title "Buat Akun SkinCheck Baru" (Outfit 700, 26px, #0f172a) and subtitle "Mulai pemantauan kesehatan kulit dan evaluasi tabir surya Anda."
  3. Form Grid:
     - Nama Lengkap: Input with user icon.
     - Email Aktif: Input with envelope icon and OTP notice helper text.
     - Nomor WhatsApp: Input with green WhatsApp icon, country prefix "+62", placeholder "812-xxxx-xxxx".
     - Kata Sandi: Password input with eye toggle and 4-bar real-time color strength meter (Lemah, Sedang, Kuat, Sangat Aman).
     - Konfirmasi Kata Sandi: Validator with instant green checkmark icon.
  4. Consent Checkbox: "Saya menyetujui Ketentuan Layanan & Kebijakan Privasi Data Medis SkinCheck."
  5. Submit Button: Primary button "Lanjutkan ke Verifikasi OTP" with arrow icon (#2563eb, height 48px, rounded 8px).
  6. Switch to Login: Text link "Sudah punya akun? Masuk di sini".

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Dual OTP Verification Screen (auth/verify_otp.html).
- Aesthetic: High-security bright minimalist verification modal on a soft pearl slate canvas (#f8fafc).
- Card Container: Max width 500px, pure white (#ffffff), 1px hairline border (#e2e8f0), rounded 16px.
- Keyframe Layout:
  1. Security Icon: 56px pulsing circle with shield-check icon (#2563eb).
  2. Title: "Verifikasi Keamanan Akun" (Outfit 700, 24px) and subtitle "Masukkan 6 digit kode yang dikirimkan."
  3. Dual Channel Banners:
     - Email OTP Box: Soft blue (#eff6ff), masked email "u***@domain.com", badge "Terkirim".
     - WhatsApp OTP Box: Soft green (#ecfdf5), masked phone "+62 812-****-890", badge "Terkirim".
  4. 6-Box Pin Input: Six square boxes (52x58px, border 1.5px #cbd5e1, rounded 10px, font 24px Outfit bold). Active box glows with blue border (#2563eb).
  5. Timer & Resend: Circular countdown "Kirim ulang dalam 01:45", link "Kirim Ulang Kode OTP".
  6. Action: Primary button "Verifikasi & Masuk ke Dashboard" (#2563eb, rounded 8px), and secondary link "Ganti Email atau Nomor WhatsApp".

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Health Hub Dashboard (customer/dashboard.html).
- Aesthetic: Bright clinical-elegance wellness dashboard on soft pearl slate canvas (#f8fafc).
- Keyframe Layout:
  1. Welcome Header: Greeting "Halo, [Nama Pengguna] 👋" (Outfit 700, 28px), summary subtitle, and Primary CTA button "Mulai Scan Wajah Baru" with camera icon (#2563eb, rounded 8px).
  2. 3 Metric Cards Row (pure white cards, 1px border #e2e8f0):
     - Card 1 (Kondisi Kulit Terkini): Skin type badge (Kombinasi Berminyak), health score dial (86/100) with emerald progress circle.
     - Card 2 (Proteksi Sunscreen): Coverage gauge (92% Merata), active protection badge, reminder "Re-aplikasi dalam 2 jam".
     - Card 3 (Riwayat Scan): Stat counter "12 Sesi Scan", trend indicator "+4% Peningkatan Hidrasi".
  3. Daily Skincare Routine Tracker: Tabbed checklist cards for Rutinitas Pagi (Cleanser, Vit C, Moisturizer, SPF 50) and Rutinitas Malam (Double Cleanse, Retinol, Night Cream) with animated checkboxes.
  4. Recommended Products Carousel: 3 matched skincare product cards with thumbnail, brand, name, active ingredient tags (Niacinamide, Ceramide), and view button.
  5. Recent Scan Snapshot Card: Face thumbnail with annotated facial zones (T-Zone, U-Zone) and link "Lihat Laporan Lengkap".

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Real-time Face Scanner & Sunscreen Checker (customer/scan_face.html).
- Aesthetic: Medical-grade camera interface with high clarity on a soft pearl canvas (#f8fafc).
- Viewport Container: Max width 560px, rounded 16px, dark clinical camera stream bordered by crisp white diagnostic controls.
- Keyframe Layout:
  1. Top Mode Switcher (Segmented Pill Toggle): [Mode 1: Analisis Kondisi Kulit (Jerawat, Minyak, Pori)] vs [Mode 2: Deteksi Pemerataan Sunscreen (UV Coverage)].
  2. Camera Viewport:
     - Live video stream with smooth rounded corners (16px).
     - AR Face Mesh Guide: Semi-transparent white oval with corner alignment brackets turning emerald (#059669) when aligned.
     - Lighting Meter Badge: Floating pill "Pencahayaan: Optimal (Lux OK)" with green status dot.
     - Laser Sweep Scan Line: Animated glowing vertical laser (#2563eb) sweeping downwards during capture.
  3. Guidance Pill: Floating text at bottom "Posisikan wajah Anda di dalam bingkai oval dan pastikan cahaya merata."
  4. Shutter Controls:
     - Center Shutter Button: 72px outer ring, 56px inner circle in sapphire blue (#2563eb) with camera icon.
     - Camera switch button (front/back) and lighting toggle.
     - Fallback dropzone: "Atau Unggah Foto dari Galeri" with dashed border.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Camera Permission & Error Fallback UI (customer/placeholders/scan_ui.html).
- Aesthetic: Calming, user-friendly diagnostic guidance screen on soft pearl slate (#f8fafc).
- Container Card: Max width 480px, pure white (#ffffff), 1px border (#e2e8f0), rounded 16px.
- Keyframe Layout:
  1. Central Illustrated Icon: Webcam icon with soft warning amber circle badge (#fffbeb background, #d97706 icon).
  2. Headline: "Izin Akses Kamera Diperlukan" (Outfit 700, 22px, #0f172a).
  3. Explanation: Clear, reassuring paragraph on why camera permission is needed for real-time face evaluation and privacy notice that raw camera video is processed locally.
  4. Step-by-Step Instructions: 3 mini-steps with numbered icons (1. Klik ikon gembok di browser bar -> 2. Ubah izin Kamera menjadi 'Izinkan' -> 3. Muat ulang halaman).
  5. Action Buttons: Primary button "Izinkan Kamera Sekarang" (#2563eb, rounded 8px) and Alternative button "Unggah Foto Wajah Saja" (#f1f5f9 background).

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Clinical Diagnostic Report & Routine Recommendations Screen (customer/scan_detail.html).
- Aesthetic: High-authority laboratory report on soft pearl slate canvas (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Report Header: Scan ID "#SC-98214 • 02 Okt 2026, 10:45 WIB", Skin Type badge "Kombinasi (T-Zone Berminyak)", large Sunscreen Coverage circular dial (94%), action buttons "Download PDF Medis" and "Bagikan Laporan".
  2. Split Diagnostic Visualization:
     - Left: High-resolution captured face with 3 toggleable modes: [Foto Asli] | [Heatmap Sunscreen UV] | [Peta Pori & Sebum].
     - Right: 5 Parameter Horizontal Progress Bars:
       * Hidrasi & Kelembapan: 78% (Normal/Lembap) [Hijau]
       * Minyak & Sebum: 84% (Tinggi di Dahi & Hidung) [Oranye]
       * Pori-pori: 62% (Sedang) [Biru]
       * Kemerahan: 18% (Rendah / Sehat) [Hijau]
       * Pemerataan Sunscreen: 94% (Merata Sempurna) [Teal]
  3. AI Clinical Summary Card: Amethyst AI badge (#8b5cf6) with detailed explanation by Gemini AI on UV gaps and sebum balancing.
  4. Ingredients Matrix Card:
     - Recommended Ingredients: Soft green chips (Niacinamide 4%, Hyaluronic Acid, Centella Asiatica).
     - Ingredients to Avoid: Soft red chips (Alcohol Denat, Excessive Fragrance, Mineral Oil).
  5. Matched Skincare Carousel: 4 approved skincare product cards with compatibility match score (98%), price, and store link.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Skin Progression Timeline & History Gallery (customer/history.html).
- Aesthetic: Clean, inspiring skin diary on soft pearl slate (#f8fafc), white cards (#ffffff), 1px hairline border (#e2e8f0).
- Keyframe Layout:
  1. Header & Filters: Title "Riwayat & Perkembangan Kulit" (Outfit 700, 28px), date range picker, metric filter pills (Semua, Sunscreen Coverage, Minyak, Hidrasi), and view switcher (Grid Galeri vs Garis Waktu).
  2. Interactive Before-After Comparison Card: Split image viewer with central draggable pill slider:
     - Left: "Scan Pertama (01 Jan 2026)" vs Right: "Scan Terkini (02 Okt 2026)".
     - Delta badges: "+26% Peningkatan Hidrasi", "-35% Reduksi Jerawat".
  3. Chronological Scan Grid: 3-column responsive cards with face thumbnail, scan date, skin type pill, mini progress bars (Sebum, Moisture, Sunscreen), and link "Detail Analisis →".
  4. Empty State: Clean mirror illustration, text "Belum Ada Riwayat Scan", primary button "Ambil Scan Pertama Anda".

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer AI Skincare Assistant Copilot (customer/assistant.html).
- Aesthetic: Conversational medical consultation interface on soft pearl slate (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Header Bar: 40px gradient avatar with stars icon, title "SkinCheck AI Copilot", status pill "Online • Didukung Google Gemini 1.5", active context pill "Konteks: Laporan Scan #SC-98214", and "Konsultasi Baru" button.
  2. Chat Stream:
     - Bot Messages: Pure white cards with 1px border (#e2e8f0), amethyst AI badge (#8b5cf6), friendly diagnostic advice.
     - Embedded Skincare Cards: Product recommendations inside the chat with thumbnail, active ingredients, and 'Mengapa Cocok'.
     - User Messages: Sapphire blue bubbles (#2563eb) with white text aligned right.
     - Quick Suggestion Pills: Horizontal tags ("Cara atasi kemerahan di pipi?", "Waktu re-aplikasi sunscreen?", "Niacinamide + Vitamin C?").
  3. Sticky Bottom Input Deck: 52px rounded input bar (border #cbd5e1, rounded 26px), attach scan photo button (paperclip), text input "Tanyakan apa saja seputar perawatan kulit...", and 40px circular blue send button (#2563eb).

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Floating AI Assistant Widget Drawer (customer/placeholders/assistant_ui.html).
- Aesthetic: Compact, floating consultation drawer widget that slides out from the bottom-right corner.
- Container: Floating drawer (width 380px, height 540px), pure white card (#ffffff), 1px border (#e2e8f0), rounded-top 20px, elevated shadow.
- Keyframe Layout:
  1. Widget Header: Amethyst AI avatar, title 'SkinCheck Copilot', minimize toggle icon, close button.
  2. Quick Skin Context Strip: Compact banner displaying current user's skin type ("Kulit Anda: Kombinasi Berminyak") with link to full report.
  3. Compact Message Stream: Lightweight message bubbles with micro-chips for recommended skincare active ingredients.
  4. Mini Input Deck: Text input field with instant microphone voice-input button and blue send button.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Skin Profile & Preferences Page (customer/profile.html).
- Aesthetic: Calm, organized clinical preferences center on soft pearl slate (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Profile Header Card: 80px avatar with photo upload button, User Name (Outfit 700, 22px), Email, WhatsApp number, and verification badges ("Email Terverifikasi ✓", "WhatsApp Terverifikasi ✓").
  2. Dermatological Baseline Card:
     - Rentang Usia: Dropdown (Remaja, 20-29, 30-39, 40+).
     - Tipe Kulit Utama: Radio pill selectors (Kering, Berminyak, Kombinasi, Sensitif, Normal).
     - Riwayat Alergi Kosmetik: Interactive tag input (Paraben, SLS, Fragrance, Alcohol).
     - Masalah Kulit Prioritas: Multi-select chips (Jerawat, Flek Hitam, Pori Besar, Garis Halus).
  3. Notification & Routine Reminders Card:
     - Toggle: "Pengingat Re-aplikasi Sunscreen (Setiap 2 Jam)".
     - Toggle: "Pengingat Rutinitas Malam (21:00)".
     - Toggle: "Laporan Mingguan via Email".
  4. Security Card: Ganti Kata Sandi inputs, and Primary button "Simpan Perubahan" (#2563eb, rounded 8px).

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin Layout — Sidebar Navigation & Top Bar (layouts/admin_base.html).
- Aesthetic: Enterprise command center layout with fixed left sidebar and clean top utility header.
- Left Sidebar Container: Width 260px, background pure white (#ffffff), 1px hairline right border (#e2e8f0).
- Keyframe Layout:
  1. Sidebar Header: Clinic brand logo with red Super User badge 'ADMIN CONSOLE'.
  2. Navigation Menu Groups:
     - Group 1 (Utama): Dashboard Analitik, Live Diagnostic Testing Hub.
     - Group 2 (Manajemen Medis): Data Pengguna & Pasien, Katalog Produk Skincare, Audit Riwayat Scan Global.
     - Group 3 (Sistem & AI): Konfigurasi Batasan AI, AI Copilot Syncer, Audit Activity Logs, Pengaturan Profil Admin.
  3. Active Navigation State: Soft blue background (#eff6ff), sapphire blue icon & text (#2563eb), solid 3px blue vertical left bar.
  4. Top Utility Bar: Height 64px, search bar, database health indicator pill ("XAMPP MySQL: 3306 Connected"), quick notification dropdown, and admin user profile chip.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin Secure Gateway Login Portal (admin/login.html).
- Aesthetic: Ultra-clean, authoritative enterprise security portal on soft pearl slate (#f8fafc).
- Card Container: Max width 420px, pure white (#ffffff), 1px high-contrast border (#cbd5e1), rounded 16px.
- Keyframe Layout:
  1. Secure Emblem: 56px hexagonal shield icon in deep sapphire (#1e40af on soft blue #eff6ff).
  2. Title: "SkinCheck Admin Console" (Outfit 700, 24px) and amber warning badge "Area Terbatas — Khusus Administrator".
  3. Input Fields:
     - Admin Username / Email: Input with admin-badge icon.
     - Master Password: Input with key icon and eye toggle.
  4. Action: Primary button "Autentikasi & Buka Konsol Admin" (deep sapphire #1e40af, height 46px, rounded 8px).
  5. Footer: "Terhubung ke Database XAMPP MySQL (127.0.0.1:3306) • Sesi terenkripsi SHA-256".

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin Executive Analytics Dashboard (admin/dashboard.html).
- Aesthetic: High-density operational command center on soft pearl slate (#f8fafc), white cards (#ffffff), 1px hairline border (#e2e8f0).
- Keyframe Layout:
  1. Top KPI Row (4 Cards):
     - Card 1: Total Pengguna (1,428 • +12% mgg ini) with people icon.
     - Card 2: Total Scan Wajah (6,892 • +28% mgg ini) with camera icon.
     - Card 3: Rata-rata Latensi AI (820 ms • Optimal) with cpu icon.
     - Card 4: Status Database XAMPP (Online • MariaDB 10.4) with green dot database icon.
  2. Charts Row:
     - Left (65% width): Daily Scan Volume line chart over 30 days (smooth soft blue gradient fill).
     - Right (35% width): Donut chart of Diagnosed Skin Types (Oily: 38%, Combination: 32%, Dry: 18%, Sensitive: 12%).
  3. System Status Banner: Pill alert "Semua Layanan Berjalan Normal (SMTP, WA Gateway, AI Engine)".
  4. Quick Action Buttons: "Kelola Pengguna", "Tambah Produk Skincare", "Pengaturan AI & Flow".
  5. Recent Activity Table: Last 5 scans with thumbnail, username, skin type, sunscreen score, timestamp, and inspect button.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the System Flow, AI Boundaries & Live Diagnostic Testing Hub (admin/settings.html).
- Aesthetic: Enterprise configuration and diagnostic powerhouse on soft pearl slate (#f8fafc), white modular cards (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Header: Title "Pengaturan Sistem, Batasan AI & Diagnostic Hub" (Outfit 700, 28px) and subtitle on flow control and live diagnostics.
  2. Module 1 (AI Parameters & Boundaries - Google Gemini):
     - API Key input with visibility toggle and 'Update Key' button.
     - AI Model Selector: Segmented toggle [gemini-1.5-flash (Cepat)] vs [gemini-1.5-pro (Mendalam)].
     - Max Output Tokens: Slider & numeric field (512 - 4096 tokens, default 2048).
     - Temperature Slider: 0.2 (Deterministik Medis) to 1.0 (Kreatif).
     - Daily Scan Limit per User field (e.g. 10 scan/hari).
     - Fallback Simulation Switch: Toggle "Otomatis beralih ke simulasi cerdas saat kuota API habis".
  3. Module 2 (Registration Flow & Maintenance):
     - Registration Flow Selector: 4 radio cards:
       1. [Dual OTP (Email + WhatsApp)] - Rekomendasi Keamanan.
       2. [Hanya Verifikasi Email].
       3. [Hanya Verifikasi WhatsApp].
       4. [Bypass OTP (Langsung Masuk)] - Mode Demo / Pengujian.
     - System Maintenance Mode Toggle.
  4. Module 3 (Live Diagnostic Testing Hub - Interactive AJAX Cards):
     - Grid of 4 Cards:
       * Card A (Test SMTP Email): Test button "Uji Kirim Email", target email field, status badge, latency (ms).
       * Card B (Test WhatsApp Gateway): Test button "Uji Ping WA", endpoint display, token badge, latency (ms).
       * Card C (Test Gemini AI): Test button "Ping Model AI", prompt field, live preview box, latency (ms).
       * Card D (Test XAMPP MySQL): Test button "Cek Koneksi MySQL", table row counters (users, scans, products, logs), query latency (ms).
     - Realtime testing state: Clicking test shows spinner, followed by soft green success badge ("Sukses 210ms") or soft red error badge.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin AI Copilot & Catalog Syncer (admin/ai_copilot.html).
- Aesthetic: Intelligence console on soft pearl slate (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0), amethyst accents (#8b5cf6).
- Keyframe Layout:
  1. Overview Card: "Model: Gemini 1.5 Active", "Status: Sinkron", "Total Pemanggilan: 14,820", token consumption gauges (daily and monthly).
  2. Skincare Product Catalog Matching Engine:
     - Index Status: "520 Produk Terindeks untuk Rekomendasi Cerdas".
     - Primary Button: "Sinkronkan Ulang Katalog Produk ke AI Engine" with spinning gear icon.
  3. Interactive Prompt Playground / Tester:
     - Prompt textarea to test skin diagnostic prompts and sunscreen coverage evaluation.
     - Raw JSON Response Inspector: Collapsible code container with syntax highlighting showing confidence scores and active ingredients matches.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the User Management Table Screen (admin/users/index.html).
- Aesthetic: High-density data table on soft pearl slate (#f8fafc), white card container (#ffffff), 1px hairline border (#e2e8f0).
- Keyframe Layout:
  1. Header & Controls: Title "Manajemen Pengguna" with badge "1,428 Users", real-time search input, Role filter dropdown (Semua, Customer, Admin), Status filter (Aktif, Nonaktif), and Primary button "Tambah Pengguna Baru" (#2563eb, rounded 8px).
  2. Data Table Columns: [Avatar & Nama], [Email & Telepon], [Role Badge], [Status Verifikasi], [Jumlah Scan], [Tanggal Bergabung], [Aksi].
  3. Badges: Role 'Admin' in soft red (#fff1f2, text #e11d48), 'Customer' in soft blue (#eff6ff, text #1d4ed8), Status 'Terverifikasi' in soft green (#ecfdf5, text #059669).
  4. Actions: Edit (pencil), Reset Password (key), Toggle Status (switch), Delete (trash).
  5. Pagination bar at bottom with record count indicator.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the User Add & Edit Form (admin/users/form.html).
- Aesthetic: Clean modal/drawer dialog on pure white card (#ffffff), 1px border (#e2e8f0), rounded 16px.
- Keyframe Layout:
  1. Modal Header: Title "Tambah Pengguna Baru / Edit Pengguna" with close icon.
  2. Form Fields:
     - Nama Lengkap: Text input with user icon.
     - Email Pengguna: Email input with envelope icon.
     - Nomor WhatsApp: Phone input with WhatsApp icon and country code prefix.
     - Kata Sandi: Password input with eye toggle (or "Kosongkan jika tidak ingin mengubah password").
     - Hak Akses (Role): Radio pill selector [Customer] vs [Administrator].
     - Status Akun: Toggle switch [Aktif / Terverifikasi].
  3. Modal Actions: Outlined button "Batal" (#f1f5f9) and Primary button "Simpan Data Pengguna" (#2563eb, rounded 8px).

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Skincare Product Catalog Inventory Table (admin/products/index.html).
- Aesthetic: Clean e-commerce inventory table on soft pearl slate (#f8fafc), white card container (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Header: Title "Katalog Produk Skincare" with count badge "520 Produk", search bar, Category filter pills (Semua, Cleanser, Toner, Serum, Sunscreen, Moisturizer), and Primary button "Tambah Produk Baru" (#2563eb, rounded 8px).
  2. Table Columns: [Thumbnail], [Nama Produk & Brand], [Kategori], [Target Tipe Kulit (Pill Tags)], [SPF/PA Rating], [Status Rekomendasi], [Aksi].
  3. Badges: Skin type tags (Oily, Dry, Normal, Sensitive) in soft-tint pills, Sunscreen SPF 50+ badge in orange pill.
  4. Actions: Edit product (pencil), toggle recommendation (stars icon), delete product (trash).
  5. Pagination bar at bottom.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Skincare Product Form & Ingredients Editor (admin/products/form.html).
- Aesthetic: Comprehensive dermatological product editor on soft pearl slate (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Header: Title "Tambah / Edit Produk Skincare" with back link.
  2. Two-Column Form Structure:
     - Left Column:
       * Nama Produk, Brand / Pabrik, Kategori dropdown, Harga (IDR), Link Toko / Beli.
       * Image Upload Dropzone: Drag-and-drop area with dashed border and live thumbnail preview.
     - Right Column:
       * Target Tipe Kulit: Checkboxes (Berminyak, Kering, Kombinasi, Sensitif, Berjerawat).
       * Kandungan Bahan Aktif: Interactive tag input (Niacinamide 10%, Hyaluronic Acid, Ceramide NP, Centella).
       * Spesifikasi Sunscreen (conditional): SPF value (SPF 50+), PA rating (PA++++), UV Filter Type (Physical, Chemical, Hybrid).
       * AI Recommendation Switch: Toggle "Sertakan dalam rekomendasi otomatis AI Copilot".
  3. Form Action Buttons: Outlined "Batal" and Primary "Simpan Produk Skincare" (#2563eb, rounded 8px).

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Global Skin Scans Audit & Image Inspector (admin/scans/index.html).
- Aesthetic: Clinical quality assurance console on soft pearl slate (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Audit Header: Metrics row ("Total Scan Bulan Ini: 2,410", "Akurasi: 96.2%", "Coverage Sunscreen Rendah: 14%"), search bar, and date picker.
  2. Scans Grid / Table: Columns for [Thumbnail Preview], [User ID & Nama], [Hasil Diagnosa (Skin Type & Acne count)], [Sunscreen Coverage %], [Waktu Scan], [Aksi].
  3. Detailed Scan Inspector Drawer:
     - Side-by-side view: Original face photo vs AI Annotated Segmentation Overlay.
     - Telemetry parameters: Sebum index, hydration score, pore density.
     - Admin actions: "Flag Scan", "Hapus Gambar (Privacy Compliance)", "Download Arsip".

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the System Activity Audit Logs Viewer (admin/logs/index.html).
- Aesthetic: High-security compliance audit trail on soft pearl slate (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0), monospaced log text.
- Keyframe Layout:
  1. Header & Filters: Title "Audit Log Aktivitas Sistem", filter dropdown for Category (AUTH, SCAN, AI_CALL, CONFIG_CHANGE, DB_QUERY), Date range picker, and Severity filter (INFO, WARNING, CRITICAL).
  2. Event Stream Table: Columns for [Timestamp (YYYY-MM-DD HH:mm:ss)], [Aktor / IP], [Kategori Event], [Severity Badge], [Deskripsi Aktivitas], [Detail Payload].
  3. Expandable Row: Click to reveal full JSON payload with request headers and SQL queries.
  4. Actions: "Export CSV / JSON Log" button.

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Admin Profile & Security Settings (admin/profile.html).
- Aesthetic: Clean, disciplined administrator account center on soft pearl slate (#f8fafc), white cards (#ffffff), 1px border (#e2e8f0).
- Keyframe Layout:
  1. Admin Identity Card: Avatar with admin badge, Administrator Name, Email, Role ("Super User"), and Last Login Timestamp.
  2. Credentials Form: Change Password fields (Current Password, New Password, Confirm Password) with strength meter.
  3. Active Sessions List: Active IP addresses, browsers, and devices with "Revoke Other Sessions" button.
  4. Action: Primary button "Simpan Perubahan Akun Admin" (#1e40af, rounded 8px).

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the System Maintenance Mode Lockout Screen.
- Aesthetic: Minimalist, respectful clinical maintenance status screen on a soft pearl canvas (#f8fafc).
- Container Card: Max width 460px, pure white card (#ffffff), 1px border (#e2e8f0), rounded 16px.
- Keyframe Layout:
  1. Animated Icon: Server/Gear icon with gentle pulsing amber glow (#fffbeb background, #d97706 icon).
  2. Headline: "Sistem Sedang Dalam Pemeliharaan Berkala" (Outfit 700, 24px, #0f172a).
  3. Status Pill: "Status Database XAMPP: Sinkronisasi Skema Data".
  4. Message: Reassuring message that user scan data and history are completely safe and services will resume shortly.
  5. Estimated Uptime: Digital countdown clock / estimated completion indicator.
  6. Action: Outlined button "Cek Status Ulang" (#f1f5f9 background, #0f172a text, rounded 8px).

---

As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the 404 Not Found & System Error Recovery Screen.
- Aesthetic: Clean, reassuring error recovery interface on soft pearl slate (#f8fafc).
- Container Card: Max width 480px, pure white (#ffffff), 1px border (#e2e8f0), rounded 16px.
- Keyframe Layout:
  1. Status Code Display: Large minimalist numeral "404" (Outfit 700, 64px, color #cbd5e1 with subtle primary blue glow #2563eb).
  2. Headline: "Halaman Tidak Ditemukan" (Outfit 700, 22px, #0f172a).
  3. Description: "Halaman atau laporan scan yang Anda tuju mungkin telah dipindahkan, dihapus, atau URL yang dimasukkan salah."
  4. Recommended Navigation Pills: Quick link chips to [Beranda Utama], [Dashboard Pasien], [Mulai Scan Baru], dan [Hubungi Tim Medis].
  5. Action Buttons: Primary button "Kembali ke Dashboard" (#2563eb, rounded 8px) and Outlined button "Laporkan Kendala".
