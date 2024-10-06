import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#memuat dataset
hour_df = pd.read_csv('hour.csv')
day_df = pd.read_csv('day.csv')

#judul dashboard
st.title("Dashboard Analisis Jumlah Sewa Sepeda")

#menampilkan data
if st.checkbox("Tampilkan Data hour_df"):
    st.write(hour_df)

if st.checkbox("Tampilkan Data day_df"):
    st.write(day_df)

#menampilkan statistik dasar
if st.button('Tampilkan Data Statistik'):
    st.write(hour_df.describe())
    st.write(day_df.describe())

st.write("")
st.write("")

st.header("Faktor - faktor yang Mempengaruhi Jumlah Sewa Sepeda pada Hari Tertentu")

#mengatur style untuk visualisasi
sns.set(style="whitegrid")

#visualisasi jumlah sewa sepeda berdasar suhu
st.subheader('Pengaruh Suhu terhadap Jumlah Sewa Sepeda berdasar Kondisi Cuaca')
plt.figure(figsize=(12, 6))
sns.scatterplot(data=hour_df, x='temp', y='cnt', hue='weathersit', alpha=0.7)
plt.title('Pengaruh Suhu terhadap Jumlah Sewa Sepeda berdasar Kondisi Cuaca')
plt.xlabel('Suhu')
plt.ylabel('Jumlah Sewa Sepeda')
plt.legend(title='Kondisi Cuaca', loc='upper right', labels=['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Berat'])
st.pyplot(plt)
plt.clf()
st.write("Dari grafik dapat dilihat bahwa saat suhu meningkat, jumlah sewa sepeda cenderung mengingkat juga. Terlihat bahwa suhu merupakan faktor yang mempengaruhi jumlah sewa sepeda, terutama disaat kondisi cuaca yang cerah.")

#visualisasi jumlah sewa sepeda berdasar kelembapan
st.subheader('Pengaruh Kelembapan terhadap Jumlah Sewa Sepeda berdasar Kondisi Cuaca')
plt.figure(figsize=(12, 6))
sns.scatterplot(data=hour_df, x='hum', y='cnt', hue='weathersit', alpha=0.7)
plt.title('Pengaruh Kelembapan terhadap Jumlah Sewa Sepeda berdasar Kondisi Cuaca')
plt.xlabel('Kelembapan')
plt.ylabel('Jumlah Sewa Sepeda')
plt.legend(title='Kondisi Cuaca', loc='upper right', labels=['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Berat'])
st.pyplot(plt)
plt.clf()
st.write("Dari grafik dapat dilihat bahwa saat kelembapan berada di 0.2 - 0.8 jumlah sewa sepeda cenderung mengingkat. Terlihat bahwa kelembapan merupakan faktor yang mempengaruhi jumlah sewa sepeda, terutama disaat kondisi cuaca yang cerah.")


#visualisasi jumlah sewa sepeda berdasar kecepatan angin
st.subheader('Pengaruh Kecepatan Angin terhadap Jumlah Sewa Sepeda berdasarkan Kondisi Cuaca')
plt.figure(figsize=(12, 6))
sns.scatterplot(data=hour_df, x='windspeed', y='cnt', hue='weathersit', alpha=0.7)
plt.title('Pengaruh Kecepatan Angin terhadap Jumlah Sewa Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kecepatan Angin')
plt.ylabel('Jumlah Sewa Sepeda')
plt.legend(title='Kondisi Cuaca', loc='upper right', labels=['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Berat'])
st.pyplot(plt)
plt.clf()
st.write("Dari grafik dapat dilihat bahwa semakin kecil kecepatan angin, jumlah sewa sepeda cenderung mengingkat. Terlihat bahwa kecepatan angin merupakan faktor yang mempengaruhi jumlah sewa sepeda, terutama disaat kondisi cuaca yang cerah.")

#visualisasi rata - rata jumlah sewa sepeda berdasar jam
st.subheader('Rata - Rata Jumlah Sewa Sepeda per Jam dalam Sehari berdasar Kondisi Cuaca')
plt.figure(figsize=(12, 6))
sns.lineplot(data=hour_df, x='hr', y='cnt', hue='weathersit', estimator='mean', marker='o')
plt.title('Rata - Rata Jumlah Sewa Sepeda per Jam dalam Sehari berdasar Kondisi Cuaca')
plt.xlabel('Jam')
plt.ylabel('Rata - Rata Jumlah Sewa Sepeda')
plt.legend(title='Kondisi Cuaca', loc='upper right', labels=['Cerah', 'Kabut', 'Hujan Ringan', 'Hujan Berat'])
plt.xticks(range(0, 24))
plt.grid()
st.pyplot(plt)
plt.clf()
st.write("Dari grafik dapat dilihat bahwa saat jam 17.00 - 18.00 jumlah sewa sepeda cenderung mengingkat. Terlihat bahwa jam merupakan faktor yang mempengaruhi jumlah sewa sepeda, terutama disaat kondisi cuaca yang cerah.")

