# Bike Sharing Data Analysis

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan **Bike Sharing Dataset**. Analisis dilakukan untuk memahami bagaimana faktor seperti musim, kondisi cuaca, dan waktu mempengaruhi jumlah penyewaan sepeda.

Hasil analisis disajikan dalam bentuk **Exploratory Data Analysis (EDA)**, visualisasi data, serta **dashboard interaktif menggunakan Streamlit**.

---

# Business Questions

1. Bagaimana pengaruh musim dan kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Bagaimana pola penyewaan sepeda berdasarkan waktu?

---

# Project Structure

```
submission
│
├── dashboard
│   ├── dashboard.py
│   └── main_data.csv
│
├── data
│   ├── day.csv
│   └── hour.csv
│
├── notebook.ipynb
├── requirements.txt
└── README.md
```

Keterangan:

* **notebook.ipynb** : berisi proses analisis data lengkap mulai dari EDA hingga visualisasi.
* **data/** : berisi dataset asli yang digunakan dalam analisis.
* **dashboard/** : berisi aplikasi dashboard interaktif menggunakan Streamlit.
* **requirements.txt** : daftar library yang dibutuhkan untuk menjalankan proyek.

---

# Setup Environment

Pastikan Python sudah terinstall di komputer. Disarankan menggunakan Python versi 3.9 atau lebih baru.

### 1. Clone repository atau download project

```
git clone (https://github.com/230660221002/Dashboard-bike.git)
```

atau download file project secara langsung.

---

### 2. Membuat Virtual Environment (Opsional)

Virtual environment digunakan untuk mengisolasi dependencies project.

```
python -m venv venv
```

Aktifkan virtual environment.

Windows:

```
venv\Scripts\activate
```

MacOS / Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

Install semua library yang dibutuhkan menggunakan file requirements.txt.

```
pip install -r requirements.txt
```

---

# Menjalankan Dashboard

Masuk ke folder dashboard:

```
cd dashboard
```

Jalankan aplikasi Streamlit:

```
streamlit run dashboard.py
```

Setelah dijalankan, dashboard akan otomatis terbuka di browser pada alamat:

```
http://localhost:8501
```

Dashboard ini menyediakan beberapa fitur seperti:

* Filter rentang tanggal
* Filter musim
* Filter kondisi cuaca
* Visualisasi distribusi penyewaan sepeda
* Tren penyewaan berdasarkan waktu

---

# Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset**, yang berisi informasi penyewaan sepeda berdasarkan waktu, musim, kondisi cuaca, serta beberapa variabel lingkungan lainnya.

Dataset terdiri dari dua file utama:

* **day.csv** : data agregasi penyewaan sepeda per hari
* **hour.csv** : data agregasi penyewaan sepeda per jam

---

# Libraries Used

Beberapa library Python yang digunakan dalam proyek ini antara lain:

* pandas
* numpy
* matplotlib
* seaborn
* streamlit

---

# Author

Galih Permana Sidik
