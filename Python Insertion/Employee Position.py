import pyodbc
from faker import Faker

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

# Employee positions
mobile_shop_job_titles = [
    "Store Manager", "Sales Associate", "Accountant", "Assistant Manager",
    "Inventory Manager", "Marketing Coordinator", "Cashier", 
    "Store Cleaner and Maintenance", "Security Officer", 
    "Shipping and Receiving Clerk", "Sales Supervisor", 'Senior Technician',"Mobile Technician",
    "Technical Support Specialist","Technician"
]

# Insert fake data into the EmployeePosition table
for position_id, position in enumerate(mobile_shop_job_titles, start=1):
    # salary = fake.random_int(min=30000, max=80000)  # Example salary range, adjust as needed
    salary = f"{fake.random_int(min=4, max=12)}0000"
    # query = f"INSERT INTO EmployeePosition (PositionID, Position, Salary) VALUES ({position_id+51}, '{position}', {salary})"
    # query = f"INSERT INTO EmployeePosition ( Position, Salary) VALUES ( '{position}', {salary})"
    # query = f"EXEC PROCEDURE InsertionInEmplyeePosition '{position}', {salary}"
    # query = f"""
    #     -- Declare variables for parameters
    #     DECLARE @Position VARCHAR(50)
    #     DECLARE @Salary MONEY

    #     -- Set values for parameters
    #     SET @Position = '{position}'  -- Replace with the actual position value
    #     SET @Salary = {salary}  -- Replace with the actual salary value

    #     -- Execute the stored procedure
    #     EXEC InsertionInEmployeePosition @Position, @Salary

    #     """
    
    # # Execute the query
    # cursor.execute(query)
    
    cursor.execute(f"EXEC InsertionInEmplyeePosition '{position}', {salary}")


# Commit the changes and close the connection
connection.commit()
connection.close()
