import json
import os

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 🎯 SkinCheck: YOLOv8 Acne Detection Training on Kaggle\n",
                "### Melatih Model AI Deteksi Jerawat & Blemish Menggunakan Akselerasi GPU Kaggle\n",
                "\n",
                "Notebook ini disiapkan khusus oleh **Luvenna** untuk **Paduka Raja** guna melatih model YOLOv8 Object Detection pada dataset jerawat.\n",
                "\n",
                "**Fitur Otomatis:**\n",
                "1. 🚀 **Akselerasi GPU**: Memanfaatkan GPU NVIDIA (T4 / P100) di Kaggle untuk training berkecepatan tinggi.\n",
                "2. 📦 **Dataset Auto-Detection**: Mendeteksi dataset Kaggle yang dilampirkan (`osmankagankurnaz/acne-dataset-in-yolov8-format` atau dataset jerawat lainnya).\n",
                "3. ⚙️ **Konfigurasi Otomatis**: Membuat file `acne_kaggle.yaml` dengan path absolut yang valid secara otomatis.\n",
                "4. 🧠 **YOLOv8 Nano**: Menggunakan model `yolov8n.pt` yang ringan dan cepat untuk kamera real-time webcam.\n",
                "5. 🔄 **Ekspor ONNX WebAssembly**: Menghasilkan `best.onnx` untuk inferensi instan di browser dan `best.pt` untuk PyTorch.\n",
                "6. 📥 **Auto-ZIP**: Mengemas seluruh model siap pakai ke `skincheck_yolov8_acne_models.zip` di tab **Output** Kaggle."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Langkah 1: Persiapan Environment & GPU Check"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import os\n",
                "import sys\n",
                "import shutil\n",
                "import glob\n",
                "import torch\n",
                "import yaml\n",
                "from pathlib import Path\n",
                "\n",
                "print(\"=\" * 60)\n",
                "print(f\"Python Version : {sys.version.split()[0]}\")\n",
                "print(f\"PyTorch Version: {torch.__version__}\")\n",
                "gpu_available = torch.cuda.is_available()\n",
                "print(f\"GPU CUDA Ready : {gpu_available}\")\n",
                "if gpu_available:\n",
                "    print(f\"GPU Device Name: {torch.cuda.get_device_name(0)}\")\n",
                "    print(f\"GPU Memory     : {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB\")\n",
                "else:\n",
                "    print(\"⚠️ PERINGATAN: GPU tidak aktif! Pastikan 'Accelerator' di panel kanan Kaggle diatur ke 'GPU T4 x2' atau 'GPU P100'.\")\n",
                "print(\"=\" * 60)\n",
                "\n",
                "import socket\n",
                "def check_internet():\n",
                "    try:\n",
                "        socket.create_connection(('8.8.8.8', 53), timeout=3)\n",
                "        return True\n",
                "    except OSError:\n",
                "        return False\n",
                "\n",
                "has_internet = check_internet()\n",
                "print(f\"Internet Access: {'AKTIF' if has_internet else 'NONAKTIF'}\")\n",
                "if not has_internet:\n",
                "    print('⚠️ PERHATIAN: Internet di Kaggle masih MATI. Aktifkan toggle Internet di panel kanan (Notebook Options)!')\n",
                "\n",
                "# Install / Update Ultralytics, ONNX, dan dependensi lainnya\n",
                "!pip install -q --upgrade ultralytics onnx onnxruntime albumentations\n",
                "import ultralytics\n",
                "ultralytics.checks()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Langkah 2: Deteksi & Verifikasi Struktur Dataset Kaggle"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "input_dir = Path(\"/kaggle/input\")\n",
                "working_dir = Path(\"/kaggle/working\")\n",
                "\n",
                "print(\"🔍 Memeriksa direktori input /kaggle/input:\")\n",
                "for item in input_dir.iterdir():\n",
                "    print(\" -\", item.name)\n",
                "\n",
                "# Temukan folder dataset jerawat\n",
                "dataset_candidates = list(input_dir.glob(\"*acne*\")) + list(input_dir.glob(\"*skin*\"))\n",
                "if dataset_candidates:\n",
                "    dataset_root = dataset_candidates[0]\n",
                "    print(f\"\\n✅ Dataset terdeteksi di: {dataset_root}\")\n",
                "else:\n",
                "    # Fallback jika belum terpasang: download via kagglehub\n",
                "    print(\"\\n⚠️ Dataset belum terpasang di input. Mengunduh otomatis via kagglehub...\")\n",
                "    import kagglehub\n",
                "    download_path = kagglehub.dataset_download(\"osmankagankurnaz/acne-dataset-in-yolov8-format\")\n",
                "    dataset_root = Path(download_path)\n",
                "    print(f\"✅ Dataset berhasil diunduh ke: {dataset_root}\")\n",
                "\n",
                "# Cari file yaml bawaan atau telusuri struktur folder\n",
                "yaml_files = list(dataset_root.rglob(\"*.yaml\"))\n",
                "print(f\"File konfigurasi ditemukan: {[f.name for f in yaml_files]}\")\n",
                "\n",
                "# Temukan folder train & valid/val\n",
                "train_dir = None\n",
                "val_dir = None\n",
                "\n",
                "for sub in [dataset_root / \"data-2\", dataset_root]:\n",
                "    if (sub / \"train\" / \"images\").exists():\n",
                "        train_dir = sub / \"train\" / \"images\"\n",
                "        for v_name in [\"valid\", \"val\", \"test\"]:\n",
                "            if (sub / v_name / \"images\").exists():\n",
                "                val_dir = sub / v_name / \"images\"\n",
                "                break\n",
                "        base_data_path = sub\n",
                "        break\n",
                "\n",
                "if not train_dir:\n",
                "    # Cari secara rekursif\n",
                "    found_train = list(dataset_root.rglob(\"*train*/images\"))\n",
                "    found_val = list(dataset_root.rglob(\"*valid*/images\")) + list(dataset_root.rglob(\"*val*/images\"))\n",
                "    if found_train:\n",
                "        train_dir = found_train[0]\n",
                "        val_dir = found_val[0] if found_val else found_train[0]\n",
                "        base_data_path = train_dir.parent.parent\n",
                "    else:\n",
                "        raise FileNotFoundError(\"Folder train/images tidak ditemukan di dalam dataset!\")\n",
                "\n",
                "print(f\"Base Data Directory: {base_data_path}\")\n",
                "print(f\"Train Directory    : {train_dir} (Jumlah: {len(list(train_dir.glob('*')))} files)\")\n",
                "print(f\"Val Directory      : {val_dir} (Jumlah: {len(list(val_dir.glob('*')))} files)\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Langkah 3: Membuat Konfigurasi Dataset `acne_kaggle.yaml`"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Ekstrak nama kelas dari yaml asli jika ada\n",
                "class_names = {0: 'acne'}\n",
                "if yaml_files:\n",
                "    try:\n",
                "        with open(yaml_files[0], 'r') as yf:\n",
                "            parsed_yaml = yaml.safe_load(yf)\n",
                "            if 'names' in parsed_yaml:\n",
                "                class_names = parsed_yaml['names']\n",
                "                print(\"Label kelas yang ditemukan:\", class_names)\n",
                "    except Exception as e:\n",
                "        print(\"Gagal parse yaml asli, gunakan kelas default:\", e)\n",
                "\n",
                "kaggle_yaml_path = working_dir / \"acne_kaggle.yaml\"\n",
                "yaml_content = {\n",
                "    'path': str(base_data_path.resolve()),\n",
                "    'train': str(train_dir.resolve()),\n",
                "    'val': str(val_dir.resolve()),\n",
                "    'names': class_names\n",
                "}\n",
                "\n",
                "with open(kaggle_yaml_path, 'w') as f:\n",
                "    yaml.dump(yaml_content, f, default_flow_style=False)\n",
                "\n",
                "print(f\"✅ Konfigurasi acne_kaggle.yaml siap di: {kaggle_yaml_path}\")\n",
                "print(\"--------------------------------------------------\")\n",
                "print(open(kaggle_yaml_path).read())\n",
                "print(\"--------------------------------------------------\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Langkah 4: Training Model YOLOv8 (Acne Bounding Box)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "from ultralytics import YOLO\n",
                "\n",
                "# Muat base model YOLOv8 Nano Pretrained\n",
                "print(\"📥 Memuat pretrained model yolov8n.pt...\")\n",
                "model = YOLO('yolov8n.pt')\n",
                "\n",
                "# Parameter Training Khusus Overnight (Tinggal Tidur)\n",
                "EPOCHS = 100         # 100 Epochs untuk akurasi maksimal & konvergensi mAP optimal\n",
                "IMGSZ = 640          # Resolusi standar deteksi jerawat\n",
                "BATCH = 16           # Batch size optimal untuk GPU Kaggle (16GB VRAM)\n",
                "DEVICE = 0 if torch.cuda.is_available() else 'cpu'\n",
                "\n",
                "print(f\"🔥 Memulai training di device: {DEVICE} selama {EPOCHS} epochs (Overnight Mode)...\")\n",
                "results = model.train(\n",
                "    data=str(kaggle_yaml_path),\n",
                "    epochs=EPOCHS,\n",
                "    imgsz=IMGSZ,\n",
                "    batch=BATCH,\n",
                "    device=DEVICE,\n",
                "    project=str(working_dir / 'runs'),\n",
                "    name='skincheck_acne_run',\n",
                "    save=True,\n",
                "    plots=True,\n",
                "    workers=4,\n",
                "    patience=25,       # Early stopping jika tidak ada kenaikan mAP dalam 25 epoch\n",
                "    cos_lr=True,       # Cosine LR Scheduler untuk penurunan loss yang stabil dan tajam\n",
                "    mosaic=1.0,        # Augmentasi mosaik 4 gambar untuk variasi wajah\n",
                "    mixup=0.1,         # Augmentasi mixup untuk mendeteksi jerawat kecil & samar\n",
                "    save_period=10     # Simpan checkpoint tiap 10 epoch\n",
                ")\n",
                "\n",
                "print(\"🎉 Training selesai dengan sempurna!\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Langkah 5: Evaluasi & Metrik Akurasi Model"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import matplotlib.pyplot as plt\n",
                "import cv2\n",
                "\n",
                "best_weights = working_dir / \"runs\" / \"skincheck_acne_run\" / \"weights\" / \"best.pt\"\n",
                "print(f\"🏆 Bobot Terbaik: {best_weights}\")\n",
                "print(f\"Ukuran File: {best_weights.stat().st_size / (1024*1024):.2f} MB\")\n",
                "\n",
                "# Validasi akurasi\n",
                "trained_model = YOLO(str(best_weights))\n",
                "metrics = trained_model.val()\n",
                "\n",
                "print(\"\\n================ 📊 EVALUATION METRICS ================\")\n",
                "print(f\" mAP@0.50      : {metrics.box.map50 * 100:.2f}%\")\n",
                "print(f\" mAP@0.50:0.95 : {metrics.box.map * 100:.2f}%\")\n",
                "print(f\" Precision     : {metrics.box.mp * 100:.2f}%\")\n",
                "print(f\" Recall        : {metrics.box.mr * 100:.2f}%\")\n",
                "print(\"=======================================================\")\n",
                "\n",
                "# Tampilkan grafik hasil training\n",
                "results_plot = working_dir / \"runs\" / \"skincheck_acne_run\" / \"results.png\"\n",
                "if results_plot.exists():\n",
                "    plt.figure(figsize=(15, 6))\n",
                "    img = cv2.imread(str(results_plot))\n",
                "    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))\n",
                "    plt.axis('off')\n",
                "    plt.title(\"Loss & Metric Progression During Training\", fontsize=14)\n",
                "    plt.show()\n",
                "\n",
                "# Tampilkan sampel prediksi pada data validasi\n",
                "val_batch_pred = working_dir / \"runs\" / \"skincheck_acne_run\" / \"val_batch0_pred.jpg\"\n",
                "if val_batch_pred.exists():\n",
                "    plt.figure(figsize=(12, 12))\n",
                "    img = cv2.imread(str(val_batch_pred))\n",
                "    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))\n",
                "    plt.axis('off')\n",
                "    plt.title(\"Contoh Deteksi Bounding Box Jerawat pada Validasi\", fontsize=14)\n",
                "    plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Langkah 6: Ekspor ke Format ONNX (WebAssembly) & Packaging ZIP"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Ekspor model ke format ONNX agar dapat dijalankan langsung di browser via ONNX Runtime WebAssembly\n",
                "print(\"🔄 Mengekspor model ke ONNX (imgsz=640, simplify=True)...\")\n",
                "onnx_export_file = trained_model.export(format='onnx', imgsz=640, simplify=True)\n",
                "print(f\"✅ Berhasil diekspor: {onnx_export_file}\")\n",
                "\n",
                "# Siapkan folder pengemasan final\n",
                "export_folder = working_dir / \"skincheck_models_export\"\n",
                "export_folder.mkdir(exist_ok=True)\n",
                "\n",
                "# Salin best.pt dan best.onnx\n",
                "shutil.copy2(best_weights, export_folder / \"best.pt\")\n",
                "shutil.copy2(onnx_export_file, export_folder / \"best.onnx\")\n",
                "\n",
                "# Salin file metadata label info\n",
                "with open(export_folder / \"classes.json\", 'w') as jf:\n",
                "    json.dump({\"classes\": list(class_names.values()) if isinstance(class_names, dict) else class_names}, jf, indent=2)\n",
                "\n",
                "# Buat arsip ZIP di root /kaggle/working/\n",
                "zip_path = working_dir / \"skincheck_yolov8_acne_models\"\n",
                "shutil.make_archive(str(zip_path), 'zip', str(export_folder))\n",
                "\n",
                "final_zip = working_dir / \"skincheck_yolov8_acne_models.zip\"\n",
                "print(\"\\n\" + \"=\" * 65)\n",
                "print(\"🎉 SELURUH PROSES TRAINING & EXPORT BERHASIL DISELESAIKAN!\")\n",
                "print(\"=\" * 65)\n",
                "print(f\"📦 File ZIP Siap Download: {final_zip} ({final_zip.stat().st_size / (1024*1024):.2f} MB)\")\n",
                "print(f\"   - best.onnx (Untuk real-time webcam di web SkinCheck)\")\n",
                "print(f\"   - best.pt   (Untuk inferensi Python / PyTorch backend)\")\n",
                "print(f\"   - classes.json\")\n",
                "print(\"\\n💡 CARA MENGUNDUH DI KAGGLE:\")\n",
                "print(\"1. Di panel kanan Kaggle Notebook, buka tab 'Output'.\")\n",
                "print(\"2. Klik tombol download (ikon panah bawah) pada 'skincheck_yolov8_acne_models.zip'.\")\n",
                "print(\"3. Ekstrak 'best.onnx' ke folder: Project_SkinChek/app/static/models/best.onnx\")\n",
                "print(\"=\" * 65)"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.10.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Tulis ke kaggle_training dan notebooks
for out_path in [
    r"c:\Users\roboy\Documents\Tugas word\TUGAS CODINGAN\RekayasaPerangktLunak\Project_SkinChek\kaggle_training\train_acne_yolov8_kaggle.ipynb",
    r"c:\Users\roboy\Documents\Tugas word\TUGAS CODINGAN\RekayasaPerangktLunak\Project_SkinChek\notebooks\train_acne_yolov8_kaggle.ipynb"
]:
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)
    print(f"Written: {out_path}")
