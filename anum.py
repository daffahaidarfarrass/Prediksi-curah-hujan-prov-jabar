import streamlit as st
import pandas as pd
import numpy as np
from scipy.interpolate import Rbf
import folium
from streamlit_folium import folium_static



# Title Page
st.title('Analisis Numerik')
st.title('Curah Hujan')

kolom1, kolom2 = st.columns(2)

#kolom untuk curah hujan
with kolom1:
    rainfall1 = st.number_input(label="Curah hujan titik 1", min_value=0)
    rainfall2 = st.number_input(label="Curah hujan titik 2", min_value=0)
with kolom2:
    rainfall3 = st.number_input(label="Curah hujan titik 3", min_value=0)
    rainfall4 = st.number_input(label="Curah hujan titik 4", min_value=0)

st.title('Area yang dicari')
# Data dummy curah hujan di Jawa Barat
data = {
    'Bandung': {'coords': (-6.9147, 107.6098), 'rainfall': [rainfall1]},
    'Bogor': {'coords': (-6.5944, 106.7892), 'rainfall': [rainfall2]},
    'Sukabumi': {'coords': (-6.9180, 106.9273), 'rainfall': [rainfall3]},
    'Cianjur': {'coords': (-6.8224, 107.1315), 'rainfall': [rainfall4]},
}

# Ekstraksi koordinat dan curah hujan dari data
coords = np.array([data[stasiun]['coords'] for stasiun in data])
rainfall = np.array([data[stasiun]['rainfall'] for stasiun in data])

# Fungsi interpolasi Thin Plate Spline (TPS)
rbf = Rbf(coords[:, 0], coords[:, 1], rainfall[:, 0], function='thin_plate')

kolom3, kolom4 = st.columns (2)
# Koordinat untuk prediksi
with kolom3 :
    latitude_pred = st.number_input(label="Koordinat X" ,value=-6.8)  # Asumsi latitude untuk prediksi
with kolom4:
    longitude_pred = st.number_input(label="Koordinat Y" ,value= 107.0)  # Asumsi longitude untuk prediksi

# Membuat objek peta dengan lokasi tengah dan zoom awal
peta = folium.Map(location=[latitude_pred, longitude_pred], zoom_start=8.5)

# Menambahkan titik pertama
folium.Marker(
    [-6.9147, 107.6098],
    popup='Bandung',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(peta)

# Menambahkan titik kedua
folium.Marker(
    [-6.5944, 106.7892],
    popup='Titik Kedua',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(peta)

folium.Marker(
    [latitude_pred, longitude_pred],
    popup='Titik yang dicari',
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(peta)

# Menampilkan peta di Streamlit
folium_static(peta)

# Prediksi curah hujan di lokasi yang ditentukan
predicted_rainfall = rbf(latitude_pred, longitude_pred)
st.subheader("Prediksi curah hujan di koordinat ({}, {}): {:.2f} mm".format(latitude_pred, longitude_pred, predicted_rainfall))
