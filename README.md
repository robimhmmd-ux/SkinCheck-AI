# SkinCheck — AI-Powered Skin Health Monitoring & Skincare Assistant

Sistem berbasis web cerdas untuk memantau perubahan kondisi kulit wajah secara objektif, memeriksa pemerataan aplikasi sunscreen (Sunscreen Evenness Check) dengan visual Heatmap, serta panduan edukasi skincare non-medis.

---

## 🏗️ Pola Arsitektur: MVC (Model - View - Controller)

Aplikasi dibangun menggunakan pola MVC murni yang memisahkan tanggung jawab secara tegas:
- **Models (`app/models/`)**: Menangani skema data entitas (User, Product, SkinScan, AnalysisResult, SunscreenResult).
- **Views (`app/views/`)**: Antarmuka HTML5, CSS3, Bootstrap 5.3 responsif (Desktop, Tablet, Mobile) dengan layout modular (`layouts/base.html`, `navbar.html`, `footer.html`).
- **Controllers (`app/controllers/`)**: Business logic, penanganan request routing, dan persiapan data sebelum dirender ke View.
- **Routes (`app/routes/`)**: Pemetaan endpoint URL ke Controller yang sesuai.
- **Static (`app/static/`)**: File CSS kustom (Glassmorphism & modern design system) dan script JavaScript client-side.

---

## 📁 Struktur Folder Project

```text
Project SkinChek/
├── .env                  # Konfigurasi environment lokal (tidak di-commit ke public repo)
├── .env.example          # Template konfigurasi environment
├── requirements.txt      # Daftar dependensi Python
├── run.py                # File entrypoint untuk menjalankan server
└── app/
    ├── __init__.py
    ├── main.py           # Application factory & registrasi routing
    ├── config/           # Modul konfigurasi sistem
    │   ├── __init__.py
    │   └── settings.py
    ├── models/           # Definisi entitas data (Pydantic / DB Entities)
    │   ├── __init__.py
    │   ├── user.py
    │   ├── product.py
    │   ├── skin_scan.py
    │   ├── analysis_result.py
    │   └── sunscreen_result.py
    ├── controllers/      # Logika aplikasi (MVC Controller)
    │   ├── __init__.py
    │   ├── home_controller.py
    │   ├── auth_controller.py
    │   ├── customer_controller.py
    │   └── admin_controller.py
    ├── routes/           # Routing web & API
    │   ├── __init__.py
    │   ├── home_routes.py
    │   ├── auth_routes.py
    │   ├── customer_routes.py
    │   ├── admin_routes.py
    │   └── api_routes.py
    ├── views/            # Template tampilan antarmuka (Jinja2 / HTML5)
    │   ├── layouts/
    │   │   ├── base.html
    │   │   ├── navbar.html
    │   │   └── footer.html
    │   └── pages/
    │       ├── home.html               # Landing page utama
    │       ├── auth/
    │       │   ├── login.html          # Login Customer
    │       │   └── register.html       # Registrasi Customer
    │       ├── customer/
    │       │   └── dashboard.html      # Dashboard Customer placeholder
    │       └── admin/
    │           ├── login.html          # Login Admin Web
    │           └── dashboard.html      # Dashboard Admin Console placeholder
    └── static/           # Asset statis
        ├── css/
        │   └── style.css
        └── js/
            └── main.js
```

---

## ⚠️ Sebelum Menjalankan (penting)

- **Model AI tidak ada di repo ini.** File `facial-condition-model/finetuned_best.h5` (174 MB) sengaja diabaikan GitHub karena melebihi batas 100 MB. Letakkan file model itu di `facial-condition-model/finetuned_best.h5` sebelum memakai fitur scan.
- **Database:** project ini memakai MySQL. Untuk MySQL lokal pakai XAMPP/MySQL biasa; untuk database cloud gratis pakai TiDB Cloud — panduannya ada di `TIDB_SETUP.md` (termasuk `DB_SSL=true`).
- **Jangan commit file `.env`.** Salin `.env.example` menjadi `.env` di komputermu sendiri dan isi kredensial di sana.
- Setelah `.env` benar, jalankan dulu `python setup_db.py` untuk membuat tabel, baru `python run.py`.

## 🚀 Cara Menjalankan Project

### 1. Prasyarat
- Python 3.10+ terinstal pada komputer Anda.

### 2. Instalasi Dependensi
Jalankan perintah berikut di terminal:
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Web Server
Jalankan file `run.py`:
```bash
python run.py
```

Setelah server berjalan, buka browser dan akses tautan berikut:
- **Landing Page (Beranda):** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Login Customer:** [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login)
- **Register Customer:** [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register)
- **Customer Dashboard:** [http://127.0.0.1:8000/dashboard](http://127.0.0.1:8000/dashboard)
- **Portal Login Admin:** [http://127.0.0.1:8000/admin/login](http://127.0.0.1:8000/admin/login)
- **Admin Dashboard:** [http://127.0.0.1:8000/admin/dashboard](http://127.0.0.1:8000/admin/dashboard)
- **API Health Check:** [http://127.0.0.1:8000/api/v1/health](http://127.0.0.1:8000/api/v1/health)

---

## 🛡️ Prinsip Batasan Medis (Non-Negotiable)
SkinCheck dan seluruh fiturnya **BUKAN alat diagnosis medis** atau pengganti dokter spesialis kulit. Seluruh hasil bersifat indikasi visual objektif untuk keperluan pemantauan rutin mandiri pengguna.
