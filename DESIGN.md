---
name: SkinCheck Lumière (Bright Minimalist)
colors:
  primary: "#2563eb"
  secondary: "#0d9488"
  accent: "#8b5cf6"
  surface: "#ffffff"
  surface-ground: "#f8fafc"
  surface-variant: "#f1f5f9"
  on-surface: "#0f172a"
  on-surface-muted: "#64748b"
  outline: "#e2e8f0"
  error: "#e11d48"
  warning: "#d97706"
  success: "#059669"
  info: "#0284c7"
typography:
  headline-lg:
    fontFamily: "Outfit, sans-serif"
    fontSize: "32px"
    fontWeight: 700
    letterSpacing: "-0.03em"
  headline-md:
    fontFamily: "Outfit, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    letterSpacing: "-0.02em"
  headline-sm:
    fontFamily: "Outfit, sans-serif"
    fontSize: "18px"
    fontWeight: 600
    letterSpacing: "-0.01em"
  body-lg:
    fontFamily: "Plus Jakarta Sans, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: "1.65"
  body-md:
    fontFamily: "Plus Jakarta Sans, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: "1.6"
  body-sm:
    fontFamily: "Plus Jakarta Sans, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "1.5"
  label-md:
    fontFamily: "Plus Jakarta Sans, sans-serif"
    fontSize: "11px"
    fontWeight: 700
    letterSpacing: "0.06em"
    textTransform: "uppercase"
rounded:
  xs: "6px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  full: "9999px"
---

# Design System — SkinCheck AI

## 1. Overview
**SkinCheck Lumière** adalah panduan identitas visual dan sistem desain antarmuka resmi untuk platform **SkinCheck AI**. 

Mengusung tema **"Minimalis, Bright & Elegan"**, sistem desain ini memadukan ketegasan klinis dermatologis (*clinical precision*) dengan kemewahan modern (*refined digital wellness*). Antarmuka difokuskan pada:
- **Purity & Brightness**: Latar belakang putih bersih dan slate mutiara (*pure pearl canvas*) yang memancarkan kesan higienis, segar, dan terpercaya layaknya laboratorium dermatologi berstandar internasional.
- **Low Visual Noise**: Menghilangkan dekorasi berlebihan, bayangan gelap tebal, dan gradien norak. Struktur visual dibangun melalui kontras tipografi, garis tepi tipis (*hairline borders*), dan proporsi ruang kosong (*generous whitespace*).
- **High Information Density with Breathability**: Data metrik kulit, skor UV sunscreen, dan rekomendasi bahan aktif disajikan secara presisi, terstruktur rapi, dan mudah dicerna sekilas (*glanceable clarity*).

---

## 2. Color Palette & Token System

### 2.1 Brand & Action Colors
Warna aksi dirancang mencolok namun berwibawa, memandu fokus pengguna langsung ke alur diagnosis utama tanpa distraksi visual.

| Token | Hex | Role & Usage | Kontras WCAG |
| :--- | :--- | :--- | :--- |
| **`primary`** | `#2563eb` | Tombol CTA utama (Ambil Scan, Mulai Analisis), link aktif, progress bar aktif. Memberikan impresi teknologi medis terpercaya (*sapphire authority*). | 4.8:1 pada `#ffffff` |
| **`primary-hover`** | `#1d4ed8` | State hover & active tombol utama. | 6.2:1 pada `#ffffff` |
| **`primary-soft`** | `#eff6ff` | Background tint untuk highlight card, chip aktif, atau badge notifikasi lembut. | Digunakan bersama text `#1d4ed8` |
| **`secondary`** | `#0d9488` | Aksi sekunder, modul kesehatan kulit (*dermatological teal*), indikator kelembapan & hidrasi. | 4.6:1 pada `#ffffff` |
| **`secondary-soft`**| `#f0fdfa` | Background tint untuk rekomendasi bahan aktif alami dan tips perawatan. | Digunakan bersama text `#0f766e` |
| **`accent`** | `#8b5cf6` | Aksen AI Copilot, deep-learning insights, dan fitur automated scanner. | 4.5:1 pada `#ffffff` |
| **`accent-soft`** | `#f5f3ff` | Background tint modul kecerdasan buatan (*AI badge*). | Digunakan bersama text `#6d28d9` |

### 2.2 Surface & Neutral Canvas (Bright & Airy)
Arsitektur permukaan terang dibangun berlapis (*layered surfaces*) menggunakan perbedaan derajat luminositas netral untuk menciptakan kedalaman yang bersih tanpa mengandalkan drop-shadow kotor.

