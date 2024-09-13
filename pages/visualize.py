import streamlit as st
import mysql.connector
import pandas as pd
from query import *

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

This section allows you to explore various insights and analytics from the sales data in the form of graphs. Using predefined queries, you can uncover important business trends, product performance, customer behavior, and sales patterns across different locations.

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
        
        "Top 10 Best-Selling Items",
        "Monthly Sales Trend",
        "Top 10 Highest Sales by Location",
        "Top 10 Average Order Value by Location",
        "Revenue Contribution by Membership Status",
        "Promotion Effectiveness"
    ]
)

if st.button("show Dashboard"):
    # Run the selected analysis
    # if analysis == "Total Sales by Category":
    #     result = total_sales_by_category_plot()
    #     st.pyplot(result)

    if analysis == "Top 10 Best-Selling Items":
        result = top_10_best_selling_items_plot()
        st.pyplot(result)


    elif analysis == "Monthly Sales Trend": 
        result = monthly_sales_trend_plot()
        st.pyplot(result)



    elif analysis == "Top 10 Highest Sales by Location":
        result = sales_by_location_plot()
        st.pyplot(result)



    # elif analysis == "Customer Purchase Frequency":
    #     result = customer_purchase_frequency()
    #     st.dataframe(result)

        
    elif analysis == "Top 10 Average Order Value by Location": 
        result = average_order_value_by_location_plot()
        st.pyplot(result)


    elif analysis == "Revenue Contribution by Membership Status":
        result = revenue_contribution_by_membership_status_plot()
        st.pyplot(result)



    # elif analysis == "Product Performance in Different Locations":
    #     result = product_performance_by_location_plot()
    #     st.pyplot(result)



    # elif analysis == "Customer Retention Analysis": 
    #     result = customer_retention_analysis()
    #     st.dataframe(result)

    elif analysis == "Promotion Effectiveness":
        
        result = promotion_effectiveness_plot()
        st.pyplot(result)

    # Continue adding more queries for other analyses

# Close connection at the end
conn.close()
