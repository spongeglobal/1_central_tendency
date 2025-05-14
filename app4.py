import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Visualization with Statistics", layout="centered")
st.title("Data Visualization & Statistics")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file with numeric columns", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if numeric_columns:
        selected_column = st.selectbox("Select a numeric column to analyze", numeric_columns)
        data = df[selected_column]

        st.subheader(f"Descriptive Statistics for: {selected_column}")
        st.write(f"**Mean:** {data.mean():.2f}")
        st.write(f"**Median (50th percentile):** {data.median():.2f}")
        st.write(f"**Mode:** {data.mode().tolist()}")
        st.write(f"**Standard Deviation:** {data.std():.2f}")
        st.write(f"**IQR (Q3 - Q1):** {(data.quantile(0.75) - data.quantile(0.25)):.2f}")

        # Display percentiles
        st.subheader("📐 Percentile Values")
        percentiles = [0.1, 0.25, 0.5, 0.75, 0.9]
        for p in percentiles:
            st.write(f"{int(p*100)}th percentile: {data.quantile(p):.2f}")

        # Histogram
        st.subheader("📊 Frequency Distribution (Histogram)")
        fig1, ax1 = plt.subplots()
        sns.histplot(data, bins=10, kde=True, ax=ax1, color='skyblue')
        ax1.set_title(f"Histogram of {selected_column}")
        st.pyplot(fig1)

        # Boxplot
        st.subheader("📈 Box-and-Whisker Plot")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x=data, ax=ax2, color='orange')
        ax2.set_title(f"Boxplot of {selected_column}")
        st.pyplot(fig2)

    else:
        st.warning("The uploaded file has no numeric columns.")