| Token | Hex | Role & Semantic Purpose |
| :--- | :--- | :--- |
| **`surface`** | `#ffffff` | Permukaan kartu (*cards*), dialog modal, input text, dropdown, dan floating bars. |
| **`surface-ground`** | `#f8fafc` | Kanvas utama halaman (*body background*). Warna abu mutiara lembut (*soft pearl*) untuk mereduksi ketegangan mata pada layar cerah. |
| **`surface-variant`**| `#f1f5f9` | Kontainer sekunder, table header, well container, card hover background. |
| **`outline`** | `#e2e8f0` | Garis batas struktural (*1px hairline border*) pada kartu, divider, dan komponen formulir. |
| **`outline-focus`** | `#93c5fd` | Ring fokus aksen saat input form aktif / keyboard accessible. |

### 2.3 Typography & Content Contrast
| Token | Hex | Role & Usage |
| :--- | :--- | :--- |
| **`on-surface`** | `#0f172a` | Teks utama, judul (*headings*), angka metrik utama, ikon dominan. Slate murni berdensitas tinggi, bebas pantulan pudar (*crisp high-contrast*). |
| **`on-surface-muted`**| `#64748b` | Teks pendukung, timestamp, placeholder form, label deskriptif sekunder. |
| **`on-surface-subtle`**| `#94a3b8` | Hint text, ikon non-interaktif, border checklist pasif. |

### 2.4 Semantic Health & Diagnostic Indicators
Warna status klinis disesuaikan dengan standar dermatologi:
- **`success`** (`#059669` / soft `#ecfdf5`): Kondisi kulit normal/sehat, proteksi sunscreen merata sempurna, status operasional sistem OK.
- **`warning`** (`#d97706` / soft `#fffbeb`): Area kulit berminyak berlebih, kelembapan rendah, perlunya re-aplikasi sunscreen, batas kuota API mendekati habis.
- **`error`** (`#e11d48` / soft `#fff1f2`): Deteksi peradangan/jerawat aktif, paparan UV tinggi tanpa proteksi, kegagalan validasi form, kegagalan koneksi SMTP/Gateway.
- **`info`** (`#0284c7` / soft `#f0f9ff`): Panduan petunjuk pemindaian kamera, tips rutin harian, informasi versi model.

---

## 3. Typography Hierarchy

Sistem tipografi menggunakan dua typeface yang saling melengkapi:
1. **`Outfit`** (Headings): Geometris, modern, tegas, dengan sentuhan premium kontemporer.
2. **`Plus Jakarta Sans`** (Body & Interface): Tipografi humanis berkejelasan tinggi, optimal untuk layar resolusi tinggi, tabel data, dan angka diagnostik.

```
Headline-LG   : Outfit 700 — 32px (line-height: 1.25, letter-spacing: -0.03em)
Headline-MD   : Outfit 600 — 24px (line-height: 1.30, letter-spacing: -0.02em)
Headline-SM   : Outfit 600 — 18px (line-height: 1.35, letter-spacing: -0.01em)
Body-LG       : Plus Jakarta Sans 400 — 17px (line-height: 1.65)
Body-MD       : Plus Jakarta Sans 400 — 15px (line-height: 1.60)
Body-SM       : Plus Jakarta Sans 400 — 13px (line-height: 1.50)
Label-MD      : Plus Jakarta Sans 700 — 11px (letter-spacing: 0.06em, UPPERCASE)
Stat-Display  : Outfit 700 — 40px (letter-spacing: -0.04em, monospaced numerals)
```

### Aturan Tipografi:
- **Uppercase Headers**: Digunakan khusus untuk label modul kecil, kategori produk, atau penanda status (contoh: `STATUS KONEKSI`, `SKIN TYPE SCORE`).
- **Heading Contrast**: Semua heading (`h1`–`h4`) wajib menggunakan warna `#0f172a` dengan ketebalan minimal `600`. Jangan gunakan warna abu-abu pudar untuk judul.
- **Data & Numeric Displays**: Angka persentase hidrasi, akurasi AI, dan skor SPF sunscreen ditampilkan tebal (*font-weight: 700*) untuk keterbacaan instan.

---

## 4. Spacing, Layout & Grid System

- **Base Unit (8pt Grid)**: Seluruh margin, padding, tinggi baris, dan ukuran ikon mengikuti kelipatan 4px atau 8px (`4px`, `8px`, `12px`, `16px`, `24px`, `32px`, `48px`, `64px`).
- **Container Bounds**:
  - Web Customer / Public: Max-width `1200px` terpusat (*centered container*).
  - Admin Dashboard & Diagnostic Hub: Max-width `1440px` fluida untuk densitas metrik operasional.
  - Scanner & Mobile Viewport: Max-width `540px` terpusat dengan rasio aspek kamera 4:3 / 1:1.
