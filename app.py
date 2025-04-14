import streamlit as st
from PIL import Image
import torch
from io import BytesIO
import numpy as np
import cv2

st.set_page_config(page_title="YOLO Object Detection", layout="centered")

st.title("YOLO Object Detection App")
st.write("Upload an image and let the YOLOv5 model detect objects in it.")

# Load YOLOv5 model from Ultralytics
@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

model = load_model()

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    if st.button("Detect Objects"):
        with st.spinner("Detecting..."):
            results = model(img)

            
            results.render() 
            detected_img = Image.fromarray(results.ims[0])
            
            st.image(detected_img, caption="Detected Objects", use_container_width=True)

            st.success("Done!")