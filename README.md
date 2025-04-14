# Object Detection Demo

🚀 Try it live on [Hugging Face Spaces](https://huggingface.co/spaces/Ibrahimnasser/streamlit_yolo)

This is a simple, interactive Streamlit app that lets you perform object detection using **YOLOv5**.

## What is YOLO?

**YOLO (You Only Look Once)** is a real-time object detection system. It processes the image in one forward pass and predicts bounding boxes and class labels with remarkable speed.

In this app, we use the pre-trained `yolov5s` model from Ultralytics, fine-tuned for speed and lightweight usage — perfect for CPU inference on Hugging Face Spaces.

---
## Packages
```python
import streamlit as st
from PIL import Image
import torch
from io import BytesIO
import numpy as np
import cv2
```
---
## Run Locally
```bash
git clone https://github.com/96ibman/YOLOVision_Streamlit_HuggingFace.git
```

```bash
cd YOLOVision_Streamlit_HuggingFace
```

```bash
python -m venv venv
```

```bash
venv/Scripts/activate
```
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```
---
## About me
[Website](https://96ibman.github.io/ibrahim-nasser/)
