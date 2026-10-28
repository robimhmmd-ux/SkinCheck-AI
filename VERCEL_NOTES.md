# SkinCheck di Vercel — apa yang cocok, apa yang tidak

## Versi dependensi (penting, sudah diperbaiki)
- Root `requirements.txt` kini mem-pin `fastapi==0.115.0`,
  `starlette==0.38.6`, `jinja2==3.1.4`. Tanpa pin ini, install terbaru
  membuat semua halaman HTML 500 (TemplateResponse gaya lama tidak
  didukung Starlette terbaru) — sudah dibuktikan dengan tes lokal
  (`/` 200, `/login` 200, `/api/v1/health` 200 dengan versi pin ini).
- `api/requirements.txt` adalah daftar khusus Vercel Function: sama
  seperti di atas, TANPA tensorflow/opencv/google-generativeai (ketiganya
  diimpor secara lazy di kode, jadi aplikasi tetap bisa diimpor tanpa
  mereka). Konsekuensinya di Vercel: analisis scan AI tidak jalan
  sampai inferensi dipindah ke layanan eksternal.

## Yang cocok
- FastAPI sebagai serverless function via `api/index.py` (Vercel mendeteksi
  FastAPI dan mengekspor `app` sebagai ASGI app).
- Database TiDB Cloud (MySQL, TLS) — tidak ada server database lokal di
  Vercel, jadi database harus di cloud. Lihat `TIDB_SETUP.md`.
- Template Jinja2 + file statis di `app/` — disertakan lewat
  `includeFiles: app/**` di `vercel.json`.

## Yang TIDAK cocok tanpa penyesuaian (baca sebelum deploy)
1. **TensorFlow + model 174 MB.** Vercel Functions punya batas ukuran
   bundle (terbaru: 500 MB unzipped untuk Python) dan filesystem
   read-only kecuali `/tmp`. TensorFlow saja sudah ratusan MB, ditambah
   model 174 MB yang TIDAK ADA di repo (diabaikan `.gitignore` karena
   batas 100 MB GitHub). Deploy mentah kemungkinan gagal karena ukuran
   atau cold-start loading model sangat lambat.
   - Opsi A (paling aman untuk demo): host backend di host server
     long-running (Railway/Render/Fly/HuggingFace Spaces) dengan Docker,
     Vercel dipakai hanya kalau dosen memang minta link Vercel.
   - Opsi B (Vercel saja, dengan kompromi): pisahkan inferensi model ke
     layanan eksternal, atau unduh model ke `/tmp` saat cold start —
     ini refactor, bukan sekadar tambah `vercel.json`.
2. **Upload scan lokal.** `storage/scans` di serverless akan hilang
   antar-invocation dan filesystem repo read-only. Patch di repo-clone
   ini mengarahkan penyimpanan ke `/tmp` saat `VERCEL=1`, jadi upload
   hanya bertahan selama instance itu hidup. Untuk permanen, butuh
   Vercel Blob / S3.
3. **`setup_db.py` tidak jalan otomatis di Vercel.** Buat tabel dulu
   dengan menjalankan `setup_db.py` secara lokal mengarah ke TiDB yang
   sama, baru deploy.
4. **Dockerfile di `facial-condition-model/` bukan untuk Vercel.**
   Vercel tidak menjalankan container Docker, dan CMD-nya (`app:app`)
   juga salah (seharusnya `app.main:app`). File itu hanya relevan
   untuk host Docker (opsi A).

## Env var yang wajib di Vercel (di dashboard Vercel, BUKAN di repo)
DB_CONNECTION=mysql, DB_HOST, DB_PORT=4000, DB_DATABASE, DB_USERNAME,
DB_PASSWORD, DB_SSL=true, SECRET_KEY, GEMINI_API_KEY (kalau pakai asisten).
Jangan commit `.env` — `.env` sudah diabaikan `.gitignore`.
