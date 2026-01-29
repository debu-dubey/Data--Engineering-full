import sqlite3
import pandas as pd

conn = sqlite3.connect("/workspaces/Data--Engineering-full/globalshop360.db")
cursor = conn.cursor()

cursor.execute("drop table if exists gold_regional_sales")

cursor.execute(
    '''
    create table gold_regional_sales as 
    select country, 
        count(order_id) as total_orders, 
        sum(price) as total_revenue
    from silver_orders
    group by country
    order by total_revenue desc
    '''
)

conn.commit()
conn.close()