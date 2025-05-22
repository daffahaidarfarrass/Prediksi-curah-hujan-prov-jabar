# 🌧️ Prediksi Curah Hujan di Jawa Barat menggunakan Thin Plate Spline (TPS)

Aplikasi ini memungkinkan pengguna memprediksi curah hujan di titik tertentu di Provinsi Jawa Barat berdasarkan input dari 4 titik referensi (misalnya: Bandung, Bogor, Sukabumi, dan Cianjur). Prediksi dilakukan dengan metode **interpolasi Thin Plate Spline (TPS)**, dan visualisasi interaktif ditampilkan melalui peta menggunakan **Folium** di dalam dashboard **Streamlit**.

---

## 🎯 Fitur Utama

- Input manual curah hujan dari 4 lokasi berbeda
- Prediksi curah hujan di titik lain menggunakan interpolasi TPS
- Visualisasi lokasi titik data dan prediksi di peta interaktif
- Tampilan antarmuka yang sederhana menggunakan Streamlit

## 🧪 Teknologi yang Digunakan

- Python 3.11.3
- streamlit 1.45.1
- Scipy 1.15.3
- folium 0.19..6
- streamlit_folium 0.25.0

## 🚀 Cara Menjalankan

1. **Clone repositori ini**
   ```bash
   git clone https://github.com/username/prediksi-curah-hujan-tps.git
2. **Masuk ke folder dictionary dimana file ini disimpan**
   ```bash
   cd prediksi-curah-hujan-tps
3. ketik Install dependensi
   ```bash
   pip install -r requirements.txt'
4. ketik
   ```bash
   streamlit run anum.py
5. file akan terbuka dibrowser
