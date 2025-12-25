# Klasifikasi Tumor Otak

📖 Deskripsi Proyek
BrainTumor AI adalah sistem klasifikasi citra medis berbasis Deep Learning yang dirancang untuk mengidentifikasi tumor otak secara otomatis dari citra MRI. Sistem ini bertujuan mendukung proses diagnosis dan analisis medis melalui pemanfaatan teknologi computer vision, sehingga deteksi tumor dapat dilakukan secara lebih cepat, konsisten, dan objektif sebagai bagian dari pengembangan smart healthcare.
Penelitian ini melakukan studi komparatif terhadap tiga arsitektur model, yaitu Custom CNN, ResNet, dan EfficientNet, untuk memperoleh keseimbangan terbaik antara akurasi klasifikasi dan efisiensi komputasi. Aplikasi diimplementasikan dalam bentuk antarmuka web interaktif berbasis Streamlit, yang memungkinkan pengguna mengunggah citra MRI dan memperoleh hasil prediksi serta evaluasi performa model secara langsung.

📂 Dataset & Alur Pra-pemrosesan
Proyek ini menggunakan dataset citra MRI tumor otak yang disusun dalam struktur folder berdasarkan kelas tumor, kemudian diproses untuk keperluan klasifikasi citra medis berbasis Deep Learning. Dataset memiliki jumlah data yang cukup besar untuk memastikan model mampu mengenali variasi pola visual tumor pada citra MRI.

Sumber Dataset: Kaggle - MRI BRAIN TUMOR
Total Dataset: 7.024 Citra
Jumlah Kelas: 4 Kelas
Pembagian Data: Training: 80% data & Validation/Test: 20% data

Alur Pra-Pemrosesan
Pengubahan Ukuran (Resizing): Seluruh citra distandarisasi ke ukuran 224 × 224 piksel agar sesuai dengan kebutuhan input model CNN, ResNet50, dan EfficientNetB0, sehingga setiap model menerima dimensi citra yang seragam selama proses pelatihan dan pengujian.
Preprocessing Input: Tahap pra-pemrosesan disesuaikan dengan karakteristik masing-masing arsitektur. Model CNN menggunakan normalisasi dasar untuk menyesuaikan skala nilai piksel, sedangkan ResNet50 dan EfficientNetB0 menggunakan metode preprocessing khusus yang selaras dengan standar model pralatih ImageNet.
Augmentasi Data: Augmentasi data diterapkan pada data pelatihan untuk meningkatkan kemampuan generalisasi model terhadap variasi citra MRI, seperti perbedaan orientasi dan kondisi visual, sehingga mengurangi risiko overfitting.
Data Loader: Data dimuat secara terstruktur dari direktori dataset dengan pengaturan ukuran batch dan mode kelas yang konsisten pada seluruh model, guna memastikan proses pelatihan dan evaluasi berjalan secara adil dan terstandarisasi.

🧠 Arsitektur Model
Base CNN (Custom): Model konvolusional sederhana yang dibangun dari awal sebagai baseline performa klasifikasi.
ResNet50 (Transfer Learning): Model pralatih dengan residual connection untuk mengekstraksi fitur visual kompleks pada citra MRI.
EfficientNetB0 (Transfer Learning): Arsitektur efisien yang menyeimbangkan akurasi dan efisiensi komputasi.

📊 Hasil Evaluasi & Analisis Perbandingan
Sistem diuji menggunakan data independen (test set) untuk memastikan objektivitas evaluasi. Berikut rangkuman performa dari ketiga model klasifikasi tumor otak:

1. Tabel Perbandingan Performa
|
|
3. Insight Analisis Komprehensif
Konsistensi Performa: Ketiga model menunjukkan hasil sempurna (100%) pada seluruh metrik evaluasi, menandakan dataset terklasifikasi dengan sangat baik pada skenario pengujian.
Efisiensi Model: Meskipun akurasi setara, EfficientNetB0 tetap unggul dari sisi efisiensi komputasi dan ukuran model dibandingkan ResNet50.
Stabilitas Baseline: Base CNN mampu mencapai performa setara dengan model transfer learning, menunjukkan bahwa arsitektur sederhana pun efektif pada dataset ini.

4. Kesimpulan
Ketiga model mencapai performa klasifikasi yang sangat optimal, namun EfficientNetB0 dipilih sebagai model utama karena menawarkan efisiensi arsitektur terbaik tanpa mengorbankan akurasi, sehingga paling sesuai untuk implementasi aplikasi berbasis web dan deployment ringan.

⚠️ Catatan Interpretasi Hasil (Overfitting & Kompleksitas Dataset)
Meskipun seluruh model mencapai akurasi 100% pada data uji, hasil ini tidak serta-merta menunjukkan bahwa model sepenuhnya bebas dari overfitting. Tingginya performa dapat dipengaruhi oleh karakteristik dataset yang memiliki pemisahan kelas visual yang sangat jelas antara citra glioma dan non-tumor, sehingga proses klasifikasi menjadi relatif lebih mudah bagi model.
Selain faktor dataset, kapasitas arsitektur model yang cukup dalam dan representatif, khususnya pada model ResNet50 dan EfficientNetB0, memungkinkan jaringan untuk menangkap fitur visual secara sangat detail. Pada dataset dengan kompleksitas yang terbatas, kondisi ini berpotensi menghasilkan performa yang sangat tinggi, meskipun kemampuan generalisasi terhadap data yang lebih beragam belum sepenuhnya teruji.
Lebih lanjut, kemungkinan adanya kemiripan distribusi data antara data training dan testing juga dapat berkontribusi terhadap hasil evaluasi yang sempurna. Oleh karena itu, untuk memastikan robustnes dan kemampuan generalisasi model pada skenario nyata, diperlukan pengujian lanjutan menggunakan dataset eksternal, citra MRI dari sumber berbeda, atau skema validasi yang lebih ketat sebelum penerapan dalam konteks klinis atau medis sebenarnya.

Copyright
Klasifikasi Tumor Otak : Final Project
Informatics Engineering Universitas Muhammadiyah Malang

“Technology for Smarter Healthcare”
Klasifikasi Tumor Otak Berbasis Deep Learning
Crafted by: Devi Dian Aprili – 461