#visualisasi rata - rata jumlah sewa sepeda berdasar hari
st.subheader('Rata - Rata Jumlah Sewa Sepeda berdasar Hari dalam Seminggu')
plt.figure(figsize=(12, 6))
sns.barplot(data=hour_df, x='weekday', y='cnt', estimator='mean')
plt.title('Rata - Rata Jumlah Sewa Sepeda berdasar Hari dalam Seminggu')
plt.xlabel('Hari')
plt.ylabel('Rata - Rata Jumlah Sewa Sepeda')
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
plt.grid(axis='y')
st.pyplot(plt)
plt.clf()
st.write("Dari grafik dapat dilihat bahwa saat hari Jumat dan Sabtu jumlah sewa sepeda cenderung mengingkat. Terlihat bahwa hari merupakan faktor yang mempengaruhi jumlah sewa sepeda.")

st.header("Perbedaan Jumlah Sewa Sepeda antara Working Day dan Weekend")

#menghitung rata - rata jumlah sewa sepeda berdasar kategori working day dan weekend
hour_df['day_type'] = hour_df['workingday'].apply(lambda x: 'Working Day' if x == 1 else 'Weekend')
rata_sewa = hour_df.groupby('day_type')['cnt'].mean().reset_index()

#memvisualisasikan jumlah sewa sepeda berdasar working day dan weekend
st.subheader('Rata - Rata Jumlah Sewa Sepeda antara Working Day dan Weekend')
plt.figure(figsize=(8, 6))
sns.barplot(data=rata_sewa, x='day_type', y='cnt', palette='pastel')
plt.title('Rata - Rata Jumlah Sewa Sepeda antara Working Day dan Weekend')
plt.xlabel('Hari')
plt.ylabel('Rata - Rata Jumlah Sewa Sepeda')
plt.ylim(0, rata_sewa['cnt'].max() + 10)  # Menambahkan space atas
st.pyplot(plt)
plt.clf()
st.write("Dari grafik dapat dilihat bahwa rata - rata saat working day jumlah sewa sepeda memiliki jumlah yang lebih tinggi.")

#RFM Analysis

st.header("Analisis Lanjutan dengan RFM Analysis")


#mengubah kolom dteday menjadi tipe datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

#menambahkan customer_id
hour_df['customer_id'] = hour_df['registered'].cumsum()  

#menyiapkan dataframe untuk RFM
rfm_df = hour_df.groupby('customer_id').agg({
    'dteday': 'max',  #mengambil tanggal penyewaan terakhir
    'cnt': 'sum'      #menghitung total penyewaan
})

#mengganti nama kolom
rfm_df.columns = ['last_rental_date', 'monetary']

#menghitung Recency
recent_date = hour_df['dteday'].max()
rfm_df['recency'] = (recent_date - rfm_df['last_rental_date']).dt.days

#menghapus kolom yang tdk dibutuhkan
rfm_df.drop('last_rental_date', axis=1, inplace=True)

#menampilkan hasil RFM
st.write(rfm_df.head())

#menghitung Frequency
rfm_df['frequency'] = hour_df.groupby('customer_id')['cnt'].count().values

#menampilkan hasil RFM
st.write(rfm_df.head())

#menampilkan ringkasan RFM
st.subheader('Ringkasan Statistik RFM')
st.write(rfm_df.describe())

#memvisualisasikan distribusi frekuensi
st.subheader('Distribusi Frekuensi Penyewaan Sepeda')
plt.figure(figsize=(10, 6))
sns.histplot(rfm_df['frequency'], bins=30, kde=True)
plt.title('Distribusi Frekuensi Penyewaan Sepeda')
plt.xlabel('Frekuensi')
plt.ylabel('Jumlah Pengguna')
st.pyplot(plt)
plt.clf()

#memvisualisasikan Recency dan Frequency
st.subheader('Recency dan Frequency')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rfm_df, x='recency', y='frequency')
plt.title('Recency dan Frequency')
plt.xlabel('Recency')
plt.ylabel('Frekuensi Penyewaan')
plt.axhline(y=rfm_df['frequency'].mean(), color='r', linestyle='--')
plt.axvline(x=rfm_df['recency'].mean(), color='g', linestyle='--')
st.pyplot(plt)
plt.clf()

st.header("Kesimpulan")
st.write("1. Faktor - faktor yang mempengaruhi jumlah sewa sepeda pada hari tertentu adalah suhu, kelembapan, kecepatan angin, jam sewa, dan hari, akan meningkat terutama disaat cuaca cerah.")
st.write("2. Jumlah sewa sepeda antara Working Day lebih tinggi dibandingkan dengan Weekend.")