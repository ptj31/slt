# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="My Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- SIDEBAR --------------------
st.sidebar.title("Dashboard Controls")
selected_option = st.sidebar.selectbox("Select View", ["Overview", "Analysis", "Settings"])
show_data = st.sidebar.checkbox("Show Raw Data", value=True)

# -------------------- MAIN CONTENT --------------------
st.title("📊 Streamlit Dashboard Template")

# Sample data generator
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=100)
    values = np.random.randn(100).cumsum()
    df = pd.DataFrame({"Date": dates, "Value": values})
    return df

df = load_data()

# Conditional display of raw 


if show_data:
    st.subheader("Raw Data")
    st.dataframe(df)

# Line chart section
st.subheader("Time Series Chart")
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Value"], label="Sample Data")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.set_title("Sample Time Series")
ax.grid(True)
st.pyplot(fig)

# Add content based on selection
if selected_option == "Overview":
    st.markdown("### Overview section here.")
elif selected_option == "Analysis":
    st.markdown("### Deeper analysis can go here.")
elif selected_option == "Settings":
    st.markdown("### Settings configuration can go here.")
