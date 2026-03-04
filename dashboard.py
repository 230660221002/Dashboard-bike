import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
sns.set_style("whitegrid")

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Load dataset
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "main_data.csv")

df = pd.read_csv(DATA_PATH)
df['dteday'] = pd.to_datetime(df['dteday'])

st.title("🚲 Bike Sharing Data Dashboard")

st.markdown("Dashboard ini menampilkan analisis penggunaan layanan bike sharing berdasarkan musim, cuaca, dan waktu.")

# ========================
# SIDEBAR FILTER
# ========================

st.sidebar.header("Filter Data")

# Filter tanggal
date_range = st.sidebar.date_input(
    "Rentang Tanggal",
    [df['dteday'].min(), df['dteday'].max()]
)

# Filter musim
season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    options=df['season'].unique(),
    default=df['season'].unique()
)

# Filter cuaca
weather_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=df['weathersit'].unique(),
    default=df['weathersit'].unique()
)

# Filter data
filtered_df = df[
    (df['dteday'] >= pd.to_datetime(date_range[0])) &
    (df['dteday'] <= pd.to_datetime(date_range[1])) &
    (df['season'].isin(season_filter)) &
    (df['weathersit'].isin(weather_filter))
]

# ========================
# KPI
# ========================

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rental", int(filtered_df['cnt'].sum()))
col2.metric("Rata-rata Harian", round(filtered_df['cnt'].mean(),2))
col3.metric("Rental Tertinggi", int(filtered_df['cnt'].max()))

st.markdown("---")

# ========================
# VISUALISASI 1
# Rental per musim
# ========================

st.subheader("Rata-rata Penyewaan Berdasarkan Musim")

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.boxplot(data=filtered_df, x="season", y="cnt", ax=ax1)

ax1.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
ax1.set_xlabel("Musim")
ax1.set_ylabel("Jumlah Rental")

st.pyplot(fig1)

# ========================
# VISUALISASI 2
# Tren waktu
# ========================

st.subheader("Tren Penyewaan Sepeda")

fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(filtered_df['dteday'], filtered_df['cnt'])
ax2.set_xlabel("Tanggal")
ax2.set_ylabel("Jumlah Rental")

st.pyplot(fig2)

# ========================
# VISUALISASI 3
# Cuaca
# ========================

st.subheader("Pengaruh Cuaca terhadap Penyewaan")

fig3, ax3 = plt.subplots(figsize=(8,5))
sns.boxplot(data=filtered_df, x="weathersit", y="cnt", ax=ax3)

ax3.set_title("Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
ax3.set_xlabel("Kondisi Cuaca")
ax3.set_ylabel("Jumlah Rental")

st.pyplot(fig3)

# ========================
# VISUALISASI 4
# Distribusi demand
# ========================

st.subheader("Distribusi Kategori Permintaan")

filtered_df = filtered_df.copy()

filtered_df["demand_category"] = pd.qcut(
    filtered_df["cnt"],
    q=3,
    labels=["Low", "Medium", "High"]
)

fig4, ax4 = plt.subplots()
sns.countplot(data=filtered_df, x="demand_category", ax=ax4)

st.pyplot(fig4)
