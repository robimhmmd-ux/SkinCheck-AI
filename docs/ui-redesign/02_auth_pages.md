# 🔐 Keyframe Prompts 02 — Authentication Pages

Dokumen ini memuat prompt perancangan keyframe UI/UX untuk seluruh alur autentikasi pelanggan:
1. **Customer Login** ([app/views/pages/auth/login.html](../../app/views/pages/auth/login.html))
2. **Customer Registration** ([app/views/pages/auth/register.html](../../app/views/pages/auth/register.html))
3. **Dual OTP Verification** ([app/views/pages/auth/verify_otp.html](../../app/views/pages/auth/verify_otp.html))

Seluruh prompt mengacu pada standar [DESIGN.md](../../DESIGN.md).

---

## 📋 Prompt 02.1: Customer Login (auth/login.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Login Page (auth/login.html).

Visual Identity & Aesthetic:
- Clean, focused bright minimalist authentication card on a soft pearl slate canvas (#f8fafc).
- Zero cluttered illustrations; focus on pristine typography, clear input affordance, and high-trust medical branding.
- Card container: Pure white (#ffffff), 1px hairline border (#e2e8f0), border-radius 16px, ambient elevation.

Layout & Component Breakdown:
1. Centered Auth Card (Max width: 440px):
   - Top clinic badge: Modern circular badge (48px) with gradient icon bi-person-check (#2563eb on soft blue tint #eff6ff).
   - Header: Headline (Outfit 600, 26px, #0f172a) "Selamat Datang Kembali", subtitle (Plus Jakarta Sans, 14px, #64748b) "Masuk ke akun SkinCheck untuk memantau perkembangan kesehatan kulit Anda."
2. Form Input Fields:
   - Email Input: Form group with label (Outfit/Plus Jakarta Sans 600, 13px, #0f172a), input container with 1px border (#cbd5e1), border-radius 8px, left icon bi-envelope (#94a3b8), placeholder "nama@email.com".
   - Focus State: Border color shifts to #2563eb with a soft glow ring (box-shadow: 0 0 0 3px rgba(37,99,235,0.12)).
   - Password Input: Label with 'Lupa Kata Sandi?' link in primary blue (#2563eb), right toggle button with icon bi-eye/bi-eye-slash.
   - Remember Me Checkbox: Custom rounded checkbox (18px) with accent blue fill on checked state.
3. Call-to-Action:
   - Primary Submit Button: Full-width button (height: 46px, background: #2563eb, text: #ffffff, font-weight: 600, rounded-sm: 8px) "Masuk ke Akun".
   - Hover state: Deep blue (#1d4ed8) with subtle translateY(-1px).
4. Secondary Navigation:
   - Hairline divider with pill text "Belum memiliki akun?".
   - Outlined secondary button: "Daftar Akun Baru Sekarang" (#f1f5f9 background, #0f172a text, 1px border #e2e8f0).
5. Footer Trust Statement:
   - Lock icon bi-shield-lock-fill with muted text (12px, #94a3b8) "Sesi terenkripsi & data riwayat kulit tersimpan aman di server lokal."
```

---

## 📋 Prompt 02.2: Customer Registration (auth/register.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Customer Registration Page (auth/register.html).

Visual Identity & Aesthetic:
- Airy, bright, and reassuring onboarding experience for new skincare patients.
- Canvas background: Soft pearl slate (#f8fafc), Card: Pure white (#ffffff) with 1px hairline border (#e2e8f0), border-radius 16px.
- Primary Blue (#2563eb), Medical Teal (#0d9488), Muted Slate (#64748b).

Layout & Form Structure:
1. Centered Card Container (Max width: 480px):
   - Brand Emblem: 48px circle with bi-person-plus-fill in soft teal tint (#f0fdfa, text: #0d9488).
   - Title: "Buat Akun SkinCheck Baru" (Outfit 700, 26px, #0f172a).
   - Subtitle: "Mulai perjalanan pemantauan kesehatan kulit dan evaluasi tabir surya Anda."
2. Form Input Grid:
   - Nama Lengkap: Input text with bi-person icon, placeholder "Nama lengkap sesuai identitas".
   - Email Aktif: Input email with bi-envelope icon, helper hint "Akan digunakan untuk pengiriman kode OTP verifikasi".
   - Nomor WhatsApp: Input tel with bi-whatsapp icon (green tint #25d366), country code prefix badge "+62", placeholder "812-xxxx-xxxx".
   - Kata Sandi: Password input with eye toggle and real-time 4-bar strength indicator (Lemah, Sedang, Kuat, Sangat Aman) using color transitions (#e11d48 -> #d97706 -> #059669).
   - Konfirmasi Kata Sandi: Matching validator with instant green checkmark bi-check-circle-fill.
3. Consent & Privacy Checkbox:
   - Checkbox with label text: "Saya menyetujui Ketentuan Layanan & Kebijakan Privasi Data Medis SkinCheck."
4. Registration Action:
   - Primary Button: "Lanjutkan ke Verifikasi OTP" with right arrow icon bi-arrow-right (#2563eb, height: 48px, rounded: 8px).
5. Switch to Login:
   - Bottom note: "Sudah punya akun? Masuk di sini" with blue anchor link.
```

---

## 📋 Prompt 02.3: Dual OTP Verification (auth/verify_otp.html)

```text
As an Expert UI/UX designer, create a keyframe based on DESIGN.md for the Dual OTP Verification Screen (auth/verify_otp.html).

Visual Identity & Aesthetic:
- High-trust, security-focused verification gateway with clear feedback for Email & WhatsApp channels.
- Pure white card (#ffffff), 1px border (#e2e8f0), soft pearl canvas (#f8fafc).
- Distinct channel badges: Email (Soft Blue #eff6ff, text #1d4ed8) and WhatsApp (Soft Green #ecfdf5, text #059669).

Layout & Interactive Components:
1. Centered Verification Card (Max width: 500px):
   - Security Shield Icon: 56px circle with animated pulsing ring and icon bi-shield-check (#2563eb).
   - Headline: "Verifikasi Keamanan Akun" (Outfit 700, 24px, #0f172a).
   - Subtitle: "Masukkan 6 digit kode verifikasi yang telah dikirimkan ke kontak Anda."
2. Dual Channel Status Banners:
   - Channel 1 (Email OTP): Box with email icon, masked email address "u***@domain.com", status badge "Terkirim".
   - Channel 2 (WhatsApp OTP): Box with WhatsApp icon, masked phone "+62 812-****-890", status badge "Terkirim".
3. 6-Box Pin Input Field:
   - Six individual square input boxes (width: 52px, height: 58px, border: 1.5px solid #cbd5e1, border-radius: 10px, text-align: center, font-size: 24px, font-family: Outfit bold).
   - Active Box: Border color #2563eb, background #eff6ff, soft shadow.
   - Filled Box: Deep slate numeral with instant automatic cursor advancement to the next box.
4. Timer & Resend Controls:
   - Countdown timer with circular progress or stopwatch icon: "Kirim ulang kode dalam 01:45".
   - Disabled/Active state for "Kirim Ulang Kode OTP via Email / WhatsApp".
5. Action Buttons:
   - Primary Button: "Verifikasi & Masuk ke Dashboard" (#2563eb, full-width, height: 46px).
   - Secondary Link: "Ganti Email atau Nomor WhatsApp" (#64748b).
```
