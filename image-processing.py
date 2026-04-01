# ==========================================================
# 📘 STREAMLIT IMAGE PROCESSING APP
# ==========================================================

import streamlit as st
import numpy as np
from PIL import Image

st.title("🖼️ Image Processing with NumPy")
st.write("Upload an image and see the processed result.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Create 2 columns for side-by-side display
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Original Image", use_container_width=True)

    # Select operation
    option = st.selectbox("Select Operation", ["Grayscale", "Blur", "Sharpen"])

    # ---------------------------
    # GRAYSCALE
    # ---------------------------
    img_array = np.array(image)

    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]
    gray = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)


    if option == "Grayscale":
        result = gray

    # ---------------------------
    # BLUR
    # ---------------------------
    elif option == "Blur":
        kernel = np.ones((3, 3)) / 9
        h, w = gray.shape
        result = np.zeros((h, w))

        for i in range(1, h-1):
            for j in range(1, w-1):
                region = gray[i-1:i+2, j-1:j+2]
                result[i, j] = np.sum(region * kernel)

        result = result.astype(np.uint8)

    # ---------------------------
    # SHARPEN
    # ---------------------------
    elif option == "Sharpen":
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        h, w = gray.shape
        result = np.zeros((h, w))

        for i in range(1, h-1):
            for j in range(1, w-1):
                region = gray[i-1:i+2, j-1:j+2]
                result[i, j] = np.sum(region * kernel)

        result = np.clip(result, 0, 255).astype(np.uint8)

    # Show processed image
    with col2:
        st.image(result, caption=f"{option} Image", use_container_width=True)

    # Optional: Show both below as well
    st.subheader("📊 Comparison")
    st.image([image, result], caption=["Original", option], width=300)
