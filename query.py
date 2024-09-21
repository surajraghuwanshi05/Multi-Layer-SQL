import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from bronze import create_connection


conn = create_connection()

# Function to run a SQL query and return the result as a pandas DataFrame
def run_query(query):
    cursor = conn.cursor(dictionary=True)  # Returns results as dictionary
    cursor.execute(query)
    result = cursor.fetchall()
    return pd.DataFrame(result)

# Queries from Gold Layer analytics

def total_sales_by_category():
    query = """
    SELECT I.Item_name,
           SUM(S.Total_amount) AS Amount_per_item
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_items AS I ON S.Item_sk = I.Item_id
    GROUP BY Item_name 
    ORDER BY Amount_per_item DESC;
    """

    # Run the query
    return run_query(query)
    

def top_10_best_selling_items():
    query = """
    SELECT I.Item_name,
           SUM(S.Quantity) AS Quantity_per_item
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_items AS I ON S.Item_sk = I.Item_id
    GROUP BY Item_name 
    ORDER BY Quantity_per_item DESC 
    LIMIT 10;
    """
    return run_query(query)

def monthly_sales_trend():
    query = """
    SELECT SUM(Total_amount) AS Revenue_per_month, 
           MONTHNAME(Date) AS MONTH
    FROM gold_fact_sales 
    WHERE Date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    GROUP BY MONTH
    ORDER BY Revenue_per_month DESC;
    """
    return run_query(query)

def sales_by_location():
    query = """
    SELECT L.Location_name,
           SUM(S.Total_amount) AS Revenue_per_location
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_locations AS L ON S.Location_sk = L.Location_id
    GROUP BY Location_name
    ORDER BY Revenue_per_location DESC;
    """
    return run_query(query)

def customer_purchase_frequency():
    query = """
    SELECT C.Customer_name,
           COUNT(C.Customer_name) AS Purchase_Count
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_customers AS C ON S.Customer_sk = C.Customer_id
    GROUP BY Customer_name
    ORDER BY Purchase_Count DESC;
    """
    return run_query(query)

def average_order_value_by_location():
    query = """
    SELECT L.Location_name,
           AVG(S.Total_amount) AS AOV
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_locations AS L ON S.Location_sk = L.Location_id
    GROUP BY Location_name
    ORDER BY AOV DESC;
    """
    return run_query(query)

def revenue_contribution_by_membership_status():
    query = """
    SELECT C.Membership_status,
           SUM(S.Total_amount) AS Revenue_per_membership
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_customers AS C ON S.Customer_sk = C.Customer_id
    GROUP BY Membership_status
    ORDER BY Revenue_per_membership DESC;
    """
    return run_query(query)

def product_performance_by_location():
    query = """
    SELECT L.Location_name, I.Item_name,
           SUM(S.Quantity) AS Total_quantity
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_items AS I ON S.Item_sk = I.Item_id
    LEFT JOIN gold_dim_locations AS L ON S.Location_sk = L.Location_id
    GROUP BY Item_name, Location_name
    ORDER BY Item_name ASC, Total_quantity DESC;
    """
    return run_query(query)

def customer_retention_analysis():
    query = """
    SELECT C.Customer_name
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_customers AS C ON S.Customer_sk = C.Customer_id
    WHERE YEAR(S.date) = '2023' AND (MONTH(S.Date) BETWEEN 1 AND 6) 
    AND C.Customer_name IN (
        SELECT C.Customer_name
        FROM gold_fact_sales AS S
        LEFT JOIN gold_dim_customers AS C ON S.Customer_sk = C.Customer_id
        WHERE YEAR(S.date) = '2023' AND (MONTH(S.Date) BETWEEN 7 AND 12)
    );
    """
    return run_query(query)

def promotion_effectiveness():
    query = """
    SELECT 'Promotional Period' AS Period,
           AVG(Total_amount) AS AVG_Sales
    FROM gold_fact_sales
    WHERE MONTH(Date) BETWEEN 10 AND 12 
    UNION 
    SELECT 'Non-Promotional Period' AS Period,
           AVG(Total_amount) AS AVG_Sales
    FROM gold_fact_sales
    WHERE MONTH(Date) NOT BETWEEN 10 AND 12;
    """
    return run_query(query)




# -----------------------------------------------------------------------

# Queries for  ploting


