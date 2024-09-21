import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bronze import create_connection




st.set_page_config(
    page_title="Multipage App",
)

conn = create_connection()


# Function to fetch table data
def fetch_table_data(query):
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    return pd.DataFrame(data, columns=columns)

# Display description on main page
st.title("Welcome to the Sales Insights and Analytics Dashboard!")

st.markdown("""
A retail business receives messy sales data from various sources—online stores, outlets, and marketplaces. They need help answering key questions like:

- What are the top-selling products?
- How are monthly sales trending?
- Which customer segments drive the most revenue?
- Which locations or teams are underperforming?            

### Overview

This diagram shows how data is organized in different stages. 
             the Bronze Layer, Silver Layer,  Gold Layer and 
             Presentation Layer.


""")



image_path = 'layers.png' 
st.image(image_path, caption='Multi layer structure', use_column_width=True)


st.markdown("""
           
### Database Schema Overview

This retail business database schema consists of four key tables:
             sales, customers, locations, and items. Each table is interconnected to track and analyze sales data across different locations,
             products, and customers.


""")

image_path2 = 'schema.png' 
st.image(image_path2, caption=' Relationship between Sales, Customers, Locations, and Items', use_column_width=True)