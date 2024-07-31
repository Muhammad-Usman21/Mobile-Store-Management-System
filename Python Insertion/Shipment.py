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




# Execute a SELECT query for Suppliers
query = "SELECT * FROM Suppliers"
cursor.execute(query)

# Fetch all rows from the result set
supplier_data = cursor.fetchall()

# Store data in a variable
suppliers = []
for row in supplier_data:
    supplier = {
        'SupplierID': row.SupplierID,
        'FirstName': row.FirstName,
        'LastName': row.LastName,
        'CNIC': row.CNIC,
        'Email': row.Email,
        'PhoneNumber': row.PhoneNumber,
        'Street': row.Street,
        'City': row.City,
        'Province': row.Province,
        'Country': row.Country,
        'PostalCode': row.PostalCode,
        'Gender': row.Gender,
        'DateOfBirth': row.DateOfBirth
    }
    suppliers.append(supplier)

# # Close the cursor and connection when done
# cursor.close()
# connection.close()











# # Execute a SELECT query for Products
# query = "SELECT * FROM Products"
# cursor.execute(query)

# # Fetch all rows from the result set
# product_data = cursor.fetchall()

# # Store data in a variable
# products = []
# for row in product_data:
#     product = {
#         'ProductID': row.ProductID,
#         'Brand': row.Brand,
#         'ModelNumber': row.ModelNumber,
#         'UnitPrice': row.UnitPrice,
#         'StockQuantity': row.StockQuantity,
#         'OS': row.OS,
#         'Storage': row.Storage,
#         'RAM': row.RAM,
#         'Battery': row.Battery,
#         'Camera': row.Camera,
#         'Display': row.Display,
#         'Processor': row.Processor,
#         'Warranty': row.Warranty,
#         'Description': row.Descriptionn  # Adjusted to match the column name in the table
#     }
#     products.append(product)

# Close the cursor and connection when done
# cursor.close()
# connection.close()






shipping_methodsx = [
    "Standard Shipping",
    "Express Shipping",
    "Priority Mail",
    "Overnight Shipping",
    "Three-Day Shipping",
    "International Shipping",
    "Free Shipping",
]

statuses = ["In Progress", "Arrived", "Arrived", "Arrived", "Arrived"]


# Define your lists and dictionaries (suppliers, etc.)
# ...




y=1
m=6


# shipment_idddd = 1

while True:
    # current_date = (datetime.now() - timedelta(daysss)).date()
    datee = f'202{y}-{m}-1'

    # Insert fake data into the Shipments table
    for qwe in range(fake.random_int(min=6, max=10)):  # Adjust the number of records as needed

        supplier = random.choice(suppliers)
        supplier_id = supplier['SupplierID']

        shipment_date = datee
        shipping_method = random.choice(shipping_methodsx) # Adjust as needed
        # status = random.choice(statuses)  # Adjust as needed
        # arrival_date = shipment_date + timedelta(days=fake.random_int(min=1, max=20))
        arrival_date =  datetime.strptime(shipment_date, '%Y-%m-%d') + timedelta(days=fake.random_int(min=1, max=28))
        
        if arrival_date <= datetime.now():
            status = 'Arrived'
        else:
            status = 'In Progress'
        
        # total_cost = f'{fake.random_int(min=5, max=9)}000000'  # Adjust as needed

        # SQL query to insert data into the Shipments table
        query = f"INSERT INTO Shipments (SupplierID, ShipmentDate, ShippingMethod, Statuss, ArrivalDate) VALUES ({supplier_id}, '{shipment_date}', '{shipping_method}', '{status}', '{arrival_date}')"

        # Execute the query
        cursor.execute(query)
        
        
        
        # rangeee = fake.random_int(min=5, max=15)
        # total_cost = int(total_cost)/rangeee
        
        
        
        # for _ in range(fake.random_int(min=5, max=15)):
        #     # shipment = random.choice(shipments)
        #     # shipment_id = shipment['ShipmentID']

        #     product = random.choice(products)
        #     product_id = product['ProductID']

        #     quantity_received = fake.random_int(min=20, max=70)  # Adjust as needed
            
        #     # cost_per_unit = fake.random_int(min=1, max=100) * 10  # Adjust as needed
        #     cost_per_unit = product['UnitPrice']  # Adjust as needed

        #     # SQL query to insert data into the Shipment_Details table
        #     query = f"INSERT INTO ShipmentDetails (ShipmentID, ProductID, QuantityReceived, CostPerUnit) " \
        #             f"VALUES ({shipment_idddd}, {product_id}, {quantity_received}, {cost_per_unit})"

        #     # Execute the query
        #     cursor.execute(query)
        
    
    if m==12:
        m = 1
        y= y+1
    else:
        m = m+1
        
    if y==4:
        break 
    
    
    
    # shipment_idddd = shipment_idddd + 1
        
    










# Commit the changes and close the connection
connection.commit()
connection.close()


