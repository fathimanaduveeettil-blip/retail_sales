# Retail Sales Analysis Dashboard

## Project Overview

This project analyzes retail sales data to identify business trends, customer behavior, product performance, and regional sales patterns. The project includes data cleaning, exploratory data analysis (EDA), KPI calculations, and an interactive Streamlit dashboard.

## Objectives

* Analyze monthly and yearly sales trends
* Identify top-performing product categories and subcategories
* Compare sales and profit across regions
* Calculate key business KPIs
* Build an interactive dashboard for business users

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly
* Streamlit
* Git & GitHub

## Dataset Features

The dataset contains:

* Order Information
* Customer Information
* Product Details
* Sales & Profit Metrics
* Regional Data
* Return Status

Key columns include:

* OrderDate
* CustomerName
* Region
* Category
* SubCategory
* Sales
* Profit
* Returned

## Analysis Performed

### Sales Analysis

* Monthly Sales Trend
* Year-over-Year Growth
* Sales by Region
* Sales by Category
* Sales by Subcategory

### KPI Analysis

* Total Revenue
* Total Profit
* Profit Margin
* Average Order Value (AOV)
* Top 10 Customers
* Return Rate
* Repeat Customer Rate

## Dashboard Features

### KPI Cards

* Revenue
* Profit
* Orders
* Average Order Value

### Interactive Filters

* Date Range
* Region
* Category
* Segment

### Visualizations

* Monthly Sales Trend
* Sales by Category
* Top Customers
* Region Comparison

### Data Table

* Dynamically updates based on selected filters

## Project Structure

Retail_Sales_Project/

├── retail_sales_cleaned.csv

├── Retail_Sales_Analysis.ipynb

├── app.py

├── README.md

├── Retail_Sales_Report.pdf

└── Retail_Sales_Presentation.pptx

## Running the Dashboard

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd retail-sales-dashboard
```

3. Install required packages

```bash
pip install pandas streamlit plotly matplotlib
```

4. Run the dashboard

```bash
python -m streamlit run app.py
```

5. Open the local URL displayed in the terminal.

## Key Insights

1. Technology products generate the highest revenue.
2. Sales peak during November and December, showing seasonal demand.
3. Laptops and Smartphones are the top-selling subcategories.
4. Revenue is distributed across multiple customers, reducing customer concentration risk.
5. Regional sales performance is relatively balanced.

## Recommendations

1. Increase inventory for high-performing technology products.
2. Prepare marketing campaigns before peak holiday seasons.
3. Strengthen customer loyalty programs to improve retention and repeat purchases.

## Author

Fathima Fidha

## License

This project is developed for educational and academic purposes.
