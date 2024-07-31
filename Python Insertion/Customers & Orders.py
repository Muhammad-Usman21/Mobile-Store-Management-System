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



pakistani_names = [
    "Ali", "Fatima", "Ahmed", "Ayesha", "Bilal", "Saima", "Usman", "Saba", "Imran", "Samina",
    "Omar", "Nadia", "Farhan", "Zainab", "Adnan", "Shabnam", "Tariq", "Zahra", "Rizwan", "Shazia",
    "Kamran", "Sadia", "Naveed", "Amina", "Waqar", "Fauzia", "Tahir", "Sadia", "Khalid", "Nazia",
    "Saad", "Asma", "Nasir", "Farida", "Noman", "Hina", "Asif", "Fariha", "Arif", "Tasneem",
    "Rashid", "Sara", "Akbar", "Fiza", "Shahid", "Bushra", "Yousuf", "Rukhsar", "Haris", "Najma",
    "Farooq", "Huma", "Irfan", "Shahnaz", "Kashif", "Rukhsar", "Majid", "Sofia", "Javed", "Nighat",
    "Salman", "Rabia", "Amir", "Parveen", "Mansoor", "Shazia", "Ghulam", "Shireen", "Talha", "Farzana",
    "Hamza", "Yasmeen", "Yasin", "Gulshan", "Riaz", "Asiya", "Azhar", "Nashra", "Qasim", "Iqra",
    "Rafiq", "Rukhsar", "Waheed", "Fauzia", "Shafiq", "Tabassum", "Younus", "Kausar", "Hamid", "Nida",
    "Sultan", "Zubaida", "Rashid", "Noreen", "Ismail", "Rabia", "Saeed", "Riffat", "Sabir", "Uzma",
    "Taufeeq", "Saima", "Iqbal", "Arzoo", "Sohail", "Sarwat", "Zafar", "Naila", "Abdul", "Rukhsana",
    "Khalil", "Firdous", "Feroz", "Madiha", "Jamil", "Shaista", "Tariq", "Tahira", "Akhtar", "Bushra",
    "Kareem", "Naima", "Majeed", "Sameera", "Nadeem", "Rehana", "Aamir", "Nida", "Rafiq", "Rukhsar",
    "Waseem", "Shazia", "Nasir", "Shabnam", "Khaleel", "Kanwal", "Sajid", "Safia", "Mustafa", "Shahnaz",
    "Akram", "Shazia", "Rashid", "Sadia", "Zubair", "Rukhsar", "Adil", "Kausar", "Aftab", "Saba",
    "Shakeel", "Tasneem", "Sharif", "Parveen", "Najeeb", "Nighat", "Qadir", "Farida", "Tanveer", "Sofia",
    "Saboor", "Nasreen", "Rameez", "Rukhsana", "Nawaz", "Fauzia", "Yasin", "Sarwat", "Rahim", "Tabassum",
    "Zulfiqar", "Farzana", "Nasim", "Rabia", "Zaheer", "Nashra", "Arshad", "Iqra", "Rashid", "Rukhsar",
    "Faisal", "Sofia", "Sohail", "Parveen", "Usama", "Bushra", "Shabbir", "Shireen", "Aslam", "Nighat",
    "Raheel", "Huma", "Yousuf", "Saira", "Farrukh", "Rukhsana", "Ashraf", "Saba", "Naeem", "Tasneem",
    "Aasia", "Adeel", "Afshan", "Aisha", "Akhter", "Aleem", "Alisha", "Altaf", "Amna", "Anwar",
    "Arshad", "Asghar", "Asma", "Aurangzeb", "Ayesha", "Azam", "Azhar", "Bashir", "Bushra", "Dawood",
    "Fahad", "Faisal", "Farah", "Farhan", "Fauzia", "Fazal", "Ghulam", "Hafeez", "Hameed", "Hassan",
    "Humaira", "Hussain", "Iram", "Irfan", "Jahangir", "Kashan", "Khadija", "Khurram", "Madiha", "Mahmood",
    "Majid", "Mansoor", "Mehmood", "Mehnaz", "Mohammad", "Nadia", "Naima", "Najeeb", "Nashra", "Naveed",
    "Nayab", "Nida", "Noreen", "Noshad", "Parveen", "Qamar", "Qurat", "Rabia", "Rameez", "Rashid",
    "Rehana", "Rizwan", "Saadia", "Saba", "Sadaf", "Sadia", "Safdar", "Saima", "Salma", "Samar",
    "Samina", "Sana", "Shabbir", "Shahbaz", "Shahid", "Shahzad", "Shakeel", "Shazia", "Sheraz", "Shumaila",
    "Sidra", "Sobia", "Sohail", "Subhan", "Sultan", "Tahira", "Tariq", "Umair", "Usman", "Wahab",
    "Waqar", "Yasir", "Yasmeen", "Zafar", "Zahid", "Zain", "Zainab", "Zaheer", "Zainab", "Zubair"
]
male_names = [
    "Ali", "Ahmed", "Bilal", "Usman", "Imran", "Omar", "Farhan", "Adnan", "Tariq", "Rizwan",
    "Kamran", "Naveed", "Waqar", "Tahir", "Khalid", "Saad", "Nasir", "Noman", "Asif", "Rashid",
    "Akbar", "Shahid", "Yousuf", "Haris", "Farooq", "Irfan", "Kashif", "Majid", "Javed", "Salman",
    "Amir", "Mansoor", "Ghulam", "Talha", "Hamza", "Yasin", "Riaz", "Azhar", "Qasim", "Rafiq",
    "Waheed", "Shafiq", "Younus", "Hamid", "Sultan", "Rashid", "Ismail", "Saeed", "Sabir", "Taufeeq",
    "Iqbal", "Sohail", "Zafar", "Abdul", "Khalil", "Feroz", "Jamil", "Tariq", "Akhtar", "Kareem",
    "Majeed", "Nadeem", "Aamir", "Rafiq", "Waseem", "Nasir", "Khaleel", "Sajid", "Mustafa", "Akram",
    "Rashid", "Zulfiqar", "Nasim", "Zaheer", "Arshad", "Rashid", "Sohail", "Usama", "Shabbir", "Aslam",
    "Raheel", "Yousuf", "Farrukh", "Ashraf", "Naeem", "Adeel", "Akhter", "Aleem", "Altaf", "Arshad",
    "Asghar", "Aurangzeb", "Azam", "Azhar", "Bashir", "Dawood", "Fahad", "Faisal", "Farhan", "Fazal",
    "Ghulam", "Hafeez", "Hameed", "Hassan", "Hussain", "Irfan", "Jahangir", "Kashan", "Khurram", "Mahmood",
    "Majid", "Mansoor", "Mehmood", "Mohammad", "Najeeb", "Noshad", "Qamar", "Rameez", "Rehana", "Rizwan",
    "Saadia", "Sadaf", "Safdar", "Saif", "Sajjad", "Salman", "Samad", "Sami", "Sarfraz", "Shahbaz",
    "Shahzad", "Shakeel", "Sheraz", "Subhan", "Taher", "Taimur", "Tariq", "Umair", "Usama", "Wahab",
    "Waqas", "Yasir", "Zahid", "Zain", "Zaheer", "Zubair"
]

