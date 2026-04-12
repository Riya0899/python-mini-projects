import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

st.title("📸 Image Analyzer")

uploaded_file = st.file_uploader("Upload an image")

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image")

    img_array = np.array(img)

    df = pd.DataFrame(img_array.reshape(-1, 3), columns=['R', 'G', 'B'])

    st.write("Average Color:")
    st.write(df.mean())

    st.write("Bright Pixels Count:")
    bright = df[(df['R'] > 200) & (df['G'] > 200) & (df['B'] > 200)]
    st.write(len(bright))

