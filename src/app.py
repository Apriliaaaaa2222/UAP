import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
from PIL import Image
from sklearn.metrics import ConfusionMatrixDisplay
import plotly.graph_objects as go   # ⬅️ TAMBAHAN UNTUK SPEEDOMETER

# =========================
# CONFIG & PATH
# =========================
st.set_page_config(
    page_title="MRI Brain Tumor Classification",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_SIZE = (224, 224)

MODEL_FILES = {
    "CNN Non-Pretrained": "cnn_non_pretrained.h5",
    "EfficientNetB0": "efficientnetb0.h5",
    "EfficientNetB0 Fine-Tuned": "efficientnetb0_finetuned.h5",
    "ResNet50": "resnet50_head.h5",
    "ResNet50 Fine-Tuned": "resnet50_finetuned.h5"
}

EVAL_FILES = {
    "CNN Non-Pretrained": {
        "report": "cnn_non_pretrained_classification_report.csv",
        "cm": "cnn_non_pretrained_confusion_matrix.csv"
    },
    "EfficientNetB0": {
        "report": "effnet_classification_report.csv",
        "cm": "effnet_confusion_matrix.csv"
    },
    "EfficientNetB0 Fine-Tuned": {
        "report": "effnet_finetune_classification_report.csv",
        "cm": "effnet_finetune_confusion_matrix.csv"
    },
    "ResNet50": {
        "report": "resnet_classification_report.csv",
        "cm": "resnet_confusion_matrix.csv"
    }
}

# =========================
# LOAD CLASS LABEL
# =========================
with open(os.path.join(BASE_DIR, "class_indices.json")) as f:
    class_indices = json.load(f)

class_names = {v: k for k, v in class_indices.items()}

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚙️ Control Panel")

selected_model = st.sidebar.selectbox(
    "Pilih Arsitektur CNN",
    list(MODEL_FILES.keys())
)

show_eval = st.sidebar.checkbox("📊 Tampilkan Evaluasi Model", value=True)

st.sidebar.info(
    "Sistem AI untuk klasifikasi **Glioma** dan **No Tumor** "
    "berbasis citra MRI otak."
)

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model(model_path):
    return tf.keras.models.load_model(model_path)

model_path = os.path.join(BASE_DIR, MODEL_FILES[selected_model])
model = load_model(model_path)

# =========================
# HEADER
# =========================
st.markdown(
    "<h1 style='text-align:center;'>🧠 MRI Brain Tumor Classification</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>AI-Based Medical Image Analysis Dashboard (UJI UAP)</p>",
    unsafe_allow_html=True
)
st.divider()

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs(
    ["🏠 Dashboard", "🧠 Klasifikasi MRI", "📊 Evaluasi Model", "ℹ️ Tentang Sistem"]
)

# =========================
# DASHBOARD
# =========================
with tab1:
    st.subheader("📌 Ringkasan Sistem")
    st.write("""
    Aplikasi ini menggunakan model **Convolutional Neural Network (CNN)** 
    untuk melakukan klasifikasi tumor otak dari citra **MRI**.
    
    Model yang tersedia:
    - CNN Non-Pretrained
    - EfficientNetB0
    - EfficientNetB0 Fine-Tuned
    - ResNet50
    - ResNet50 Fine-Tuned
    """)

# =========================
# KLASIFIKASI MRI
# =========================
with tab2:
    st.subheader("🧠 Klasifikasi Citra MRI")

    uploaded_file = st.file_uploader(
        "Upload citra MRI otak",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Citra MRI", width=320)

        img = img.resize(IMG_SIZE)
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = model.predict(img_array)
        pred_class = np.argmax(pred)
        confidence = np.max(pred) * 100

        # HASIL PREDIKSI
        st.success(f"**Prediksi:** {class_names[pred_class]}")

        # =========================
        # SPEEDOMETER / GAUGE
        # =========================
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=confidence,
            number={"suffix": "%"},
            title={"text": "Confidence Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2563eb"},
                "steps": [
                    {"range": [0, 50], "color": "#7f1d1d"},
                    {"range": [50, 75], "color": "#78350f"},
                    {"range": [75, 100], "color": "#14532d"},
                ],
            }
        ))

        fig.update_layout(
            height=320,
            margin=dict(l=10, r=10, t=60, b=10)
        )

        st.plotly_chart(fig, use_container_width=True)

# =========================
# EVALUASI MODEL
# =========================
with tab3:
    st.subheader("📊 Evaluasi Model")

    if show_eval and selected_model in EVAL_FILES:
        report_path = os.path.join(
            BASE_DIR, EVAL_FILES[selected_model]["report"]
        )
        cm_path = os.path.join(
            BASE_DIR, EVAL_FILES[selected_model]["cm"]
        )

        if os.path.exists(report_path) and os.path.exists(cm_path):
            df_report = pd.read_csv(report_path)
            df_cm = pd.read_csv(cm_path, index_col=0)

            st.markdown("### 📋 Classification Report")
            st.dataframe(df_report, use_container_width=True)

            st.markdown("### 🔢 Confusion Matrix")
            fig, ax = plt.subplots()
            ConfusionMatrixDisplay(df_cm.values).plot(ax=ax)
            st.pyplot(fig)
        else:
            st.warning("⚠️ File evaluasi tidak tersedia.")
    else:
        st.info("Evaluasi tidak tersedia untuk model ini.")

# =========================
# TENTANG SISTEM
# =========================
with tab4:
    st.subheader("ℹ️ Tentang Sistem")
    st.write("""
    **Judul:** MRI Brain Tumor Classification  
    **Metode:** CNN & Transfer Learning  
    **Dataset:** MRI Otak  
    **Kelas:** Glioma, No Tumor  
    **Tahun:** 2025  

    Aplikasi ini dibuat sebagai bagian dari **UJI UAP**.
    """)

st.divider()
st.caption("UJI UAP • MRI Brain Tumor Classification • 2025")
