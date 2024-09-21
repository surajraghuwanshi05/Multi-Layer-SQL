import streamlit as st
import mysql.connector
import pandas as pd
from query import *
from bronze import create_connection

# # Set up MySQL connection
# def create_connection():
#     return mysql.connector.connect(
#         host="localhost",    # e.g., "localhost"
#         user="root",    # e.g., "root"
#         password="suraj@123",  # Your MySQL password
#         database="test"  # Your database name
#     )

conn = create_connection()

st.markdown("""
### Insights & Analytics

This section allows you to explore various insights and analytics from the sales data. Using predefined queries, you can uncover important business trends, product performance, customer behavior, and sales patterns across different locations.

Select a query from the dropdown menu to gain valuable insights and make data-driven decisions.
""")

# Function to execute a query and return results as a DataFrame
def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return pd.DataFrame(result, columns=columns)



st.title("Sales & Customer Analytics")

# Select an analysis
analysis = st.selectbox(
    "Choose an analysis",
    [
        "Total Sales by Category",
        "Top 10 Best-Selling Items",
        "Monthly Sales Trend",
        "Sales by Location",
        "Customer Purchase Frequency",
        "Average Order Value by Location",
        "Revenue Contribution by Membership Status",
        "Product Performance in Different Locations",
        "Customer Retention Analysis",
        "Promotion Effectiveness"
    ]
)

if st.button("show Dashboard"):
    # Run the selected analysis
    if analysis == "Total Sales by Category":
        result = total_sales_by_category()
        st.dataframe(result)

    elif analysis == "Top 10 Best-Selling Items":
        result = top_10_best_selling_items()
        st.dataframe(result)


    elif analysis == "Monthly Sales Trend": 
        result = monthly_sales_trend()
        st.dataframe(result)


    elif analysis == "Sales by Location":
        result = sales_by_location()
        st.dataframe(result)


    elif analysis == "Customer Purchase Frequency":
        result = customer_purchase_frequency()
        st.dataframe(result)

        
    elif analysis == "Average Order Value by Location": 
        result = monthly_sales_trend()
        st.dataframe(result)

    elif analysis == "Revenue Contribution by Membership Status":
        result = revenue_contribution_by_membership_status()
        st.dataframe(result)


    elif analysis == "Product Performance in Different Locations":
        result = product_performance_by_location()
        st.dataframe(result)


    elif analysis == "Customer Retention Analysis": 
        result = customer_retention_analysis()
        st.dataframe(result)

    elif analysis == "Promotion Effectiveness":
        
        result = promotion_effectiveness()
        st.dataframe(result)
    # Continue adding more queries for other analyses

# Close connection at the end
conn.close()
