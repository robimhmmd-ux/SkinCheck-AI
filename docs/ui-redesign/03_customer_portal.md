# 🧴 Keyframe Prompts 03 — Customer Portal

Dokumen ini memuat prompt perancangan keyframe UI/UX untuk seluruh modul Customer Portal di platform **SkinCheck AI**:
1. **Health Hub Dashboard** ([app/views/pages/customer/dashboard.html](../../app/views/pages/customer/dashboard.html))
2. **Real-time Face Scanner & Sunscreen Checker** ([app/views/pages/customer/scan_face.html](../../app/views/pages/customer/scan_face.html))
3. **Clinical Diagnostic Report & Routine Recommendations** ([app/views/pages/customer/scan_detail.html](../../app/views/pages/customer/scan_detail.html))
4. **Skin Progression Timeline & History Gallery** ([app/views/pages/customer/history.html](../../app/views/pages/customer/history.html))
5. **AI Skincare Assistant Copilot** ([app/views/pages/customer/assistant.html](../../app/views/pages/customer/assistant.html))
6. **Customer Skin Profile & Preferences** ([app/views/pages/customer/profile.html](../../app/views/pages/customer/profile.html))

---

## 📋 Prompt 03.1: Customer Health Hub Dashboard (customer/dashboard.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Health Hub Dashboard (customer/dashboard.html).

