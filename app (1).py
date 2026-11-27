
import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="GridMind AI",
    page_icon="⚡",
    layout="wide"
)

# Load Dataset
DATA_PATH = "gridmind_hourly.parquet"

@st.cache_data
def load_data():
    data = pd.read_parquet(DATA_PATH)
    data["datetime"] = pd.to_datetime(data["datetime"])
    return data

df = load_data()

# Dashboard Design
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: white;
}
[data-testid="stMetric"] {
    background-color: #17243a;
    padding: 18px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("⚡ GridMind AI")
st.subheader("Electricity Consumption Analysis & Demand Forecasting")
st.caption("Intelligent Energy Analytics | Pakistan")

st.divider()

# Sidebar Filters
st.sidebar.title("Dashboard Filters")

cities = ["All Cities"] + sorted(df["city"].dropna().unique().tolist())

selected_city = st.sidebar.selectbox(
    "Select City",
    cities
)

# Filter Data
filtered_df = df.copy()

if selected_city != "All Cities":
    filtered_df = filtered_df[
        filtered_df["city"] == selected_city
    ]

# KPI Calculations
total_records = len(filtered_df)
total_households = filtered_df[
    ["city", "house_no"]
].drop_duplicates().shape[0]

average_usage = filtered_df["usage_kw"].mean()
maximum_usage = filtered_df["usage_kw"].max()

# KPI Cards
st.subheader("Energy Consumption Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Records", f"{total_records:,}")
c2.metric("Households", f"{total_households:,}")
c3.metric("Average Usage", f"{average_usage:.3f} kW")
c4.metric("Maximum Usage", f"{maximum_usage:.3f} kW")

st.divider()

# City Analysis
st.subheader("City-Wise Electricity Consumption")

city_data = (
    filtered_df.groupby("city")["usage_kw"]
    .mean()
    .reset_index()
)

fig1 = px.bar(
    city_data,
    x="city",
    y="usage_kw",
    color="city",
    title="Average Electricity Usage by City",
    labels={
        "city": "City",
        "usage_kw": "Average Usage (kW)"
    },
    template="plotly_dark"
)

st.plotly_chart(fig1, use_container_width=True)

# Hourly Analysis
st.subheader("Hourly Consumption Pattern")

hourly_data = (
    filtered_df.groupby(filtered_df["datetime"].dt.hour)["usage_kw"]
    .mean()
    .reset_index()
)

hourly_data.columns = ["Hour", "Average Usage"]

fig2 = px.line(
    hourly_data,
    x="Hour",
    y="Average Usage",
    markers=True,
    title="Average Electricity Usage by Hour",
    template="plotly_dark"
)

st.plotly_chart(fig2, use_container_width=True)

# Monthly Analysis
st.subheader("Monthly Electricity Consumption")

monthly_data = (
    filtered_df.groupby(filtered_df["datetime"].dt.to_period("M"))["usage_kw"]
    .mean()
    .reset_index()
)

monthly_data["Month"] = monthly_data["datetime"].astype(str)

fig3 = px.line(
    monthly_data,
    x="Month",
    y="usage_kw",
    markers=True,
    title="Monthly Average Electricity Usage",
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

# Footer
st.divider()

st.caption(
    "GridMind AI | Electricity Consumption Analysis "
    "& Demand Forecasting | Data Science Project"
)
