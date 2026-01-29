import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------
# Page Configuration
# ----------------------
st.set_page_config(
    page_title="COVID-19 Dashboard",
    layout="wide"
)

# ----------------------
# Title
# ----------------------
st.title("🦠 COVID-19 Country Wise Dashboard")
st.markdown("COVID-19 data analysis using tables and visualizations")
st.markdown("---")

# ----------------------
# Load Dataset
# ----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("covid_data.csv")
    df[['Confirmed', 'Deaths', 'Recovered']] = df[['Confirmed', 'Deaths', 'Recovered']].fillna(0)
    return df

data = load_data()

# ----------------------
# Sidebar Filter
# ----------------------
st.sidebar.header("Filter Options")

countries = ["All"] + sorted(data["Country/Region"].unique())
selected_country = st.sidebar.selectbox("Select Country / Region", countries)

if selected_country != "All":
    filtered_data = data[data["Country/Region"] == selected_country]
else:
    filtered_data = data

# ----------------------
# Data Table
# ----------------------
st.subheader("📋 COVID-19 Data Table")
st.dataframe(filtered_data)

st.markdown("---")

# ----------------------
# Top 10 Countries Table
# ----------------------
st.subheader("🏆 Top 10 Countries by Confirmed Cases")

top10 = data.sort_values(by="Confirmed", ascending=False).head(10)
st.dataframe(top10)

st.markdown("---")

# ----------------------
# Bar Chart
# ----------------------
st.subheader("📊 COVID-19 Cases Comparison (Top 10)")

bar_fig = px.bar(
    top10,
    x="Country/Region",
    y=["Confirmed", "Deaths", "Recovered"],
    barmode="group",
    title="Confirmed vs Deaths vs Recovered"
)

st.plotly_chart(bar_fig, use_container_width=True)

st.markdown("---")

# ----------------------
# Line Chart
# ----------------------
st.subheader("📈 Confirmed vs Deaths Trend")

line_fig = px.line(
    top10,
    x="Country/Region",
    y=["Confirmed", "Deaths"],
    markers=True,
    title="Confirmed vs Deaths (Top 10 Countries)"
)

st.plotly_chart(line_fig, use_container_width=True)