Visual Identity & Aesthetic:
- Bright, clinical-elegance wellness dashboard providing a holistic view of the patient's skin journey.
- Soft pearl canvas (#f8fafc), pure white cards (#ffffff), hairline borders (#e2e8f0), generous whitespace.
- Accent colors: Sapphire (#2563eb) for scan actions, Derm Teal (#0d9488) for hydration metrics, Amber (#d97706) for UV reminders.

Dashboard Layout & Sections:
1. Personalized Welcome Header:
   - User greeting: "Halo, [Nama Pengguna] 👋" (Outfit 700, 28px, #0f172a).
   - Subtitle: "Berikut adalah ringkasan kesehatan kulit dan rekomendasi harian Anda."
   - Quick Action CTA: Primary Button "Mulai Scan Wajah Baru" with camera icon (#2563eb, rounded-sm: 8px).
2. Key Metric Cards (Row of 3 Cards):
   - Card 1 (Kondisi Kulit Terkini): Skin type badge (e.g. "Kombinasi Cenderung Berminyak"), overall health score dial (86/100) with soft green progress circle.
   - Card 2 (Proteksi Sunscreen Terakhir): Coverage gauge (92% Merata Sempurna), status badge "Proteksi Aktif", reminder badge "Re-aplikasi dalam 2 jam".
   - Card 3 (Total Riwayat Pemindaian): Stat counter (12 Sesi Scan), tanggal scan terakhir, trend indikator "+4% Peningkatan Hidrasi".
3. Daily Skincare Routine Tracker:
   - Two tabbed checklist cards: Rutinitas Pagi (Morning Cleanse, Vitamin C, Moisturizer, Sunscreen SPF 50) and Rutinitas Malam (Double Cleanse, Retinol/Niacinamide, Night Cream).
   - Interactive checkboxes with smooth strike-through animation.
4. Recommended Skincare Carousel:
   - 3 product cards matching the user's diagnosed skin type: Product thumbnail, brand name, product title, key active ingredients tags (#f1f5f9 chips: Niacinamide 5%, Ceramide NP), and detail button.
5. Recent Scan Snapshot:
   - Split card showing the latest face thumbnail with annotated facial zones (T-Zone, U-Zone) and quick link "Lihat Laporan Lengkap".
```

---

## 📋 Prompt 03.2: Real-time Face Scanner & Sunscreen Checker (customer/scan_face.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Real-time Face Scanner & Sunscreen Checker (customer/scan_face.html).

Visual Identity & Aesthetic:
- Pristine, medical-grade camera interface with high usability, zero clutter, and clear visual framing guidance.
- Darkened clinical viewport framed within a bright pearl canvas container, surrounded by crisp white diagnostic controls.
- Primary Blue (#2563eb) for camera triggers, Medical Teal (#0d9488) for alignment prompts, Emerald (#059669) for good lighting indicator.

Scanner UI Structure:
1. Mode Switcher (Pill Tabs):
   - Segmented control toggle at top center: [Mode 1: Analisis Kondisi Kulit (Jerawat, Minyak, Pori)] vs [Mode 2: Deteksi Pemerataan Sunscreen (UV Coverage)].
2. Camera Viewport Container (Aspect Ratio 4:3 or 1:1, Max width: 560px, border-radius 16px):
   - Live video stream with smooth rounded corners.
   - Medical AR Face Guide: Semi-transparent white oval guide with dashed outline and corner alignment brackets that turn emerald green (#059669) when face is properly positioned.
   - Real-time Lighting & Distance Meter: Small floating badge at top right: "Pencahayaan: Optimal (Lux OK)" with green dot indicator.
   - Scanning Sweep Effect (when triggered): Soft glowing vertical laser line (#2563eb) sweeping downwards.
3. Diagnostic Instructions:
   - Floating guide pill at bottom of viewport: "Posisikan wajah Anda tepat di dalam bingkai oval dan pastikan cahaya merata."
4. Shutter Controls:
   - Center Shutter Button: Outer ring (72px) with white border, inner circle (56px) in primary sapphire blue (#2563eb) with camera icon bi-camera-fill.
   - Hover state: Gentle pulsing glow.
   - Camera Switcher Button (Front/Back) and Flash/Lighting Toggle on the sides.
   - Fallback Option below: "Atau Unggah Foto dari Galeri" with drag & drop dashed container.
```

---

## 📋 Prompt 03.3: Clinical Diagnostic Report & Routine Recommendations (customer/scan_detail.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Clinical Diagnostic Report & Routine Recommendations Screen (customer/scan_detail.html).

Visual Identity & Aesthetic:
- High-authority, elegant clinical laboratory report layout.
- Soft pearl canvas (#f8fafc), white cards (#ffffff), hairline borders (#e2e8f0), high-contrast slate text (#0f172a).
- Semantic accents: Emerald for optimal areas, Amber for moderate sebum, Crimson for acne/redness hotspots.

Report Layout & Visual Hierarchy:
1. Report Header Banner:
   - Patient ID and Scan Timestamp: "ID Scan: #SC-98214 • 02 Oktober 2026, 10:45 WIB".
   - Overall Skin Condition Badge: "Tipe Kulit: Kombinasi (Berminyak di T-Zone, Kering di Pipi)" (Soft blue pill #eff6ff).
   - Sunscreen Protection Score: Large circular gauge (94% Perlindungan UV Maksimal).
   - Export & Share: Button "Download PDF Medis" (bi-file-earmark-pdf) and "Bagikan Laporan".
2. Split Diagnostic Visualization:
   - Left Column (Visual Inspection): High-resolution captured face with toggleable heatmaps: [Foto Asli] | [Heatmap Sunscreen UV] | [Peta Kondisi Pori & Sebum].
   - Right Column (5 Parameter Radar / Bar Metrics):
     - Hidrasi & Kelembapan: 78% (Normal/Lembap) [Bar Hijau]
     - Minyak & Sebum: 84% (Tinggi di Dahi & Hidung) [Bar Oranye]
     - Pori-pori Wajah: 62% (Sedang) [Bar Biru]
     - Kemerahan / Inflamasi: 18% (Rendah / Sehat) [Bar Hijau]
     - Pemerataan Sunscreen: 94% (Merata Sempurna) [Bar Teal]
3. AI Clinical Summary & Deep Analysis:
   - Card with AI badge (Amethyst #8b5cf6): Detailed diagnostic explanation generated by Gemini AI regarding UV protection gap in neck/jaw area and sebum control advice.
4. Curated Ingredients Matrix:
   - Two-column card:
     - "Bahan Aktif yang Direkomendasikan": Pills with Niacinamide 4%, Hyaluronic Acid, Centella Asiatica (#f0fdf4 green tint).
     - "Bahan yang Perlu Dihindari": Pills with Alcohol Denat, Fragrance Berlebih, Minyak Mineral Komedogenik (#fff1f2 red tint).
5. Personalized Matched Products:
   - Curated list of 4 approved skincare products with compatibility scores ("98% Match"), price, and purchase link.
```

---

## 📋 Prompt 03.4: Skin Progression Timeline & History Gallery (customer/history.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Skin Progression Timeline & History Gallery (customer/history.html).

Visual Identity & Aesthetic:
- Clean, inspiring progression diary demonstrating skin health improvements over time.
- Bright pearl canvas (#f8fafc), pure white cards (#ffffff), hairline borders (#e2e8f0).
- Interactive before/after comparison tool with elegant dual-slider control.

Layout & Component Breakdown:
1. Timeline Header & Filters:
   - Title: "Riwayat & Perkembangan Kulit" (Outfit 700, 28px).
   - Filter Controls: Date Range picker, Skin Metric filter (Semua, Sunscreen Coverage, Tingkat Minyak, Hidrasi), dan mode tampilan (Grid Galeri vs Garis Waktu).
2. Before-After Comparison Slider Card:
   - Split image viewer with central draggable pill slider:
     - Left: "Scan Pertama (01 Jan 2026)" vs Right: "Scan Terkini (02 Okt 2026)".
     - Delta metric badge: "+26% Peningkatan Hidrasi", "-35% Reduksi Jerawat".
3. Chronological Scan Grid:
   - Cards arranged in responsive 3-column grid:
     - Card Thumbnail: Face preview with date overlay badge.
     - Skin Type Pill: e.g. "Oily", "Combination", "Normal".
     - Mini Metrics Row: Sebum, Moisture, UV Coverage with progress bars.
     - Action link: "Detail Analisis →".
4. Empty State (if no history):
   - Illustration of a clean mirror with scan line, title "Belum Ada Riwayat Scan", button "Ambil Scan Pertama Anda".
```

---

## 📋 Prompt 03.5: AI Skincare Assistant Copilot (customer/assistant.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer AI Skincare Assistant Copilot (customer/assistant.html).

Visual Identity & Aesthetic:
- Modern conversational AI interface inspired by refined medical consultations.
- Canvas background: Soft pearl slate (#f8fafc), Chat Container: Pure white card (#ffffff) with hairline border (#e2e8f0), border-radius 16px.
- Distinct message bubbles: AI Assistant (Pure white with 1px border #e2e8f0 and Amethyst AI badge #8b5cf6), User (Primary Blue fill #2563eb with white text).

Chat Interface Architecture:
1. Header Bar:
   - AI Persona Avatar: 40px circle with gradient background and glowing icon bi-stars.
   - Persona Title: "SkinCheck AI Copilot" with status badge "Online • Didukung Google Gemini 1.5".
   - Context Pill: "Konteks Aktif: Laporan Scan Terakhir (#SC-98214)".
   - Action: Button "Mulai Konsultasi Baru" (bi-arrow-clockwise).
2. Conversation Stream:
   - Bot Message Card:
     - Greeting message with personalized observation based on user's recent scan.
     - Embedded Interactive Product Cards: Compact skincare card within message showing product image, active ingredients, and 'Mengapa Cocok untuk Kulitmu'.
   - Quick Prompt Pills (horizontal scrolling tags):
     - "Bagaimana cara mengatasi kemerahan di pipi?"
     - "Kapan waktu terbaik re-aplikasi sunscreen?"
     - "Apakah niacinamide aman digabung vitamin C?"
3. Message Input Deck (Sticky Bottom):
   - Rounded container (height: 52px, border: 1px solid #cbd5e1, background: #ffffff, border-radius: 26px).
   - Left action: Attach scan/photo button (bi-paperclip).
   - Text input: "Tanyakan apa saja seputar perawatan kulit dan produk..."
   - Right send button: Circular button (40px) in primary blue (#2563eb) with send icon bi-send-fill.
```

---

## 📋 Prompt 03.6: Customer Skin Profile & Preferences (customer/profile.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Skin Profile & Preferences Page (customer/profile.html).

Visual Identity & Aesthetic:
- Calm, organized settings and clinical preferences center.
- Pure white cards (#ffffff), 1px hairline border (#e2e8f0), soft pearl canvas (#f8fafc).
- Primary Blue (#2563eb), Medical Teal (#0d9488), Muted Slate (#64748b).

Layout & Form Sections:
1. Profile Header Card:
   - Avatar circle (80px) with initial or photo upload button.
   - User Name (Outfit 700, 22px), Email, and Phone number.
   - Verification Badges: "Email Terverifikasi ✓", "WhatsApp Terverifikasi ✓".
2. Dermatological Baseline Card:
   - Rentang Usia: Dropdown (Remaja, 20-29, 30-39, 40+).
   - Tipe Kulit Utama Menurut Pengguna: Radio pill selectors (Kering, Berminyak, Kombinasi, Sensitif, Normal).
   - Riwayat Alergi Bahan Kosmetik: Tag input (e.g. Paraben, SLS, Fragrance, Alkohol).
   - Masalah Kulit Prioritas: Multi-select chips (Jerawat, Flek Hitam, Pori Besar, Garis Halus).
3. Notification & Routine Reminders Card:
   - Toggle switch: "Pengingat Re-aplikasi Sunscreen (Setiap 2 Jam)".
   - Toggle switch: "Pengingat Rutinitas Perawatan Malam (Pukul 21:00)".
   - Toggle switch: "Laporan Mingguan Perkembangan Kulit via Email".
4. Security & Credentials:
   - Ganti Kata Sandi form fields.
   - Tombol Simpan Perubahan: Primary button (#2563eb, rounded-sm: 8px).
```
