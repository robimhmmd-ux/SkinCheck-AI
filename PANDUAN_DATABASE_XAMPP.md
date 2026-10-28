# 🐘 PANDUAN LENGKAP & PENGINGAT DATABASE XAMPP (MYSQL)

Dokumen ini adalah **panduan resmi dan pengingat permanen** bahwa project **SkinCheck AI** menggunakan database **MySQL melalui XAMPP**.

---

## 📌 PENGINGAT UNTUK CHAT BARU DENGAN AI
> **Jika suatu saat Anda membuka sesi chat baru dengan asisten AI, Anda cukup mengetik:**
> 
> *"Baca file GEMINI.md dan PANDUAN_DATABASE_XAMPP.md. Ingat, project ini WAJIB menggunakan XAMPP MySQL!"*
> 
> Asisten AI akan otomatis membaca aturan di file `GEMINI.md` dan `.agents/rules/DATABASE_RULES.md` sehingga **tidak akan pernah menggantinya kembali ke SQLite**.

---

## ⚙️ 1. Konfigurasi Aktif di File `.env`
Project ini sudah disetel dan aktif terhubung ke XAMPP MySQL dengan parameter berikut:
```env
# Database Configuration (XAMPP MySQL — WAJIB UTAMA)
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=skincheck_db
DB_USERNAME=root
DB_PASSWORD=
```

---

## 🚀 2. Cara Menjalankan & Memastikan XAMPP Siap

### Langkah 1: Buka XAMPP Control Panel
1. Buka aplikasi **XAMPP Control Panel** di Windows Anda.
2. Klik tombol **Start** pada modul:
   - **Apache** (hingga indikator berwarna hijau)
   - **MySQL** (hingga indikator berwarna hijau, port 3306)

### Langkah 2: Buka phpMyAdmin di Browser
1. Buka browser dan ketik alamat:
   ```
   http://localhost/phpmyadmin
   ```
2. Pada panel sebelah kiri, Anda akan melihat database bernama:
   **`skincheck_db`**
3. Di dalam database tersebut, terdapat 7 tabel utama project:
   - 👤 `users` — Data akun Customer dan Super Admin.
   - 🔑 `otp_tokens` — Kode verifikasi OTP registrasi (Email & WhatsApp).
   - 📸 `skin_scans` — Riwayat unggahan foto pemindaian wajah.
   - 🔬 `analysis_results` — Hasil diagnosis AI (jerawat, flek, kerutan, kulit kering, minyak).
   - 💄 `products` — Katalog skincare/kosmetik rekomendasi + direct link Shopee.
   - 📋 `activity_logs` — Rekam log aktivitas pengguna.
   - ⚙️ `system_settings` — Kunci konfigurasi sistem (Gemini API, SMTP, WA Gateway).

---

## 🛠️ 3. Perintah Bantuan (Scripts)

### Inisialisasi / Buat Ulang Tabel Baru:
Jika ada perubahan model atau ingin memastikan seluruh tabel terbentuk rapi, jalankan:
```powershell
python setup_db.py
```

### Migrasi / Backup Data dari SQLite ke MySQL:
Jika di masa depan ada data lokal di file `skincheck_db.sqlite` yang ingin dipindahkan ke XAMPP MySQL, cukup jalankan:
```powershell
python migrate_sqlite_to_mysql.py
```

### Menjalankan Server Aplikasi:
```powershell
python run.py
```
Aplikasi dapat diakses di browser pada: `http://127.0.0.1:8000`.

---

## 🔐 Akun Default untuk Login (Sudah Tersedia di Database MySQL):

| Role | Email | Password |
| :--- | :--- | :--- |
| **Super Admin** | `admin@skincheck.internal` | `adminsecurepassword` |
| **Demo Customer** | `user@skincheck.internal` | `user123456` |
| **Halaman Login Admin** | `http://127.0.0.1:8000/admin/login` | |
| **Halaman Login Customer** | `http://127.0.0.1:8000/login` | |

---

## 💡 Troubleshooting / Masalah Umum XAMPP
1. **Port 3306 bentrok / MySQL tidak mau Start:**
   - Buka Task Manager, pastikan tidak ada instance `mysqld.exe` lain yang sedang menggantung di latar belakang.
   - Buka XAMPP Control Panel sebagai Administrator (*Run as administrator*).
2. **Error Table doesn't exist:**
   - Jalankan `python setup_db.py` di terminal project untuk otomatis men-generate struktur tabel yang hilang.
