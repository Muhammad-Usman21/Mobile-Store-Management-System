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











# Insert fake data into the Customers table
for employee_count in range(40):  # Adjust the number of records as needed
    # employee_id  = fake.unique.random_int(min=1, max=1000000)
    # customer_id = fake.unique.random_number(digits=5)
    first_name = random.choice(pakistani_names)
    #first_name = fake.first_name()[:15]
    last_name = random.choice(male_names)
    #last_name = fake.last_name()[:15]
    # cnic = fake.unique.random_number(digits=13)
    cnic = f"{fake.random_number(digits=5):05d}-{fake.random_number(digits=7):07d}-{random.choice([1,2])}"
    #email = fake.email()[:50]
    email = f"{first_name}{last_name}{fake.random_int(min=99, max=99999)}@gmail.com"
    #phone_number = fake.phone_number()[:20]
    phone_number = f"+92 3{fake.random_number(digits=2):02d} {fake.random_number(digits=7):07d}"
    street = random.choice(pakistani_street_names)
    # street = fake.street_address()[:20]
    city = random.choice(pakistan_cities)
    # city = fake.city()[:20]
    province = random.choice(pakistan_provinces)
    # province = fake.state()[:20]
    postal_code = fake.zipcode()
    gender = fake.random_element(elements=('M', 'F'))
    date_of_birth = fake.date_of_birth(minimum_age=21, maximum_age=59)
    
    # position = random.choice(mobile_shop_job_titles)
    # position = fake.random_int(min=12, max=50)
    position = fake.random_int(min=2, max=13)
    # salary = f"{fake.random_int(min=4, max=15)}0000"
    
    #hireDate = fake.date_of_birth(minimum_age=18, maximum_age=80)
    #retireDate = fake.date_of_birth(minimum_age=18, maximum_age=80)
    #retireDate = fake.random_element(elements=(fake.date_of_birth(minimum_age=20, maximum_age=50), None))
    
    # Generate a random hire date (assuming within the last 20 years)
    #hireDate = fake.date_between(start_date='-20y', end_date='today')
    # Generate a random hire date (assuming after the date of birth)
    start_date=date_of_birth + timedelta(days=7300)
    if start_date >=  (datetime.now() - timedelta(days=1000)).date():
        hireDate = fake.date_between(start_date=date_of_birth + timedelta(days=7300), end_date='today')
    else :
        hireDate = fake.date_between(start_date= (datetime.now() - timedelta(days=1000)).date(), end_date='today')
    
    # Generate a random retire date (assuming within the next 20 years)
    # retireDate = fake.date_between(start_date=hireDate + timedelta(days=1), end_date='today')



    if fake.boolean(chance_of_getting_true=70):  # Adjust the chance_of_getting_true as needed
        # Generate a random retire date (assuming after the hire date)
        retireDate = fake.date_between(start_date=hireDate + timedelta(days=1), end_date="today")
    else:
        retireDate = None


    if retireDate == None:
        query = f"INSERT INTO Employees ( FirstName, LastName, CNIC, Email, PhoneNumber, Street, City, Province, PostalCode, Gender, DateOfBirth, HireDate, PositionID) VALUES ('{first_name}', '{last_name}', '{cnic}', '{email}', '{phone_number}', '{street}', '{city}', '{province}', {postal_code}, '{gender}', '{date_of_birth}', '{hireDate}', {position})"
    else: 
        # SQL query to insert data into the Customers table
        # query = f"INSERT INTO Employees (EmployeeID, FirstName, LastName, CNIC, Email, PhoneNumber, Street, City, Province, PostalCode, Gender, DateOfBirth, Position, Salary, HireDate, RetireDate) VALUES ({employee_id}, '{first_name}', '{last_name}', '{cnic}', '{email}', '{phone_number}', '{street}', '{city}', '{province}', {postal_code}, '{gender}', '{date_of_birth}', '{position}', {salary}, '{hireDate}', '{retireDate}')"
        query = f"INSERT INTO Employees (FirstName, LastName, CNIC, Email, PhoneNumber, Street, City, Province, PostalCode, Gender, DateOfBirth, HireDate, RetireDate) VALUES ('{first_name}', '{last_name}', '{cnic}', '{email}', '{phone_number}', '{street}', '{city}', '{province}', {postal_code}, '{gender}', '{date_of_birth}', '{hireDate}', '{retireDate}')"

    # Execute the query
    cursor.execute(query)












# Commit the changes and close the connection
connection.commit()
connection.close()


