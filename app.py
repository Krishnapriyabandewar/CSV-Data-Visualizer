import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the application
st.title("CSV Data Visualizer")

# Upload CSV file
uploaded_file = st.file_uploader(r"C:\Users\Krishnapriya\Desktop\streamlit_csv_visualizer\gender_submission.csv", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data", df.head())

    # Chart selection
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

    # Ensure DataFrame is not empty
    if not df.empty:
        if chart_type in ["Line Chart", "Bar Chart"]:
            # Allow user to select a column
            column = st.selectbox("Select a Column", df.select_dtypes(include=['float', 'int', 'object']).columns)
            if df[column].dtype == 'object':
                st.error("Selected column contains non-numeric data. Cannot generate chart.")
            else:
                # Generate the appropriate chart
                if chart_type == "Line Chart":
                    st.line_chart(df[column])
                elif chart_type == "Bar Chart":
                    st.bar_chart(df[column])
        elif chart_type == "Histogram":
            # Allow user to select a column and number of bins
            column = st.selectbox("Select a Column", df.select_dtypes(include=['float', 'int']).columns)
            bins = st.slider("Number of bins", 5, 50, 10)

            # Plot histogram
            plt.figure(figsize=(8, 5))
            plt.hist(df[column], bins=bins, color="skyblue", edgecolor="black")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.title(f"Histogram of {column}")
            st.pyplot(plt)
    else:
        st.error("Uploaded file is empty.")