pakistani_street_names = [
    "Jinnah Avenue", "Iqbal Street", "Allama Iqbal Road", "Liaquat Boulevard", "Fatima Jinnah Lane",
    "Quaid-e-Azam Street", "Gulshan-e-Iqbal Road", "Shaukat Khanum Street", "Faisal Boulevard", "Sir Syed Road",
    "Raziq Street", "Javed Avenue", "Nasreen Lane", "Hafeez Road", "Sultana Street", "Wahid Road",
    "Ahmed Square", "Al-Noor Street", "Shaheen Avenue", "Farid Street", "Aziz Lane", "Sadiq Road",
    "Rukhsar Street", "Malik Crescent", "Anwar Lane", "Hina Road", "Yasin Street", "Zahra Lane",
    "Munir Avenue", "Rabia Road", "Shabbir Street", "Yasmeen Boulevard", "Ahsan Lane", "Nida Street",
    "Raheel Road", "Samina Street", "Tariq Avenue", "Naima Lane", "Ali Crescent", "Farah Road",
    "Khalid Street", "Bushra Lane", "Haider Avenue", "Shazia Road", "Rizwan Street", "Ayesha Lane",
    "Naveed Road", "Fariha Street", "Arif Avenue", "Kausar Lane"
]

pakistan_cities = [
    "Karachi", "Lahore", "Islamabad", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala", "Peshawar",
    "Quetta", "Sialkot", "Bahawalpur", "Sukkur", "Jhang", "Sheikhupura", "Abbottabad", "Gujrat", "Sargodha",
    "Mardan", "Kasur", "Dera Ghazi Khan", "Sahiwal", "Okara", "Wah Cantonment", "Mingora", "Nawabshah",
    "Chiniot", "Kotri", "Larkana", "Mirpur Khas", "Jacobabad", "Shikarpur", "Rahim Yar Khan", "Kohat",
    "Khuzdar", "Dadu", "Gojra", "Muridke", "Bahawalnagar", "Samundri", "Tando Allahyar", "Khairpur",
    "Chishtian", "Abbottabad", "Mandi Bahauddin", "Daska", "Pakpattan", "Tando Adam", "Khuzdar", "Vehari"
]

