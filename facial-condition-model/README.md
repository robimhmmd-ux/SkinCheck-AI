---
license: apache-2.0
tags:
- computer-vision
- image-classification
- skin-analysis
- tensorflow
- keras
library_name: tensorflow
---

# Facial Condition Analysis Model

Detects 5 skin conditions: Acne, Dry Skin, Oily Skin, Dark Spots, Wrinkles

## Usage
```python
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model('finetuned_best.h5')
# Input: 224x224 RGB images
# Output: 5 predictions (percentages)
```

## Model Details
- Framework: TensorFlow/Keras
- Input Size: 224x224x3
- Output: 5 sigmoid outputs
## Model Weights
> **Note**: File bobot model binary (`finetuned_best.h5`, ~181 MB) tidak disertakan di repositori Git karena melampaui batas ukuran file GitHub (100 MB). Bobot model dapat disinkronkan langsung dari Kaggle menggunakan skrip:
> ```bash
> kaggle_training/2_unduh_model_ke_web.bat
> ```
