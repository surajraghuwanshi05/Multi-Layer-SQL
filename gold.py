
import mysql.connector
from mysql.connector import Error
from bronze import create_connection,execute_query



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
        # Create Gold layer
        
        # create_gold_layer_tables(connection)
        # load_gold_layer_tables(connection)
        connection.close()

if __name__ == "__main__":
    main()
