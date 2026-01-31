import sqlite3
import pandas as pd 

conn = sqlite3.connect('/workspaces/Data--Engineering-full/globalshop360.db')
cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS CUSTOMERS (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT,
    reg_date DATE)
    '''
)


cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS ORDERS (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    product_name TEXT,
    price REAL,
    order_date TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES CUSTOMERS (customer_id)
    )
    '''
)

customers_df = pd.read_csv('customers.csv')
orders_df = pd.read_csv('orders.csv')

customers_df.to_sql('CUSTOMERS' , conn, if_exists = 'replace', index=False)
orders_df.to_sql('ORDERS' , conn, if_exists = 'replace', index=False)

conn.commit()
conn.close()

print("Data succesfully uploaded to globalshop360.db")