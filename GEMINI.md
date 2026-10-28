# INTRUKSI & PANDUAN UTAMA PROJECT SKINCHECK AI

## 🚨 ATURAN PRIORITAS TERTINGGI: DATABASE XAMPP (MYSQL)
**PENTING UNTUK SEMUA AGEN / ASISTEN AI:**
1. Database project ini **WAJIB MENGGUNAKAN XAMPP MYSQL** (`skincheck_db`), **BUKAN SQLITE**.
2. Jangan pernah mengubah `DB_CONNECTION` di `.env` menjadi `sqlite`. Nilai wajibnya adalah:
   ```env
   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=skincheck_db
   DB_USERNAME=root
   DB_PASSWORD=
   ```
3. Jika user meminta perbaikan, testing, atau penambahan fitur, seluruh operasi database **harus selalu diarahkan ke XAMPP MySQL**.
4. Jika ada tabel baru atau update kolom, inisialisasi dilakukan menggunakan:
   ```powershell
   python setup_db.py
   ```
5. Tabel-tabel resmi dalam `skincheck_db`:
   - `users`
   - `otp_tokens`
   - `skin_scans`
   - `analysis_results`
   - `products`
   - `activity_logs`
   - `system_settings`

---

## 📋 ARSITEKTUR SISTEM & UML
- Diagram UML lengkap (Use Case & Activity) berada di file [uml_skincheck_lengkap.html](uml_skincheck_lengkap.html).
- Tab 1: Use Case Diagram (SmartUTBK layout & warna aktor: Biru Customer, Merah Admin, Kuning OTP, Ungu AI).
- Tab 2: Master Activity Diagram Full Poster (4 Swimlanes: Customer, OTP Service, AI Engine, Admin).
- Tab 3: Dokumentasi & Matriks Keselarasan Sistem (Traceability 21 Use Case vs Kode).
- Seluruh endpoint FastAPI terhubung 1-to-1 dengan Use Case di diagram.
