import mysql.connector
from mysql.connector import Error
from create import create_connection



# Execute SQL commands
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")



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




def load_gold_data(connection):
    gold_sql ="""INSERT INTO Gold_dim_items(Item_id, Item_name,Inserted_at,Updated_at)
    SELECT Item_id, Item_name, NOW(), NOW() FROM Silver_dim_items 
    ON DUPLICATE KEY UPDATE
    Item_name = VALUES(Item_name),
    Updated_at = NOW();

    INSERT INTO Gold_dim_locations(Location_id, Location_name, City,Inserted_at,Updated_at)
    SELECT Location_id, Location_name, City, NOW(), NOW() FROM Silver_dim_locations
    ON DUPLICATE KEY UPDATE
    Location_name = VALUES(Location_name),
    City = VALUES(City),
    Updated_at = NOW() ;

    INSERT INTO  Gold_dim_customers(Customer_id, Customer_name, Membership_status,Inserted_at,Updated_at)
    SELECT Customer_id, Customer_name, Membership_status, NOW(), NOW() FROM Silver_dim_customers
    ON DUPLICATE KEY UPDATE
    Customer_name = VALUES(Customer_name),
    Membership_status = VALUES(Membership_status),
    Updated_at = NOW();
    

    INSERT INTO Gold_fact_sales(Item_sk,Location_sk,Customer_sk,Quantity,Price_per_unit,date,TOtal_amount,Inserted_at,Updated_at)
    SELECT Item_id,Location_id,Customer_id,Quantity,Price_per_unit,Date,Total_amount, NOW(), NOW()
    FROM Silver_fact_sales
    ON DUPLICATE KEY UPDATE
        Item_sk = VALUES(Item_sk),
        Location_sk = VALUES(Location_sk),
        Customer_sk = VALUES(Customer_sk),
        Quantity = VALUES(Quantity),
        Price_per_unit = VALUES(Price_per_unit),
        Date = VALUES(Date),
        Total_amount = VALUES(Total_amount),
        Updated_at = NOW();
    """
    execute_query(connection, gold_sql)

# Main program
def main():
    connection = create_connection()

    if connection:
        # Create Bronze, Silver, and Gold tables
        # load_bronze_layer_tables(connection)
        # load_silver_layer_tables(connection)
        # load_gold_layer_tables(connection)
        connection.close()

if __name__ == "__main__":
    main()
