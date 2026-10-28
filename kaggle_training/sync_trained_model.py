"""
SkinCheck - Kaggle Model Sync Utility
Script untuk memantau status training dan mengunduh model YOLOv8 dari Kaggle
langsung ke folder aplikasi SkinCheck (app/static/models).
"""

import subprocess
import sys
import os
import shutil
import zipfile
from pathlib import Path

# Hindari error encoding cp1252 di Windows terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

KERNEL_SLUG = "robimuhammadw/skincheck-yolov8-acne-detection-training"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_MODELS_DIR = PROJECT_ROOT / "app" / "static" / "models"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def check_status():
    print("=" * 60)
    print("[INFO] MEMERIKSA STATUS TRAINING YOLOV8 DI KAGGLE...")
    print("=" * 60)
    stdout, stderr, code = run_cmd(f"kaggle kernels status {KERNEL_SLUG}")
    print(stdout)
    if "RUNNING" in stdout:
        print("\n[PROSES] Model sedang dalam proses training di GPU Kaggle!")
        print(f"👉 Paduka Raja dapat memantau log secara live di:")
        print(f"   https://www.kaggle.com/code/{KERNEL_SLUG}")
        return "RUNNING"
    elif "COMPLETE" in stdout:
        print("\n[SELESAI] Training telah SELESAI dengan sukses!")
        return "COMPLETE"
    elif "ERROR" in stdout or "FAILED" in stdout:
        print("\n[ERROR] Terjadi kesalahan pada proses eksekusi kernel di Kaggle.")
        return "ERROR"
    return stdout

def download_and_deploy():
    status = check_status()
    if status != "COMPLETE":
        print("\n[PERINGATAN] Model belum siap diunduh. Tunggu hingga status 'COMPLETE'.")
        return

    print("\n" + "=" * 60)
    print("[DOWNLOAD] MENGUNDUH ARTIFAK MODEL DARI KAGGLE...")
    print("=" * 60)
    OUTPUT_DIR.mkdir(exist_ok=True)
    STATIC_MODELS_DIR.mkdir(parents=True, exist_ok=True)

    cmd = f"kaggle kernels output {KERNEL_SLUG} -p \"{OUTPUT_DIR}\""
    print(f"Menjalankan: {cmd}")
    stdout, stderr, code = run_cmd(cmd)
    print(stdout)
    if code != 0:
        print(f"Gagal mengunduh output: {stderr}")
        return

    # Cari file zip atau best.onnx
    zip_files = list(OUTPUT_DIR.glob("*.zip"))
    onnx_files = list(OUTPUT_DIR.rglob("best.onnx"))
    pt_files = list(OUTPUT_DIR.rglob("best.pt"))

    if zip_files:
        print(f"[EKSTRAK] Mengekstrak {zip_files[0].name}...")
        with zipfile.ZipFile(zip_files[0], 'r') as z:
            z.extractall(OUTPUT_DIR)
        onnx_files = list(OUTPUT_DIR.rglob("best.onnx"))
        pt_files = list(OUTPUT_DIR.rglob("best.pt"))

    if onnx_files:
        target_onnx = STATIC_MODELS_DIR / "best.onnx"
        shutil.copy2(onnx_files[0], target_onnx)
        print(f"[BERHASIL] Model WebAssembly (ONNX) terpasang di: {target_onnx}")
        print(f"           Ukuran: {target_onnx.stat().st_size / (1024*1024):.2f} MB")

    if pt_files:
        target_pt = STATIC_MODELS_DIR / "best.pt"
        shutil.copy2(pt_files[0], target_pt)
        print(f"[BERHASIL] Bobot PyTorch (best.pt) tersimpan di: {target_pt}")

    print("\n" + "=" * 60)
    print("[SUKSES] INTEGRASI SELESAI!")
    print("Model YOLOv8 kini aktif untuk Live Webcam Bounding Box di SkinCheck.")
    print("=" * 60)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "download":
        download_and_deploy()
    else:
        check_status()
