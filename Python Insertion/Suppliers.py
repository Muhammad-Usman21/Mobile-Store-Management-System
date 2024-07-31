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


# Insert fake data into the Suppliers table
for count in range(12):  # Adjust the number of records as needed
    # supplier_id = fake.unique.random_int(min=1, max=1000000)
    first_name = fake.first_name()[:25]
    last_name = fake.last_name()[:25]
    cnic = f"{fake.random_number(digits=5):05d}-{fake.random_number(digits=7):07d}-{random.choice([1,2])}"
    email = f"{first_name}{last_name}{fake.random_int(min=99, max=99999)}@gmail.com"
    phone_number = f"+{fake.random_number(digits=3):03d} {fake.random_number(digits=3):03d} {fake.random_number(digits=7):07d}"
    # street = fake.street_address()[:20]
    # city = random.choice(pakistan_cities)
    province = fake.state()[:40]
    # country = "Pakistan"  # Assuming all suppliers are from Pakistan
    street = fake.street_address()[:40]
    city = fake.city()
    country = fake.country()
    postal_code = fake.zipcode()
    gender = fake.random_element(elements=('M', 'F'))
    date_of_birth = fake.date_of_birth(minimum_age=21, maximum_age=49)

    # SQL query to insert data into the Suppliers table
    query = f"INSERT INTO Suppliers (FirstName, LastName, CNIC, Email, PhoneNumber, Street, City, Province, Country, PostalCode, Gender, DateOfBirth) VALUES ( '{first_name}', '{last_name}', '{cnic}', '{email}', '{phone_number}', '{street}', '{city}', '{province}', '{country}', {postal_code}, '{gender}', '{date_of_birth}')"

    # Execute the query
    cursor.execute(query)

# Commit the changes and close the connection
connection.commit()
connection.close()