- **Whitespace Philosophy (Breathing Room)**: Card dan section diberi padding lapang (minimal `24px` di desktop, `16px` di mobile) untuk menghasilkan estetika yang tenang dan tidak padat menyesakkan.

---

## 5. Component Guidelines

### 5.1 Buttons (Tombol Interaktif)
- **Geometry**: Sudut membulat proporsional `rounded-sm: 8px` atau `rounded-md: 12px` (bergantung ukuran). Jangan campur tombol sudut lancip tajam dengan tombol bulat di satu layar.
- **Primary CTA**:
  - Background: `#2563eb`, Text: `#ffffff`
  - Hover: `#1d4ed8` dengan elevasi halus `transform: translateY(-1px)`
  - Active: `#1e40af` dengan `transform: translateY(0)`
  - Focus Ring: `box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2)`
- **Secondary / Soft Button**:
  - Background: `#f1f5f9`, Text: `#0f172a`, Border: `1px solid #e2e8f0`
  - Hover: Background `#e2e8f0`
- **Ghost / Link Button**:
  - Background: `transparent`, Text: `#2563eb`
  - Hover: Background `#eff6ff`

### 5.2 Cards & Containers
- **Elevasi Minimalis**: Kartu **TIDAK** menggunakan drop-shadow hitam pekat. Kartu mengandalkan:
  - Background: `#ffffff` (Pure White)
  - Border: `1px solid #e2e8f0` (Hairline Crisp)
  - Subtle Ambient Shadow: `0 1px 3px rgba(15, 23, 42, 0.04), 0 4px 12px rgba(15, 23, 42, 0.02)`
- **Hover State**: Border berubah menjadi `#cbd5e1`, dengan pergeseran mikro `translateY(-2px)` dan shadow halus `0 8px 24px rgba(15, 23, 42, 0.06)`.
- **Card Header**: Diberi garis pemisah lembut `border-bottom: 1px solid #f1f5f9` dan padding vertikal `16px`.

### 5.3 Form Inputs & Controls
- **Inputs & Selects**:
  - Background: `#ffffff`
  - Border: `1px solid #cbd5e1` (1px presisi)
  - Height: `44px` (touch-friendly standar)
  - Border Radius: `8px`
  - Placeholder: `#94a3b8`
- **Focus State**:
  - Border: `#2563eb`
  - Glow Ring: `box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12)`
  - Background: `#ffffff` murni

### 5.4 Badges, Tags & Chips
- Menggunakan skema **Soft-Tone (Tonal Tint)**: Background 10–12% saturasi warna terkait dengan teks saturasi tinggi agar tetap anggun dan tidak mencolok berlebihan.
  - *Skin Type Oily*: Background `#fff7ed`, Text `#c2410c`, Border `#ffedd5`
  - *Skin Type Dry*: Background `#eff6ff`, Text `#1d4ed8`, Border `#dbeafe`
  - *Skin Type Normal*: Background `#f0fdf4`, Text `#15803d`, Border `#dcfce7`
  - *AI Status Active*: Background `#f5f3ff`, Text `#6d28d9`, Border `#ede9fe`

### 5.5 Scanner & AI Camera Viewfinder
- **Frame**: Rasio aspek proporsional dengan sudut membulat `16px`.
- **Overlay Guides**: Garis pandu wajah oval halus semi-transparan (`rgba(255, 255, 255, 0.6)`) dengan sudut bidik (*corner brackets*) aksen `#2563eb`.
- **Radar / Scan Line**: Garis gradien bercahaya lembut bergerak vertikal (*subtle laser sweep*) dengan glow `#2563eb` saat AI sedang memproses analisis citra wajah.

---

## 6. Micro-Interactions & Animation Principles

- **Durasi Standar**: Transisi UI beroperasi pada **180ms – 240ms**. Hindari animasi lambat di atas 400ms yang menghambat alur kerja pengguna.
- **Timing Function**: Gunakan kurva modern `cubic-bezier(0.16, 1, 0.3, 1)` untuk menghasilkan impresi pegas responsif yang luwes (*snappy yet elegant*).
- **Interactive Feedback**:
  - Setiap klik tombol memberikan feedback visual seketika (state peredupan atau spinner mini).
  - Toast notification meluncur lembut dari pojok kanan atas dengan blur latar belakang (*backdrop-filter: blur(8px)*).

---

## 7. Accessibility & Inclusivity (WCAG 2.1 AA Compliance)

