import mysql.connector
from mysql.connector import Error

# Connect to MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",    # e.g., "localhost"
        user="root",    # e.g., "root"
        password="suraj@123",  # Your MySQL password
        database="test"  # Your database name
        )
        if connection.is_connected():
            print("Connected to MySQL")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Execute SQL commands
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to create Bronze Layer Tables
def create_bronze_layer_tables(connection):
    bronze_sql = """
    CREATE TABLE IF NOT EXISTS Bronze_dim_items(
        Item_id int,
        Item_name varchar(255),
        Inserted_at datetime default current_timestamp
    );

    CREATE TABLE IF NOT EXISTS Bronze_dim_locations(
        Location_id int,
        Location_name varchar(255),
        City varchar(255),
        Inserted_at datetime default current_timestamp
    );

    CREATE TABLE IF NOT EXISTS Bronze_dim_customers(
        Customer_id INT,
        Customer_name varchar(255),
        Membership_status varchar(255),
        Inserted_at datetime default current_timestamp
    );

    CREATE TABLE IF NOT EXISTS Bronze_fact_sales(
        Transaction_id int,
        Item_id int,
        Location_id int,
        Customer_id int,
        Quantity int,
        Price_per_unit float,
        Date date,
        Total_amount float,
        Inserted_at datetime default current_timestamp
    );
    """
    execute_query(connection, bronze_sql)


# Function to create Silver Layer Tables
def create_silver_layer_tables(connection):
    silver_sql = """
    CREATE TABLE IF NOT EXISTS Silver_dim_customers(
        Customer_id int ,
        Customer_name varchar(255) ,
        Membership_status varchar(50) ,
        Inserted_at datetime
    );

    CREATE TABLE IF NOT EXISTS Silver_dim_items(
        Item_id int,
        Item_name varchar(255),
        Inserted_at datetime
    );

    CREATE TABLE IF NOT EXISTS Silver_dim_locations(
        Location_id int,
        Location_name varchar(255) ,
        City varchar(255),
        Inserted_at datetime
    );

    CREATE TABLE IF NOT EXISTS Silver_fact_sales(
        Transaction_id int ,
        Item_id int,
        Location_id int,
        Customer_id int,
        Quantity int ,
        Price_per_unit float ,
        Date date ,
        Total_amount float,
        Inserted_at datetime
    );
    """
    execute_query(connection, silver_sql)





# Function to create Gold Layer Tables
def create_gold_layer_tables(connection):
    gold_sql = """
    CREATE TABLE IF NOT EXISTS Gold_dim_customers(
        Customer_sk int auto_increment unique,
        Customer_id int unique,
        Customer_name varchar(255),
        Membership_status varchar(255),
        Inserted_at datetime,
        Updated_at datetime
    );

    CREATE TABLE IF NOT EXISTS Gold_dim_items(
        Item_sk int auto_increment unique,
        Item_id int unique,
        Item_name varchar(255),
        Inserted_at datetime,
        Updated_at datetime
    );

    CREATE TABLE IF NOT EXISTS Gold_dim_locations(
        Location_sk int auto_increment unique,
        Location_id int unique,
        Location_name varchar(255),
        City varchar(255),
        Inserted_at datetime,
        Updated_at datetime
    );

    CREATE TABLE IF NOT EXISTS Gold_fact_sales(
        Sales_sk int auto_increment unique,
        Item_sk int,
        Location_sk int,
        Customer_sk int,
        Quantity int,
        Price_per_unit float,
        Date date,
        Total_amount float,
        Inserted_at datetime,
        Updated_at datetime
    );
    """
    execute_query(connection, gold_sql)




# Main program
def main():
    connection = create_connection()

    if connection:
        # Create Bronze, Silver, and Gold tables
        # create_bronze_layer_tables(connection)
        # create_silver_layer_tables(connection)
        # create_gold_layer_tables(connection)
        connection.close()

if __name__ == "__main__":
    main()
