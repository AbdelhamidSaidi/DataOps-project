import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px


# Note: run this app with `streamlit run app.py` to view in the browser.


st.set_page_config(page_title="DataOps Dashboard", layout="wide")

st.title("📊 DataOps Sales Dashboard")

# Prefer processed output but fall back to raw data and apply a minimal
# transformation so the dashboard can render without running the full ETL.
processed_path = "data/processed_data.csv"
raw_path = "data/raw_data.csv"

if os.path.exists(processed_path):
    df = pd.read_csv(processed_path)
elif os.path.exists(raw_path):
    st.info("Using raw data and applying basic transform (dropna, compute total).")
    df = pd.read_csv(raw_path)
    df = df.dropna()
    if "total" not in df.columns:
        df["total"] = df["quantity"] * df["price"]
else:
    st.warning("Processed data not found. Run the pipeline first.")
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Select Product Category",
    options=df["product_category"].unique(),
    default=df["product_category"].unique()
)

filtered_df = df[df["product_category"].isin(category_filter)]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${filtered_df['total'].sum():,.2f}")
col2.metric("Total Quantity", f"{filtered_df['quantity'].sum():,}")
col3.metric("Average Price", f"${filtered_df['price'].mean():,.2f}")

# Plotly Interactive Chart
fig = px.scatter(
    filtered_df,
    x="quantity",
    y="price",
    color="product_category",
    title="Quantity vs Price"
)

st.plotly_chart(fig, use_container_width=True)

# Bar chart
category_sales = (
    filtered_df.groupby("product_category")["total"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_bar = px.bar(
    category_sales,
    x="product_category",
    y="total",
    title="Total Sales by Category"
)

st.plotly_chart(fig_bar, use_container_width=True)
