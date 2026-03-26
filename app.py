import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Page Title
st.set_page_config(page_title="Real-Time Dashboard", layout="wide")
st.title("Real-Time Data Dashboard")

# Sidebar
st.sidebar.header("Settings")
num_points = st.sidebar.slider("Number of Data Points", 10, 200, 50)

# Create placeholder
placeholder = st.empty()

# Generate real-time data
data = pd.DataFrame({
    "Time": pd.date_range(start="2024-01-01", periods=num_points, freq="S"),
    "Value": np.random.randn(num_points).cumsum()
})

# Real-time update loop
for i in range(50):
    new_row = pd.DataFrame({
        "Time": [pd.Timestamp.now()],
        "Value": [data["Value"].iloc[-1] + np.random.randn()]
    })

    data = pd.concat([data, new_row], ignore_index=True)

    with placeholder.container():
        col1, col2 = st.columns(2)

        # Line Chart
        with col1:
            st.subheader(" Live Line Chart")
            st.line_chart(data.set_index("Time"))

        # Bar Chart
        with col2:
            st.subheader(" Bar Chart")
            st.bar_chart(data["Value"].tail(10))

        # Data Table
        st.subheader("Data Table")
        st.dataframe(data.tail(10))

    time.sleep(1)