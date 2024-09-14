# SQL Multi-Layer Architecture with Streamlit Insights

## Project Overview

This project demonstrates a **multi-layer SQL architecture** integrated with a **Streamlit** app to provide real-time insights and analytics. The architecture follows the **Bronze**, **Silver**, and **Gold** layer structure for efficient data handling and transformation. The **Streamlit** app allows users to visualize and interact with the data through a web-based interface.

## Project Structure




- **Bronze Layer:**
  - Stores raw data ingested from various sources.
  - Data is stored in its original format, ensuring no loss of detail.
  
- **Silver Layer:**
  - Processes the raw data by cleaning, transforming, and standardizing it.
  - Prepares the data for analysis by removing duplicates, handling missing values, and applying necessary transformations.

- **Gold Layer:**
  - Final layer for analytics and reporting.
  - Clean, aggregated data is stored for querying insights and generating reports.

## Streamlit App Overview

The **Streamlit** app is used to interact with the data stored in the **Gold Layer** and provides the following features:

- **Data Analytics:** (via `analytics.py`)
  - Generate insights based on key performance indicators (KPIs).
  - Perform comparative analyses between different data points.
  
- **Visualization:** (via `visualize.py`)
  - Visualize trends and patterns in the data using charts and graphs.

- **Documentation:** (via `documentation.py`)
  - Provides an overview and documentation for using the app.

## Setup Instructions

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/surajraghuwanshi05/SQL.git


## File Explanations

- **pages/analytics.py:** 
  - Contains the logic for generating data insights and performing analysis in the Streamlit app. 
  - Includes SQL queries and Python functions to calculate key metrics and trends.

- **pages/documentation.py:** 
  - Serves as a documentation page within the Streamlit app, providing users with a guide on how to navigate and use the app's features.

- **pages/visualize.py:** 
  - Responsible for generating visualizations such as charts and graphs to represent the data insights.
  - Utilizes libraries like `matplotlib` and `seaborn` to create visual outputs in the app.

- **create.py:** 
  - Sets up the multi-layer architecture (Bronze, Silver, Gold) by creating the necessary tables in the database.
  - Defines the structure of each layer and ensures data is appropriately organized and stored.

- **load.py:** 
  - Handles the loading of data into the Bronze, Silver, and Gold layers.
  - Ensures data is moved and transformed correctly between layers.

- **main.py:** 
  - The entry point for the Streamlit app.
  - Coordinates the interaction between different components of the app, including analytics, visualization, and data querying.

- **query.py:** 
  - Contains predefined SQL queries used to extract data from the Gold Layer.
  - Focuses on extracting clean, aggregated data for analysis and visualization in the app.

- **requirements.txt:** 
  - Lists all the Python dependencies required to run the project.
  - Install the dependencies by running `pip install -r requirements.txt`.

