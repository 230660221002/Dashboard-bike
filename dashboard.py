import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Load data
df = pd.read_csv("main_data.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

st.title("Bike Sharing Data Dashboard")

# Sidebar filter
st.sidebar.header("Filter Data")

selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=df['season'].unique(),
    default=df['season'].unique()
)

filtered_df = df[df['season'].isin(selected_season)]

# KPI
col1, col2, col3 = st.columns(3)

col1.metric("Total Rental", int(filtered_df['cnt'].sum()))
col2.metric("Rata-rata Harian", round(filtered_df['cnt'].mean(), 2))
col3.metric("Rental Tertinggi", int(filtered_df['cnt'].max()))

st.markdown("---")

# Visualisasi 1
st.subheader("Rata-rata Rental per Musim")
season_avg = filtered_df.groupby("season")["cnt"].mean()

fig1, ax1 = plt.subplots()
season_avg.plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# Visualisasi 2
st.subheader("Tren Rental Harian")

fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(filtered_df['dteday'], filtered_df['cnt'])
ax2.set_xlabel("Tanggal")
ax2.set_ylabel("Jumlah Rental")
st.pyplot(fig2)

# Visualisasi 3
st.subheader("Distribusi Kategori Permintaan")

filtered_df = filtered_df.copy()
filtered_df['demand_category'] = pd.qcut(
    filtered_df['cnt'],
    q=3,
    labels=["Low", "Medium", "High"]
)

fig3, ax3 = plt.subplots()
sns.countplot(data=filtered_df, x="demand_category", ax=ax3)
st.pyplot(fig3)
