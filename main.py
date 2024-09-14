import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from create import create_connection




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
### Scenario: Business Struggling with Data Overload​

a growing retail business is dealing with massive amounts of sales data coming in from different sources—online stores, physical outlets, and third-party marketplaces. Every day, they receive raw sales data in different formats and from various locations.​

The problem they face is that this data is unstructured and messy, making it difficult to extract valuable insights. They want to answer questions like:​

- What are the top-selling products across different regions?​

- How are monthly sales trending over time?​

- Which customer segment is contributing the most to revenue?​

- Which teams or locations are underperforming?"            

### Overview

This application provides a comprehensive platform for analyzing sales and customer data,
 offering valuable insights into key business metrics. Built using a multi-layer architecture (Bronze, Silver, and Gold layers),
 this app integrates data from various sources and allows you to interactively explore critical sales information.
 Below, you'll find details about the Structure. These layers form the foundation for the insights and metrics you can explore through this application.


""")



image_path = 'layers.png' 
st.image(image_path, caption='Multi layer structure', use_column_width=True)