pakistan_provinces = ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan", "Islamabad Capital Territory", "Gilgit-Baltistan"]

mobile_shop_job_titles = [
    "Store Manager","Sales Associate", "Customer Service Representative","Mobile Technician","Inventory Manager","Marketing Coordinator",
    "Cashier","Technical Support Specialist","Store Cleaner/Maintenance","Security Officer","Accountant",
    "Assistant Manager","Shipping and Receiving Clerk","Retail Trainer","Sales Supervisor",
]

# Payment methods
payment_methods = ["Credit Card", "Cash", "Bank Transfer"]













# Execute a SELECT query
query = "SELECT * FROM Employees"
cursor.execute(query)

# Fetch all rows from the result set
employee_data = cursor.fetchall()

# Store data in a variable
employees = []
for row in employee_data:
    employee = {
        'EmployeeID': row.EmployeeID,
        'FirstName': row.FirstName,
        'LastName': row.LastName,
        'CNIC': row.CNIC,
        'Email': row.Email,
        'PhoneNumber': row.PhoneNumber,
        'Street': row.Street,
        'City': row.City,
        'Province': row.Province,
        'PostalCode': row.PostalCode,
        'Gender': row.Gender,
        'DateOfBirth': row.DateOfBirth,
        'HireDate': row.HireDate,
        'RetireDate': row.RetireDate,
        'PositionID': row.PositionID
    }
    employees.append(employee)
    
    
    











customerrr_count = 1


daysss = 800

while True:
    
    current_date = (datetime.now() - timedelta(daysss)).date()


    # Insert fake data into the Customers table
    for qwe in range(fake.random_int(min=50, max=80)):  # Adjust the number of records as needed
        
        counterrrE = 0

        while True:
            
            counterrrE = counterrrE + 1
            
            random_employee = random.choice(employees)
            random_employeeID = random_employee['EmployeeID']

            
            date_string = random_employee['HireDate']  # Replace this with your date string
            date_format = "%Y-%m-%d"
            # Convert the string to a datetime object
            random_employeeHire = datetime.strptime(date_string, date_format).date()    
            
            date_string = random_employee['RetireDate']  # Replace this with your date string
            date_format = "%Y-%m-%d"
            
            if date_string != None :
                # Convert the string to a datetime object
                random_employeeRetire = datetime.strptime(date_string, date_format).date()
                
            else:
                random_employeeRetire =  None


            if random_employeeHire < current_date :
                if random_employeeRetire != None :
                    if current_date < random_employeeRetire :
                        break
                    
                    else:
                        continue
                    
                else:
                    break
                    
            else:
                continue
                    
            if counterrrE== 100:
                break
            
        if counterrrE== 100:
            break
        

        first_name = random.choice(pakistani_names)
        last_name = random.choice(male_names)

        cnic = f"{fake.random_number(digits=5):05d}-{fake.random_number(digits=7):07d}-{random.choice([1,2])}"

        email = f"{first_name}{last_name}{fake.random_number(digits=6)}@gmail.com"
        phone_number = f"+92 3{fake.random_number(digits=2):02d} {fake.random_number(digits=7):07d}"
        street = random.choice(pakistani_street_names)
        city = random.choice(pakistan_cities)
        province = random.choice(pakistan_provinces)
        postal_code = fake.zipcode()
        gender = fake.random_element(elements=('M', 'F'))
        date_of_birth = fake.date_of_birth(minimum_age=19, maximum_age=79)

        # SQL query to insert data into the Customers table
        query = f"INSERT INTO Customers ( CustomerID, FirstName, LastName, CNIC, Email, PhoneNumber, Street, City, Province, PostalCode, Gender, DateOfBirth) VALUES ( '{customerrr_count}','{first_name}', '{last_name}', '{cnic}', '{email}', '{phone_number}', '{street}', '{city}', '{province}', {postal_code}, '{gender}', '{date_of_birth}')"

        # Execute the query
        cursor.execute(query)


        # Insert fake data into the Orders table
        for asd in range(random.choice([1,1,1,1,2])):  # Adjust the number of records as needed

            customer_id = customerrr_count  # Assuming you have customers with IDs up to 100
            employee_id = random_employeeID  # Assuming you have employees with IDs up to 100
            order_date = current_date
            payment_method = random.choice(payment_methods)

            # SQL query to insert data into the Orders table
            query = f"INSERT INTO Orders ( CustomerID, EmployeeID, OrderDate, PaymentMethod) VALUES ({customer_id}, {employee_id}, '{order_date}', '{payment_method}')"

            # Execute the query
            cursor.execute(query)
            
    
            
            
        customerrr_count = customerrr_count+1
        
        
        
    daysss = daysss - 1 

    if daysss==1:
        break











# Commit the changes and close the connection
connection.commit()
connection.close()


