import pyodbc
from faker import Faker

# Connection details
server = 'USMAN\\MSSQLSERVERDEV'
database = 'DB_PROJECT'
username = ''
password = ''
driver = '{SQL Server}'

# Connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Create a connection and cursor
connection = pyodbc.connect(conn_str)
cursor = connection.cursor()

# Faker instance for generating fake data
fake = Faker()

# Repair services
repair_services = [
    {"ServiceName": "Screen Replacement", "Description": "Replace damaged screens", "Cost": 1500.00},
    {"ServiceName": "Battery Replacement", "Description": "Replace old or faulty batteries", "Cost": 500.00},
    {"ServiceName": "Water Damage Repair", "Description": "Fix water-damaged devices", "Cost": 1000.00},
    {"ServiceName": "Software Update", "Description": "Install the latest software updates", "Cost": 300.00},
    {"ServiceName": "Data Recovery", "Description": "Recover lost or deleted data", "Cost": 800.00},
    {"ServiceName": "Virus Removal", "Description": "Remove viruses and malware", "Cost": 400.00},
    {"ServiceName": "Charging Port Repair", "Description": "Fix issues with charging ports", "Cost": 600.00},
    {"ServiceName": "Camera Replacement", "Description": "Replace malfunctioning cameras", "Cost": 700.00},
    {"ServiceName": "Speaker Repair", "Description": "Fix problems with speakers", "Cost": 550.00},
    {"ServiceName": "Microphone Replacement", "Description": "Replace faulty microphones", "Cost": 450.00},
    {"ServiceName": "Network Connectivity Fix", "Description": "Address network connection issues", "Cost": 650.00},
    {"ServiceName": "Screen Protector Installation", "Description": "Install protective screen covers", "Cost": 200.00},
    {"ServiceName": "Button Repair", "Description": "Fix issues with physical buttons", "Cost": 500.00},
    {"ServiceName": "Headphone Jack Replacement", "Description": "Replace damaged headphone jacks", "Cost": 350.00},
    {"ServiceName": "Power Button Fix", "Description": "Address problems with power buttons", "Cost": 550.00},
    {"ServiceName": "Data Transfer Service", "Description": "Transfer data between devices", "Cost": 250.00},
    {"ServiceName": "Touchscreen Calibration", "Description": "Calibrate touchscreens for accuracy", "Cost": 300.00},
    {"ServiceName": "SIM Card Slot Repair", "Description": "Fix issues with SIM card slots", "Cost": 400.00},
    {"ServiceName": "Device Cleaning Service", "Description": "Thorough cleaning of devices", "Cost": 150.00},
    {"ServiceName": "Firmware Upgrade", "Description": "Upgrade device firmware", "Cost": 350.00},
]

# Insert fake data into the RepairServices table
for service in repair_services:
    # query = "INSERT INTO RepairServices (ServiceName, Description, Cost) VALUES (?, ?, ?)"
    
    # # Execute the query with parameters
    # cursor.execute(query, service["ServiceName"], service["Description"], service["Cost"])
    
    query = "EXEC InsertionInRepairServices ?, ?, ?"
    cursor.execute(query, service["ServiceName"], service["Description"], service["Cost"])

# Commit the changes and close the connection
connection.commit()
connection.close()
