import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Advanced Sales Dashboard", layout="wide")

st.title("📊 Advanced Sales Data Dashboard (NumPy + Pandas)")

# Load data
@st.cache_data
def load_data():
    sales_df = pd.read_json('sales-data.json')
    customers_df = pd.read_csv('customers.csv')
    df = pd.merge(sales_df, customers_df, on='order_id')
    df['total_amount'] = df['price'] * df['quantity']

    # NumPy Feature: Discount Calculation (vectorized)
    conditions = [
        df['total_amount'] > 50000,
        df['total_amount'] > 20000
    ]
    choices = [0.20, 0.10]

    df['discount'] = np.select(conditions, choices, default=0.05)
    df['final_amount'] = df['total_amount'] - (df['total_amount'] * df['discount'])

    return df


df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")
city_filter = st.sidebar.multiselect("Select City", df['city'].unique(), default=df['city'].unique())
category_filter = st.sidebar.multiselect("Select Category", df['category'].unique(), default=df['category'].unique())

# Search + Value Filter
search_value = st.sidebar.text_input("🔎 Search (Product/Customer/City)")

min_val, max_val = int(df['final_amount'].min()), int(df['final_amount'].max())
value_range = st.sidebar.slider("💰 Filter by Final Amount", min_val, max_val, (min_val, max_val))

filtered_df = df[(df['city'].isin(city_filter)) & (df['category'].isin(category_filter))]

# Apply search
if search_value:
    filtered_df = filtered_df[
        filtered_df['product'].str.contains(search_value, case=False) |
        filtered_df['customer_name'].str.contains(search_value, case=False) |
        filtered_df['city'].str.contains(search_value, case=False)
    ]

# Apply value filter
filtered_df = filtered_df[
    (filtered_df['final_amount'] >= value_range[0]) &
    (filtered_df['final_amount'] <= value_range[1])
]

# Sorting
sort_option = st.sidebar.selectbox("Sort By", ['final_amount', 'price', 'quantity'])
filtered_df = filtered_df.sort_values(by=sort_option, ascending=False)

# KPIs using NumPy
st.subheader("📌 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{np.sum(filtered_df['final_amount']):,.0f}")
col2.metric("Average Order Value", f"₹{np.mean(filtered_df['final_amount']):,.0f}")
col3.metric("Max Order", f"₹{np.max(filtered_df['final_amount']):,.0f}")
col4.metric("Min Order", f"₹{np.min(filtered_df['final_amount']):,.0f}")

# Top Products (No Matplotlib)
st.subheader("🏆 Top Products")
top_products = (
    filtered_df.groupby('product')['final_amount']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
st.bar_chart(top_products)

# Category Sales
st.subheader("📦 Category-wise Sales")
category_sales = filtered_df.groupby('category')['final_amount'].sum()
st.bar_chart(category_sales)

# NumPy Insight
st.subheader("🧠 NumPy Insights")
values = filtered_df['final_amount'].values

st.write("Standard Deviation:", np.std(values))
st.write("Median Value:", np.median(values))
st.write("90th Percentile:", np.percentile(values, 90))

# High Value Orders
st.subheader("💰 High Value Orders (> ₹20,000)")
high_value = filtered_df[filtered_df['final_amount'] > 20000]
st.dataframe(high_value)

# Data Table
st.subheader("📋 Full Data")
st.dataframe(filtered_df)

# Download
st.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name='advanced_sales_numpy.csv',
    mime='text/csv'
)

st.success("Dashboard with NumPy Loaded 🚀")