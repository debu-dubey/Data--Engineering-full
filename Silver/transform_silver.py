import sqlite3
import pandas as pd

conn = sqlite3.connect("/workspaces/Data--Engineering-full/globalshop360.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS silver_orders")

cursor.execute(
    '''
    create table silver_orders as 
    select 
        c.customer_id, 
        c.name, 
        c.reg_date, 
        o.order_id, 
        o.product_name, 
        o.price, 
        o.order_date 
    from CUSTOMERS as c 
    inner join ORDERS as o 
    on c.customer_id = o.customer_id
    '''
)