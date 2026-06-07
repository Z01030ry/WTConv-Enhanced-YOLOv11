# WTConv-Enhanced YOLOv11 for Robust Blood Cell Cancer Detection

## Overview

This repository contains the official implementation of the paper:

**WTConv-Enhanced YOLOv11 for Robust Blood Cell Cancer Detection**

The proposed method improves the baseline YOLOv11 detector by incorporating:

* **WTConv (Wavelet Transform Convolution)** for enhanced multi-scale feature extraction;
* **Generalized Intersection over Union (GIoU) Loss** for improved bounding-box regression;
* Optimized feature representation for complex blood cell morphology and dense cell distributions.

The framework is designed for automatic blood cell cancer detection and classification in microscopic images.

---

## Method Framework

The proposed model introduces WTConv into the YOLOv11 backbone to improve frequency-aware feature extraction while replacing the original localization loss with GIoU loss to enhance localization accuracy.

Key contributions include:

1. Improved multi-resolution feature representation through wavelet decomposition.
2. Enhanced discrimination of morphologically similar blood cell categories.
3. More accurate localization of small and overlapping cells.
4. Reduced computational complexity while achieving superior detection performance.

---

## Dataset

The experiments were conducted using a publicly available blood cell dataset obtained from Roboflow.

Dataset source:

https://roboflow.com/

The dataset contains 13 blood cell categories, including:

* Abnormal Promyelocyte
* Atypical Lymphocyte
* Basophil
* Eosinophil
* Erythroblast
* Lymphoblast
* Lymphocyte
* Monoblast
* Monocyte
* Myeloblast
* Myelocyte
* Neutrophil
* Promonocyte

Please follow the original dataset license and terms of use.

---

## Experimental Environment

### Hardware

* NVIDIA GPU
* Intel/AMD CPU

### Software

* Python 3.10
* PyTorch
* CUDA
* Ultralytics YOLO Framework

---

## Repository Structure

```text
WTConv-Enhanced-YOLOv11/
│
├── ultralytics/          # Modified YOLOv11 framework
├── train.py             # Training script
├── runs/                # Experimental results
├── README.md
└── LICENSE
```

---

## Training

To train the proposed model:

```bash
python train.py
```

Model configuration files can be modified according to specific experimental requirements.

---

## Experimental Results

### Performance Comparison

| Model              | mAP@0.5   | Precision | Recall    | F1-score  |
| ------------------ | --------- | --------- | --------- | --------- |
| YOLOv8             | 0.674     | 0.618     | 0.567     | 0.591     |
| YOLOv9s            | 0.660     | 0.599     | 0.542     | 0.569     |
| YOLOv10n           | 0.674     | 0.612     | 0.590     | 0.601     |
| YOLOv12            | 0.682     | 0.628     | 0.579     | 0.602     |
| YOLOv11 (Baseline) | 0.686     | 0.742     | 0.833     | 0.785     |
| Proposed Method    | **0.709** | **0.806** | **0.917** | **0.858** |

The proposed WTConv-GIoU enhanced YOLOv11 achieves the best overall performance across all evaluation metrics.

---

## Computational Complexity

| Model            | Parameters (M) | GFLOPs |
| ---------------- | -------------- | ------ |
| YOLOv11          | 2.593          | 6.5    |
| YOLOv11 + WTConv | 2.477          | 6.3    |
| YOLOv11 + GIoU   | 2.591          | 6.4    |
| Proposed Method  | 2.477          | 6.3    |

The proposed model improves detection accuracy while maintaining a lightweight architecture.

---

## Reproducibility

All source code, model configurations, and experimental settings used in this study are publicly available in this repository.

Researchers can reproduce the reported results using the provided implementation and publicly available dataset.

---

## Citation

If you find this repository useful in your research, please cite:

```bibtex
@article{zhang2026wtconv,
  title={WTConv-Enhanced YOLOv11 for Robust Blood Cell Cancer Detection},
  author={Zhang, Rongyu and Xue, Zhipeng and Kong, Lingyun},
  journal={Pattern Analysis and Applications},
  year={2026}
}
```

---

## Authors

* Rongyu Zhang
* Zhipeng Xue
* Lingyun Kong (Corresponding Author)

School of Electronic Information Engineering

Xijing University, Xi'an, Shaanxi, China

Email: [1400100383@qq.com](mailto:1400100383@qq.com)

---

## License

This project is released for academic research purposes.
Please cite the associated publication when using this code.
