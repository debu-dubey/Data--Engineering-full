import pandas as pd 
from faker import Faker 
import random

fake = Faker()

NUM_CUSTOMERS = 100
NUM_ORDERS = 500

#Generate the customers
customers = []
for i in range(NUM_CUSTOMERS):
    customers.append(
        {
            'customer_id' : 1000 + i,
            'name' : fake.name(),
            'country' : fake.country(),
            'reg_date' : fake.date_this_year()
        }
    )

df_customers = pd.DataFrame(customers)

df_customers.to_csv('customers.csv', index=False)

# Generate the orders
orders = []
for i in range(NUM_ORDERS):
    orders.append(
        {
            'order_id': fake.uuid4(),
            'customer_id': random.randint(1000, 1000 + NUM_CUSTOMERS - 1),
            'product_name': random.choice(['Laptop','Mobile','Washing Machine','Bat','Bowl','Monitor']),
            'price': round(random.uniform(100,200),2),
            'order_date': fake.date_time_this_year()
        }
    )
df_orders = pd.DataFrame(orders)
df_orders.to_csv('orders.csv',index=False)

print('Data generation is complete')