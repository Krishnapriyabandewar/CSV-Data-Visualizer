import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Data Visualizer")

# Upload CSV file
uploaded_file = st.file_uploader(r"C:\Users\Krishnapriya\Desktop\streamlit_csv_visualizer\gender_submission.csv", type=["csv"])


if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data", df.head())

    # Chart selection
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

    # Select column(s)
    if chart_type in ["Line Chart", "Bar Chart"]:
        column = st.selectbox("Select a Column", df.columns)

        # Display chart
        if chart_type == "Line Chart":
            st.line_chart(df[column])
        elif chart_type == "Bar Chart":
            st.bar_chart(df[column])
    elif chart_type == "Histogram":
        column = st.selectbox("Select a Column", df.columns)
        bins = st.slider("Number of bins", 5, 50, 10)

        # Plot histogram
        plt.hist(df[column], bins=bins)
        st.pyplot(plt)
