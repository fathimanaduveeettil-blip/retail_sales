import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Retail Sales Dashboard",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
sales = pd.read_csv("retail_sales_cleaned.csv")

sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title("📊 Retail Sales Dashboard")

# -------------------------------------------------
# SIDEBAR FILTERS
# -------------------------------------------------
st.sidebar.header("Filters")

# Date Filter
start_date = sales["OrderDate"].min().date()
end_date = sales["OrderDate"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [start_date, end_date]
)

# Region Filter
selected_region = st.sidebar.multiselect(
    "Region",
    sales["Region"].unique(),
    default=sales["Region"].unique()
)

# Category Filter
selected_category = st.sidebar.multiselect(
    "Category",
    sales["Category"].unique(),
    default=sales["Category"].unique()
)

# Segment Filter
selected_segment = st.sidebar.multiselect(
    "Segment",
    sales["Segment"].unique(),
    default=sales["Segment"].unique()
)

# -------------------------------------------------
# APPLY FILTERS
# -------------------------------------------------
filtered_df = sales[
    (sales["Region"].isin(selected_region)) &
    (sales["Category"].isin(selected_category)) &
    (sales["Segment"].isin(selected_segment))
]

if len(date_range) == 2:
    filtered_df = filtered_df[
        (filtered_df["OrderDate"] >= pd.to_datetime(date_range[0])) &
        (filtered_df["OrderDate"] <= pd.to_datetime(date_range[1]))
    ]

# -------------------------------------------------
# KPI CARDS
# -------------------------------------------------
revenue = filtered_df["Sales"].sum()
profit = filtered_df["Profit"].sum()
orders = filtered_df["OrderID"].nunique()
aov = revenue / orders if orders > 0 else 0

st.subheader("📌 Key Performance Indicators")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Revenue", f"${revenue:,.2f}")
kpi2.metric("Profit", f"${profit:,.2f}")
kpi3.metric("Orders", f"{orders:,}")
kpi4.metric("AOV", f"${aov:,.2f}")

st.divider()

# -------------------------------------------------
# PREPARE DATA
# -------------------------------------------------

# Monthly Sales Trend
monthly_sales = (
    filtered_df
    .groupby(filtered_df["OrderDate"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

# Sales by Category
category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Top Customers
top_customers = (
    filtered_df
    .groupby("CustomerName")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Region Comparison
region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# -------------------------------------------------
# ROW 1
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Monthly Sales Trend")
    st.line_chart(monthly_sales)

with col2:
    st.subheader("📊 Sales by Category")
    st.bar_chart(category_sales)

# -------------------------------------------------
# ROW 2
# -------------------------------------------------
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏆 Top 10 Customers")
    st.bar_chart(top_customers)

with col4:
    st.subheader("🌍 Region Comparison")
    st.bar_chart(region_sales)

# -------------------------------------------------
# DATA TABLE
# -------------------------------------------------
st.divider()

st.subheader("📋 Filtered Data")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)