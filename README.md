# 🧠 Klasifikasi Tumor Otak Berbasis Deep Learning

## 📖 Deskripsi Proyek
**BrainTumor AI** adalah sistem klasifikasi citra medis berbasis **Deep Learning** yang dirancang untuk mengidentifikasi tumor otak secara otomatis dari citra **MRI**. Sistem ini bertujuan mendukung proses diagnosis dan analisis medis melalui pemanfaatan teknologi *computer vision*, sehingga deteksi tumor dapat dilakukan secara lebih cepat, konsisten, dan objektif sebagai bagian dari pengembangan **smart healthcare**.

Penelitian ini melakukan studi komparatif terhadap tiga arsitektur model, yaitu **Custom CNN**, **ResNet50**, dan **EfficientNetB0**, untuk memperoleh keseimbangan terbaik antara akurasi klasifikasi dan efisiensi komputasi. Aplikasi diimplementasikan dalam bentuk **antarmuka web interaktif berbasis Streamlit**, yang memungkinkan pengguna mengunggah citra MRI dan memperoleh hasil prediksi serta evaluasi performa model secara langsung.

---

## 📂 Dataset & Alur Pra-pemrosesan

- **Sumber Dataset:** Kaggle – *MRI Brain Tumor*
- **Total Dataset:** 7.024 citra MRI
- **Jumlah Kelas:** 4 kelas
- **Pembagian Data:**
  - Training: 80%
  - Validation/Test: 20%

Dataset disusun dalam struktur folder berdasarkan kelas tumor dan diproses untuk keperluan klasifikasi citra medis berbasis Deep Learning.

---

## 🛠️ Alur Pra-pemrosesan

- **Pengubahan Ukuran (Resizing):**  
  Seluruh citra distandarisasi ke ukuran **224 × 224 piksel** agar sesuai dengan kebutuhan input model **CNN**, **ResNet50**, dan **EfficientNetB0**.

- **Preprocessing Input:**  
  Disesuaikan dengan karakteristik masing-masing model.  
  - CNN menggunakan normalisasi dasar  
  - ResNet50 dan EfficientNetB0 menggunakan preprocessing standar ImageNet

- **Augmentasi Data:**  
  Diterapkan pada data pelatihan untuk meningkatkan kemampuan generalisasi model terhadap variasi citra MRI dan mengurangi risiko overfitting.

- **Data Loader:**  
  Data dimuat secara terstruktur dari direktori dataset dengan pengaturan batch size dan mode kelas yang konsisten pada seluruh model.

---

## 🧠 Arsitektur Model

- **Base CNN (Custom):**  
  Model konvolusional sederhana yang dibangun dari awal sebagai baseline performa klasifikasi.

- **ResNet50 (Transfer Learning):**  
  Model pralatih dengan *residual connection* untuk mengekstraksi fitur visual kompleks pada citra MRI.

- **EfficientNetB0 (Transfer Learning):**  
  Arsitektur efisien yang menyeimbangkan akurasi dan efisiensi komputasi.

---

## 📊 Hasil Evaluasi & Analisis Perbandingan

Sistem diuji menggunakan **data independen (test set)** untuk memastikan objektivitas evaluasi.

### 🔍 Tabel Perbandingan Performa

| Model | Precision | Recall | F1-Score | Test Accuracy | Analysis Comparison |
|------|-----------|--------|----------|---------------|---------------------|
| Base CNN (Custom) | 100% | 100% | 100% | 100% | Baseline kuat dengan performa sempurna pada data uji |
| ResNet50 (Transfer Learning) | 100% | 100% | 100% | 100% | Ekstraksi fitur stabil dan konsisten |
| EfficientNetB0 (Transfer Learning) | 100% | 100% | 100% | 100% | Top-Performer dengan arsitektur paling efisien |

---

## 📈 Insight Analisis Komprehensif

- **Konsistensi Performa:**  
  Ketiga model menunjukkan hasil sempurna pada seluruh metrik evaluasi.

- **Efisiensi Model:**  
  EfficientNetB0 unggul dalam efisiensi komputasi dan ukuran model dibandingkan ResNet50.

- **Stabilitas Baseline:**  
  Base CNN mampu menyamai performa model transfer learning pada dataset ini.

---

## ✅ Kesimpulan

Ketiga model mencapai performa klasifikasi yang sangat optimal. Namun, **EfficientNetB0** dipilih sebagai model utama karena menawarkan **efisiensi arsitektur terbaik tanpa mengorbankan akurasi**, sehingga paling sesuai untuk implementasi aplikasi berbasis web dan deployment ringan.

---

## ⚠️ Catatan Interpretasi Hasil (Overfitting & Kompleksitas Dataset)

Meskipun seluruh model mencapai akurasi **100%** pada data uji, hasil ini tidak serta-merta menunjukkan bahwa model sepenuhnya bebas dari overfitting. Tingginya performa dapat dipengaruhi oleh karakteristik dataset yang memiliki pemisahan kelas visual yang sangat jelas antara citra **glioma** dan **non-tumor**.

Selain itu, kapasitas arsitektur model yang cukup dalam, khususnya pada **ResNet50** dan **EfficientNetB0**, memungkinkan jaringan menangkap fitur visual secara sangat detail. Pada dataset dengan kompleksitas terbatas, kondisi ini berpotensi menghasilkan performa yang sangat tinggi meskipun kemampuan generalisasi terhadap data yang lebih beragam belum sepenuhnya teruji.

Oleh karena itu, diperlukan **pengujian lanjutan menggunakan dataset eksternal** atau skema validasi yang lebih ketat sebelum penerapan dalam konteks klinis atau medis nyata.

---

## ©️ Copyright
**Klasifikasi Tumor Otak**  
Final Project – Informatics Engineering  
Universitas Muhammadiyah Malang  

---

### “Technology for Smarter Healthcare”  
**Klasifikasi Tumor Otak Berbasis Deep Learning**  
Crafted by: **Devi Dian Aprili – 461**