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


# Function to load data into Bronze Layer
def load_bronze_data(connection):
    load_sql = """
    -- Loading Data
    TRUNCATE TABLE Bronze_fact_sales;
    LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/sales.csv'
    INTO TABLE Bronze_fact_sales
    FIELDS TERMINATED BY ','  
    LINES TERMINATED BY '\\n' 
    IGNORE 1 ROWS
    (Transaction_id, Item_id, Location_id, Customer_id, Quantity, Price_per_unit, Date, Total_amount);
    
    TRUNCATE TABLE Bronze_dim_locations;
    LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/locations.csv'
    INTO TABLE Bronze_dim_locations
    FIELDS TERMINATED BY ','  
    LINES TERMINATED BY '\\n' 
    IGNORE 1 ROWS (Location_id, Location_name, City);

    TRUNCATE TABLE Bronze_dim_items;
    LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/items.csv'
    INTO TABLE Bronze_dim_items
    FIELDS TERMINATED BY ','  
    LINES TERMINATED BY '\\n' 
    IGNORE 1 ROWS (Item_id, Item_name);

    TRUNCATE TABLE Bronze_dim_customers;
    LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customers.csv'
    INTO TABLE Bronze_dim_customers
    FIELDS TERMINATED BY ','  
    LINES TERMINATED BY '\\n' 
    IGNORE 1 ROWS (Customer_id, Customer_name, Membership_status);
    """
    execute_query(connection, load_sql)




# Main program
def main():
    connection = create_connection()

    if connection:
        # Create Bronze layer
        # create_bronze_layer_tables(connection)
        # load_bronze_layer_tables(connection)
        
        connection.close()

if __name__ == "__main__":
    main()