def top_10_best_selling_items_plot():
    query = """
    SELECT I.Item_name,
           SUM(S.Quantity) AS Quantity_per_item
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_items AS I ON S.Item_sk = I.Item_id
    GROUP BY Item_name 
    ORDER BY Quantity_per_item DESC
    LIMIT 10;
    """
    
    # Run the query
    df = run_query(query)
    
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the bar chart
    ax.bar(df['Item_name'], df['Quantity_per_item'], color='lightgreen')
    
    # Set labels and title
    ax.set_xlabel('Item Name')
    ax.set_ylabel('Quantity Sold')
    ax.set_title('Top 10 Best Selling Items')
    
    # Rotate x-axis labels
    ax.set_xticklabels(df['Item_name'], rotation=45)
    
    # Adjust layout
    fig.tight_layout()
    return fig



def monthly_sales_trend_plot():
    query = """
    SELECT SUM(Total_amount) AS Revenue_per_month, 
       MONTHNAME(Date) AS MONTH,
       MONTH(Date) AS Month_Number
FROM gold_fact_sales 
WHERE Date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY MONTH, Month_Number
ORDER BY Month_Number;

    """
    
    # Run the query
    df = run_query(query)
    
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the line chart
    ax.plot(df['MONTH'], df['Revenue_per_month'], marker='o', color='blue')
    
    # Set labels and title
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue')
    ax.set_title('Monthly Sales Trend')
    
    # Rotate x-axis labels
    ax.set_xticklabels(df['MONTH'], rotation=45)
    
    # Adjust layout
    fig.tight_layout()
    return fig

def sales_by_location_plot():
    query = """
    SELECT L.Location_name,
           SUM(S.Total_amount) AS Revenue_per_location
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_locations AS L ON S.Location_sk = L.Location_id
    GROUP BY Location_name
    ORDER BY Revenue_per_location DESC LIMIT 10;
    """
    
    # Run the query
    df = run_query(query)
    
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the bar chart
    ax.bar(df['Location_name'], df['Revenue_per_location'], color='orange')
    
    # Set labels and title
    ax.set_xlabel('Location')
    ax.set_ylabel('Revenue')
    ax.set_title('Sales by Location')
    
    # Rotate x-axis labels
    ax.set_xticklabels(df['Location_name'], rotation=45)
    
    # Adjust layout
    fig.tight_layout()
    return fig


def average_order_value_by_location_plot():
    query = """
    SELECT L.Location_name,
           AVG(S.Total_amount) AS AOV
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_locations AS L ON S.Location_sk = L.Location_id
    GROUP BY Location_name
    ORDER BY AOV DESC LIMIT 10;
    """
    
    # Run the query
    df = run_query(query)
    
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the bar chart
    ax.bar(df['Location_name'], df['AOV'], color='red')
    
    # Set labels and title
    ax.set_xlabel('Location')
    ax.set_ylabel('Average Order Value (AOV)')
    ax.set_title('Average Order Value by Location')
    
    # Rotate x-axis labels
    ax.set_xticklabels(df['Location_name'], rotation=45)
    
    # Adjust layout
    fig.tight_layout()
    return fig



def revenue_contribution_by_membership_status_plot():
    query = """
    SELECT C.Membership_status,
           SUM(S.Total_amount) AS Revenue_per_membership
    FROM gold_fact_sales AS S
    LEFT JOIN gold_dim_customers AS C ON S.Customer_sk = C.Customer_id
    GROUP BY Membership_status
    ORDER BY Revenue_per_membership DESC;
    """
    
    # Run the query
    df = run_query(query)
    
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the pie chart
    ax.pie(df['Revenue_per_membership'], labels=df['Membership_status'], autopct='%1.1f%%', startangle=90)
    
    # Set title
    ax.set_title('Revenue Contribution by Membership Status')
    
    # Equal aspect ratio ensures the pie chart is circular
    ax.axis('equal')
    
    return fig


def promotion_effectiveness_plot():
    query = """
    SELECT 'Promotional Period' AS Period,
           AVG(Total_amount) AS AVG_Sales
    FROM gold_fact_sales
    WHERE MONTH(Date) BETWEEN 10 AND 12 
    UNION 
    SELECT 'Non-Promotional Period' AS Period,
           AVG(Total_amount) AS AVG_Sales
    FROM gold_fact_sales
    WHERE MONTH(Date) NOT BETWEEN 10 AND 12;
    """
    
    # Run the query
    df = run_query(query)
    
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create the bar chart
    ax.bar(df['Period'], df['AVG_Sales'], color=['#FF9999', '#66B3FF'])
    
    # Set labels and title
    ax.set_xlabel('Period')
    ax.set_ylabel('Average Sales')
    ax.set_title('Promotion Effectiveness')
    
    return fig
