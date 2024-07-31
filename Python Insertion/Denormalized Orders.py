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


# Execute a SELECT query with JOINs
query = """


SELECT
	O.OrderID,
	O.OrderDate,
	O.PaymentMethod,
	C.CustomerID,
	C.FirstName AS CustomerFirstName,
	C.LastName AS CustomerLastName,
	C.CNIC AS CustomerCNIC,
	C.Email AS CustomerEmail,
	C.PhoneNumber AS CustomerPhoneNumber,
	C.Street AS CustomerStreet,
	C.City AS CustomerCity,
	C.Province AS CustomerProvince,
	C.PostalCode AS CustomerPostalCode,
	C.Gender AS CustomerGender,
	C.DateOfBirth AS CustomerDateOfBirth,
	E.EmployeeID,
	E.FirstName AS EmployeeFirstName,
	E.LastName AS EmployeeLastName,
	E.CNIC AS EmployeeCNIC,
	E.Email AS EmployeeEmail,
	E.PhoneNumber AS EmployeePhoneNumber,
	E.Street AS EmployeeStreet,
	E.City AS EmployeeCity,
	E.Province AS EmployeeProvince,
	E.PostalCode AS EmployeePostalCode,
	E.Gender AS EmployeeGender,
	E.DateOfBirth AS EmployeeDateOfBirth,
	E.HireDate AS EmployeeHireDate,
	E.RetireDate AS EmployeeRetireDate,
	EP.PositionID,
	EP.Position AS EmployeePosition,
	EP.Salary AS EmployeeSalary
FROM
	Orders O
	INNER JOIN Customers C ON O.CustomerID = C.CustomerID
	INNER JOIN Employees E ON O.EmployeeID = E.EmployeeID
	LEFT JOIN EmployeePosition EP ON E.PositionID = EP.PositionID

"""

cursor.execute(query)

# Fetch all rows from the result set
result_data = cursor.fetchall()

# Store data in a variable
result_set = []
for row in result_data:
    result = {
        'OrderID': row.OrderID,
        'OrderDate': row.OrderDate,
        'PaymentMethod': row.PaymentMethod,
        'CustomerID': row.CustomerID,
        'CustomerFirstName': row.CustomerFirstName,
        'CustomerLastName': row.CustomerLastName,
        'CustomerCNIC': row.CustomerCNIC,
        'CustomerEmail': row.CustomerEmail,
        'CustomerPhoneNumber': row.CustomerPhoneNumber,
        'CustomerStreet': row.CustomerStreet,
        'CustomerCity': row.CustomerCity,
        'CustomerProvince': row.CustomerProvince,
        'CustomerPostalCode': row.CustomerPostalCode,
        'CustomerGender': row.CustomerGender,
        'CustomerDateOfBirth': row.CustomerDateOfBirth,
        'EmployeeID': row.EmployeeID,
        'EmployeeFirstName': row.EmployeeFirstName,
        'EmployeeLastName': row.EmployeeLastName,
        'EmployeeCNIC': row.EmployeeCNIC,
        'EmployeeEmail': row.EmployeeEmail,
        'EmployeePhoneNumber': row.EmployeePhoneNumber,
        'EmployeeStreet': row.EmployeeStreet,
        'EmployeeCity': row.EmployeeCity,
        'EmployeeProvince': row.EmployeeProvince,
        'EmployeePostalCode': row.EmployeePostalCode,
        'EmployeeGender': row.EmployeeGender,
        'EmployeeDateOfBirth': row.EmployeeDateOfBirth,
        'EmployeeHireDate': row.EmployeeHireDate,
        'EmployeeRetireDate': row.EmployeeRetireDate,
        'PositionID': row.PositionID,
        'EmployeePosition': row.EmployeePosition,
        'EmployeeSalary': row.EmployeeSalary
    }
    result_set.append(result)

# Insert data from the result_set into the CombinedData table
for record in result_set:
    insert_query = """
        INSERT INTO Orders_Denormalized (
            OrderID, OrderDate, PaymentMethod,
            CustomerID, CustomerFirstName, CustomerLastName, CustomerCNIC,
            CustomerEmail, CustomerPhoneNumber, CustomerStreet,
            CustomerCity, CustomerProvince, CustomerPostalCode,
            CustomerGender, CustomerDateOfBirth, EmployeeID,EmployeeFirstName,
            EmployeeLastName, EmployeeCNIC, EmployeeEmail,
            EmployeePhoneNumber, EmployeeStreet, EmployeeCity,
            EmployeeProvince, EmployeePostalCode, EmployeeGender,
            EmployeeDateOfBirth, EmployeeHireDate, EmployeeRetireDate,
            PositionID,EmployeePosition, EmployeeSalary
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)
    """

    cursor.execute(insert_query, (
        record['OrderID'], record['OrderDate'], record['PaymentMethod'],
        record['CustomerID'],record['CustomerFirstName'], record['CustomerLastName'], record['CustomerCNIC'],
        record['CustomerEmail'], record['CustomerPhoneNumber'], record['CustomerStreet'],
        record['CustomerCity'], record['CustomerProvince'], record['CustomerPostalCode'],
        record['CustomerGender'], record['CustomerDateOfBirth'], record['EmployeeID'],record['EmployeeFirstName'],
        record['EmployeeLastName'], record['EmployeeCNIC'], record['EmployeeEmail'],
        record['EmployeePhoneNumber'], record['EmployeeStreet'], record['EmployeeCity'],
        record['EmployeeProvince'], record['EmployeePostalCode'], record['EmployeeGender'],
        record['EmployeeDateOfBirth'], record['EmployeeHireDate'], record['EmployeeRetireDate'],
        record['PositionID'],record['EmployeePosition'], record['EmployeeSalary']
    ))



# Commit the transaction
connection.commit()

print("Data inserted successfully!")

# Close the cursor and connection
cursor.close()
connection.close()



