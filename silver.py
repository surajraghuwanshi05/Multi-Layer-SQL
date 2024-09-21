import mysql.connector
from mysql.connector import Error
from bronze import create_connection,execute_query





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




def load_silver_data(connection):
    silver_sql ="""TRUNCATE TABLE Silver_dim_items;
    INSERT INTO Silver_dim_items(Item_id, Item_name,Inserted_at)
    SELECT Item_id, LOWER(TRIM(Item_name)) as Item_name, NOW() 
    FROM Bronze_dim_items 
    WHERE Item_id IS NOT NULL
    AND Item_name IS NOT NULL;


    TRUNCATE TABLE Silver_dim_locations;
    INSERT INTO Silver_dim_locations(Location_id, Location_name, City,Inserted_at)
    SELECT Location_id, LOWER(TRIM(Location_name)) as Location_name,
    LOWER(TRIM(City)) AS City, NOW() FROM Bronze_dim_locations
    WHERE Location_id IS NOT NULL
    AND Location_name IS NOT NULL
    AND City IS NOT NULL;


    TRUNCATE TABLE Silver_dim_customers;
    INSERT INTO  Silver_dim_customers(Customer_id, Customer_name, Membership_status,Inserted_at)
    SELECT Customer_id, LOWER(TRIM(Customer_name)) AS Customer_name,
    LOWER(TRIM(Membership_status)) AS Membership_status,
    NOW() FROM Bronze_dim_customers
    WHERE Customer_id IS NOT NULL 
    AND Customer_name IS NOT NULL
    AND Membership_status IS NOT NULL;

    
    
    TRUNCATE TABLE Silver_fact_sales;
    INSERT INTO Silver_fact_sales(
    Transaction_id, Item_id, Location_id, Customer_id, Quantity,
    Price_per_unit, Date, Total_amount, Inserted_at)
    SELECT Transaction_id, Item_id, Location_id, Customer_id,
    Quantity, Price_per_unit, Date, Total_amount, NOW()
    FROM Bronze_fact_sales
    WHERE Transaction_id IS NOT NULL
    AND Quantity >= 0 AND Quantity IS NOT NULL
    AND Price_per_unit>=0 AND Price_per_unit IS NOT NULL
    AND Total_amount >=0 AND Total_amount IS NOT NULL;

    """
    execute_query(connection, silver_sql)





# Main program
def main():
    connection = create_connection()

    if connection:
        # Create  Silver, tables
        
        # create_silver_layer_tables(connection)
        # load_silver_layer_tables(connection)
        
        connection.close()

if __name__ == "__main__":
    main()
