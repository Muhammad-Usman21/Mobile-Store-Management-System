

import pyodbc
import random
from faker import Faker
from datetime import datetime, timedelta

# Connection details
server = 'USMAN\MSSQLSERVERDEV'
database = 'DB_PROJECT'
username = ''
password = ''
driver = '{SQL Server}'

# Connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(conn_str)

# Create a cursor from the connection
cursor = connection.cursor()

# Faker instance for generating fake data
fake = Faker()














# Execute a SELECT query for Products
query = "SELECT * FROM Products"
cursor.execute(query)

# Fetch all rows from the result set
product_data = cursor.fetchall()

# Store data in a variable
products = []
for row in product_data:
    product = {
        'ProductID': row.ProductID,
        'Brand': row.Brand,
        'ModelNumber': row.ModelNumber,
        'UnitPrice': row.UnitPrice,
        'StockQuantity': row.StockQuantity,
        'OS': row.OS,
        'Storage': row.Storage,
        'RAM': row.RAM,
        'Battery': row.Battery,
        'Camera': row.Camera,
        'Display': row.Display,
        'Processor': row.Processor,
        'Warranty': row.Warranty,
        'Description': row.Descriptionn  # Adjusted to match the column name in the table
    }
    products.append(product)

# Close the cursor and connection when done
# cursor.close()
# connection.close()


        
        
        
# Execute a SELECT query for Orders
query = "SELECT * FROM Orders"
cursor.execute(query)

# Fetch all rows from the result set
order_data = cursor.fetchall()

# Store data in a variable
orders = []
for row in order_data:
    order = {
        'OrderID': row.OrderID,
        'CustomerID': row.CustomerID,
        'EmployeeID': row.EmployeeID,
        'OrderDate': row.OrderDate,
        # 'TotalAmount': row.TotalAmount,  # Adjust based on your actual column names
        'PaymentMethod': row.PaymentMethod
    }
    orders.append(order)




# Execute a SELECT query for RepairServices
query = "SELECT * FROM RepairServices"
cursor.execute(query)

# Fetch all rows from the result set
repair_service_data = cursor.fetchall()

# Store data in a variable
repair_services = []
for row in repair_service_data:
    repair_service = {
        'RepairID': row.RepairID,
        'ServiceName': row.ServiceName,
        'Description': row.Descriptionn,
        'Cost': row.Cost
    }
    repair_services.append(repair_service)



repair_service_notes = [
    "Replaced faulty component.",
    "Fixed wiring issues.",
    "Performed routine maintenance.",
    "Installed new parts.",
    "Adjusted settings for optimal performance.",
    "Completed diagnostic tests.",
    "Resolved software conflicts.",
    "Cleaned and lubricated moving parts.",
    "Conducted system inspection.",
    "Verified system integrity."
]



for order in orders:
    
    order_id = order['OrderID']
    
    if random.choice([True, False, False, False]):


        for _ in range(random.choice([1, 1, 4,2,2,2,3,3,3,3,5,5,5, 3, 3, 4, 5])):
            # order = random.choice(order_data)
            # order_id = order['OrderID']

            repair_service = random.choice(repair_services )
            repair_id = repair_service['RepairID']

            # quantity = random.choice([1, 1, 1, 2, 2, 2, 3, 3])  # Adjust as needed

            notes = random.choice(repair_service_notes) # Adjust as needed

            # SQL query to insert data into the OrderRepairs table
            query = f"INSERT INTO OrderRepairs (OrderID, RepairID, Notes) " \
                    f"VALUES ({order_id}, {repair_id}, '{notes}')"

            # Execute the query
            cursor.execute(query)
        
        
        
        
            
    else :
        
        for _ in range(random.choice([1,1,1,2,2,2, 3,3, 4, 5])):
            # order = random.choice(orders)
            # order_id = order['OrderID']

            product = random.choice(products)
            product_id = product['ProductID']

            quantity = random.choice([1,1,1,2])  # Adjust as needed
            
            unit_price = product['UnitPrice'] * quantity  # Adjust as needed
            
            discount = fake.random_int(min=0, max=3)  # Adjust as needed
            # total_price = quantity * unit_price * (1 - discount / 100)  # Calculate total_price based on quantity, unit_price, and discount

            # SQL query to insert data into the OrderDetails table
            query = f"INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice, Discount) " \
                    f"VALUES ({order_id}, {product_id}, {quantity}, {unit_price}, {discount})"

            # Execute the query
    
            cursor.execute(query)
    
    
    
    # order_id = order_id + 1








# Commit the changes and close the connection
connection.commit()
connection.close()