1. **Rasio Kontras Minimum**:
   - Teks bodi (`body-md`, `body-sm`) terhadap background wajib memenuhi rasio minimal **4.5:1**.
   - Judul besar (`h1`, `h2`) dan elemen antarmuka grafis (ikon, border form aktif) wajib memenuhi minimal **3:1**.
2. **Focus Indicators**: Semua elemen interaktif (`button`, `a`, `input`) wajib memiliki `focus-visible` ring kontras tinggi tanpa boleh di-`outline: none` secara permanen.
3. **Non-Color Dependence**: Setiap indikator status hasil analisis kulit tidak boleh hanya mengandalkan warna; wajib disertai ikon dan label teks penjelas (contoh: ikon centang `bi-check-circle` + badge hijau + teks "Normal").

---

## 8. Do's and Don'ts

### ✅ DO's (Yang Wajib Dilakukan)
- **DO** gunakan kanvas putih dan pearl slate cerah sebagai dasar layout agar terkesan bersih, klinis, dan elegan.
- **DO** gunakan border tipis (*1px hairline*) `#e2e8f0` sebagai pemisah visual antar kontainer, bukan bayangan gelap tebal.
- **DO** terapkan warna primer `#2563eb` secara selektif hanya untuk aksi paling esensial (1 aksi utama per viewport).
- **DO** jaga konsistensi radius sudut komponen: gunakan `8px` untuk input/button dan `12px` s.d. `16px` untuk kartu konten.
- **DO** sediakan ruang kosong (*whitespace*) yang lapang di sekitar teks analisis dan metrik kulit agar informasi mudah dicerna.

### ❌ DON'Ts (Yang Dilarang Keras)
- **DON'T** menggunakan background hitam pekat pekat / neon cyberpunk untuk modul klinis utama (SkinCheck mengutamakan estetika *bright clinical luxury*).
- **DON'T** mencampur tombol bersudut bulat lonjong (*pill*) dengan tombol bersudut lancip kotak (*0px radius*) dalam satu tampilan.
- **DON'T** menggunakan teks abu-abu terang yang sulit dibaca di atas background putih (hindari teks dengan kontras di bawah 4.5:1).
- **DON'T** menggunakan bayangan kartu hitam legam dengan opacity tinggi (`rgba(0,0,0,0.3)`); gunakan ambient shadow ber-opacity rendah (maksimal `0.06`).
- **DON'T** memenuhi layar dengan gradien multi-warna mencolok tanpa tujuan fungsional.

---

## 9. Implementation Reference (CSS Custom Properties)

Potongan token CSS berikut merupakan implementasi langsung dari desain sistem ini pada file [app/static/css/style.css](file:///c:/Users/roboy/Documents/Tugas%20word/TUGAS%20CODINGAN/RekayasaPerangktLunak/Project_SkinChek/app/static/css/style.css):

```css
:root {
  /* Brand Tokens */
  --primary: #2563eb;
  --primary-hover: #1d4ed8;
  --primary-soft: #eff6ff;
  --secondary: #0d9488;
  --secondary-hover: #0f766e;
  --secondary-soft: #f0fdfa;
  --accent: #8b5cf6;
  --accent-soft: #f5f3ff;

  /* Surface & Canvas (Bright Minimalist) */
  --surface: #ffffff;
  --surface-ground: #f8fafc;
  --surface-variant: #f1f5f9;
  --outline: #e2e8f0;
  --outline-subtle: #f8fafc;
  --outline-focus: #93c5fd;

  /* Typography Colors */
  --on-surface: #0f172a;
  --on-surface-muted: #64748b;
  --on-surface-subtle: #94a3b8;

  /* Diagnostics & Semantic Status */
  --success: #059669;
  --success-soft: #ecfdf5;
  --warning: #d97706;
  --warning-soft: #fffbeb;
  --error: #e11d48;
  --error-soft: #fff1f2;
  --info: #0284c7;
  --info-soft: #f0f9ff;

  /* Typography Families */
  --font-heading: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

  /* Border Radii */
  --radius-xs: 6px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;

  /* Crisp Ambient Lighting (Low Noise Shadows) */
  --shadow-ambient: 0 1px 3px rgba(15, 23, 42, 0.04), 0 4px 12px rgba(15, 23, 42, 0.02);
  --shadow-elevated: 0 8px 24px rgba(15, 23, 42, 0.06), 0 2px 6px rgba(15, 23, 42, 0.02);
  --shadow-primary-glow: 0 4px 16px rgba(37, 99, 235, 0.18);

  /* Transitions */
  --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
  --transition: all 0.2s var(--ease-spring);
}
```
