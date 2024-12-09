# prompt: buat dashboard beserta analisis pertanyaan 1 sampai 5 dan analisis lajutan dengan streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data (replace with your actual data loading)
day_data = pd.read_csv('data/day.csv')
hour_data = pd.read_csv('data/hour.csv')

# Berdasarkan hasil assessing data, tidak ditemukan missing value dan duplikasi data pada kedua dataset. 
# Namun, perlu dilakukan beberapa langkah cleaning data:

# Mengubah tipe data kolom 'dteday' menjadi datetime pada kedua dataset.
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Mengganti angka menjadi keterangan pada kolom 'season' di day_df
day_df['season'] = day_df['season'].map({    1: 'Spring',    2: 'Summer',    3: 'Fall',    4: 'Winter'})

# Mengganti angka menjadi keterangan pada kolom 'season' di hour_df
hour_df['season'] = hour_df['season'].map({    1: 'Spring',    2: 'Summer',    3: 'Fall',  4: 'Winter'})
# Mengganti angka menjadi keterangan pada kolom 'weekday' di day_df
day_df['weekday'] = day_df['weekday'].map({    0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday'})

# Mengganti angka menjadi keterangan pada kolom 'weekday' di hour_df
hour_df['weekday'] = hour_df['weekday'].map({ 0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'})
# Mengganti angka menjadi keterangan pada kolom 'weathersit' di day_df
day_df['weathersit'] = day_df['weathersit'].map({ 1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'})

# Mengganti angka menjadi keterangan pada kolom 'weathersit' di hour_df
hour_df['weathersit'] = hour_df['weathersit'].map({ 1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'})

# Mengganti angka menjadi keterangan pada kolom 'year' di day_df
day_df['yr'] = day_df['yr'].map({ 0: '2011', 1: '2012'})

# Mengganti angka menjadi keterangan pada kolom 'year' di hour_df
hour_df['yr'] = hour_df['yr'].map({ 0: '2011', 1: '2012'})

# Mengganti angka menjadi keterangan pada kolom 'month' di day_df
day_df['mnth'] = day_df['mnth'].map({  1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',7: 'July',  8: 'August', 9: 'September', 10: 'October', 11: 'November',  12: 'December'})

# Mengganti angka menjadi keterangan pada kolom 'month' di hour_df
hour_df['mnth'] = hour_df['mnth'].map({ 1: 'January', 2: 'February',3: 'March',4: 'April',5: 'May',6: 'June',7: 'July',8: 'August',9: 'September',10: 'October',11: 'November',12: 'December'})

# Mengganti 'workingday' menjadi 'hari kerja' dan 'hari libur' di day_df
day_df['workingday'] = day_df['workingday'].map({0: 'hari libur/weekend', 1: 'hari kerja'})

# Mengganti 'workingday' menjadi 'hari kerja' dan 'hari libur' di hour_df
hour_df['workingday'] = hour_df['workingday'].map({0: 'hari libur/weekend', 1: 'hari kerja'})

# Mengganti 'holiday' menjadi 'libur' dan 'tidak libur' di day_df
day_df['holiday'] = day_df['holiday'].map({0: 'tidak libur', 1: 'libur'})

# Mengganti 'holiday' menjadi 'libur' dan 'tidak libur' di hour_df
hour_df['holiday'] = hour_df['holiday'].map({0: 'tidak libur', 1: 'libur'})

# --- Dashboard Title ---
st.title("Bike Sharing Dataset Analysis Dashboard")

# Sidebar with options
st.sidebar.title("Bike Sharing Dashboard")
selected_analysis = st.sidebar.selectbox("Pilih Analisis", ["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3", "Pertanyaan 4", "Pertanyaan 5", "Analisis Lanjutan"])



if selected_analysis == "Pertanyaan 1":
    st.header("Pola Penggunaan Sepeda pada Hari Kerja vs Akhir Pekan")

    # Visualisasi dengan Barplot (copy from your existing code)
    st.subheader("Jumlah Peminjaman Sepeda Berdasarkan Hari Kerja")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='workingday', y='cnt', data=day_df, errorbar=None, ax=ax)
    plt.xlabel('Working Day')
    plt.ylabel('Count')
    plt.title('Jumlah Peminjaman Sepeda Berdasarkan Hari Kerja')
    st.pyplot(fig)

    st.subheader("Jumlah Peminjaman Sepeda Berdasarkan Hari Libur")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='holiday', y='cnt', data=day_df, errorbar=None, ax=ax)
    plt.xlabel('Holiday')
    plt.ylabel('Count')
    plt.title('Jumlah Peminjaman Sepeda Berdasarkan Hari Libur')
    st.pyplot(fig)

    st.write("**Kesimpulan:**")
    st.write("- Jumlah pengguna sepeda pada hari kerja lebih banyak daripada hari weekend.")
    st.write("- Jumlah pengguna sepeda pada hari libur nasional lebih sedikit daripada hari biasa.")


elif selected_analysis == "Pertanyaan 2":
    st.header("Perbedaan Signifikan dalam Jumlah Penyewaan Sepeda (Casual vs Registered)")

    # Visualisasi dengan Pie Chart (copy from your existing code)
    total_users = hour_df['casual'].sum() + hour_df['registered'].sum()
    casual_percentage = (hour_df['casual'].sum() / total_users) * 100
    registered_percentage = (hour_df['registered'].sum() / total_users) * 100

    labels = ['Casual', 'Registered']
    sizes = [casual_percentage, registered_percentage]
    colors = ['lightcoral', 'lightskyblue']
    explode = (0.1, 0)

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Persentase Penggunaan Sepeda Berdasarkan Tipe Pengguna')
    plt.axis('equal')
    st.pyplot(fig)

    st.write("**Kesimpulan:**")
    st.write("- Pengguna terdaftar jauh lebih banyak daripada pengguna kasual.")
    st.write("- Ini menunjukkan bahwa program penyewaan sepeda telah berhasil menarik minat pengguna untuk berlangganan secara reguler.")


elif selected_analysis == "Pertanyaan 3":
    st.header("Pengaruh Cuaca Ekstrem terhadap Jumlah Penyewaan Sepeda")

    # Visualisasi dengan Barplot (copy from your existing code)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', hue='weathersit', data=hour_df, estimator=sum, errorbar=None, palette='Set2', ax=ax)
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Total Penggunaan Sepeda')
    plt.title('Total Penggunaan Sepeda Berdasarkan Kondisi Cuaca')
    st.pyplot(fig)

    st.write("**Kesimpulan:**")
    st.write("- Jumlah total penggunaan sepeda paling tinggi pada cuaca cerah.")
    st.write("- Jumlah total penggunaan sepeda paling rendah pada cuaca hujan lebat/salju.")
    st.write("- Ini menunjukkan bahwa cuaca memiliki pengaruh yang signifikan terhadap minat masyarakat untuk menggunakan sepeda.")


elif selected_analysis == "Pertanyaan 4":
    st.header("Tren Musiman Penggunaan Sepeda Sepanjang Tahun")

    # Visualisasi dengan Lineplot (copy from your existing code)
    day_df['year_month'] = day_df['dteday'].dt.strftime('%Y-%m')
    monthly_trend = day_df.groupby('year_month')['cnt'].sum()

    fig, ax = plt.subplots(figsize=(12, 6))
    plt.plot(monthly_trend.index, monthly_trend.values)
    plt.xlabel('Bulan dan Tahun')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.title('Tren Bulanan Penyewaan Sepeda')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(fig)

    st.write("**Kesimpulan:**")
    st.write("- Terdapat tren peningkatan jumlah penyewaan sepeda dari tahun 2011 hingga 2012.")
    st.write("- Pada beberapa bulan, jumlah penyewaan cenderung lebih tinggi (Mei-Oktober).")
    st.write("- Pada bulan-bulan lain (November-Februari), jumlah penyewaan cenderung lebih rendah.")


elif selected_analysis == "Pertanyaan 5":
    st.header("Pengaruh Suhu, Kecepatan Angin, dan Kelembapan terhadap Keputusan Sewa Sepeda")

    # Visualisasi dengan Heatmap (copy from your existing code)
    correlation_matrix = day_df[['temp', 'windspeed', 'hum', 'cnt']].corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.title('Korelasi antara Suhu, Kecepatan Angin, Kelembapan, dan Jumlah Penyewaan')
    st.pyplot(fig)

    st.write("**Kesimpulan:**")
    st.write("- Suhu memiliki korelasi positif yang kuat dengan jumlah penyewaan.")
    st.write("- Kecepatan angin dan kelembapan memiliki korelasi negatif lemah dengan jumlah penyewaan.")


elif selected_analysis == "Analisis Lanjutan":
    st.header("Analisis Lanjutan")

    # Analisis Clustering (copy from your existing code)
    weather_analysis = hour_df.groupby('weathersit').agg({
        'cnt': ['nunique', 'min', 'max', 'mean', 'median', 'std']
    })
    st.write(weather_analysis)

    st.write("**Kesimpulan:**")
    st.write("- Cuaca cerah memiliki rata-rata jumlah penyewaan tertinggi.")
    st.write("- Cuaca buruk memiliki rata-rata jumlah penyewaan terendah.")


# You can add more analyses and visualizations based on your needs.
