import streamlit as st

# Display the introduction
st.title("Project Documentation: Sales Insights and Analytics Dashboard")

st.markdown("""
### Introduction

Welcome to the Sales Insights and Analytics Dashboard. This application is designed to provide in-depth analysis and insights from your sales data using the refined Gold Layer of our multi-layered architecture. The Gold Layer represents the final, polished dataset, optimized for detailed querying and analytics.

### Gold Layer Overview

The Gold Layer consists of the most refined and processed data, ready for analysis. It includes:

- **items Table**: Final item data with update timestamps.
- **locations Table**: Processed location data with update timestamps.
- **customers Table**: Finalized customer data with timestamps.
- **sales Table**: Refined sales transaction data with detailed metrics.

### Analytics Capabilities

The **Insights & Analytics** section of the dashboard provides various predefined queries to explore key business insights from the Gold Layer data:

- **Total Sales by Category**: View total sales amounts for each product category.
- **Top 10 Best-Selling Items**: Identify the top 10 items based on quantity sold.
- **Monthly Sales Trend**: Analyze sales trends on a monthly basis for the past year.
- **Sales by Location**: Determine total sales revenue for each location.
- **Customer Purchase Frequency**: Find out how often customers make purchases.
- **Average Order Value (AOV)**: Calculate the average order value for different locations.
- **Revenue by Membership Status**: Assess revenue based on customer membership status (Regular, Silver, Gold).
- **Product Performance in Locations**: Analyze how each product performs across various locations.
- **Customer Retention Analysis**: Identify customers who made purchases in both halves of the year.
- **Promotion Effectiveness**: Compare sales during promotional periods with non-promotional periods.

### Using the App

1. **View Gold Layer Data**: The app exclusively uses data from the Gold Layer for analysis.
2. **Select and Run Queries**: Choose a query from the dropdown menu in the Insights & Analytics section to generate specific insights.
3. **Analyze Results**: Review the results to gain valuable insights and make informed business decisions.

This dashboard is designed to offer a streamlined and intuitive experience for analyzing your sales data, focusing on the most refined and actionable insights available from the Gold Layer.
""")
