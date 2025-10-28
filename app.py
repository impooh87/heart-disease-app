import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the page
st.set_page_config(page_title="Heart Disease Risk Analysis", layout="wide")

# Title and description
st.title("💓 Heart Disease Risk Analysis")
st.write("Upload a dataset to explore patterns, visualize trends, and understand risk factors.")

# File uploader
uploaded_file = st.file_uploader("📁 Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Preview data
    st.subheader("🔍 Preview of Your Data")
    st.dataframe(df.head())

    # Show column names
    st.subheader("📊 Column Names")
    st.write(df.columns.tolist())

    # Select outcome column
    outcome_column = st.selectbox("🎯 Select the outcome column", df.columns)

    # Outcome distribution
    st.subheader("📈 Outcome Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(x=outcome_column, data=df, ax=ax1)
    ax1.set_title(f"Distribution of {outcome_column}")
    st.pyplot(fig1)

    # Feature comparison
    st.subheader("📉 Feature Comparison")
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    x_axis = st.selectbox("Select X-axis feature", numeric_columns, index=0)
    y_axis = st.selectbox("Select Y-axis feature", numeric_columns, index=1)

    fig2, ax2 = plt.subplots()
    sns.scatterplot(x=x_axis, y=y_axis, hue=outcome_column, data=df, ax=ax2)
    ax2.set_title(f"{x_axis} vs {y_axis} by {outcome_column}")
    st.pyplot(fig2)

    # Summary statistics
    st.subheader("📋 Summary Statistics")
    st.dataframe(df.describe())

    # Correlation heatmap (numeric only)
    st.subheader("📌 Correlation Heatmap")
    numeric_df = df.select_dtypes(include='number')
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax3)
    st.pyplot(fig3)

    # Filter by feature
    st.subheader("📎 Filter by Feature")
    filter_column = st.selectbox("Select a column to filter", df.columns)
    unique_values = df[filter_column].unique()
    selected_value = st.selectbox(f"Select a value from {filter_column}", unique_values)
    filtered_df = df[df[filter_column] == selected_value]
    st.write(f"Filtered data where `{filter_column}` = `{selected_value}`:")
    st.dataframe(filtered_df)

