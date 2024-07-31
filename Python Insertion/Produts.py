import pyodbc
import random
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

# Other lists and data for generating fake product data
# shipment_ids = range(1, 101)  # Assuming you have 100 shipments
# # brands = ["Brand1", "Brand2", "Brand3"]  # Add more brands as needed
# mobile_brands = [
#     "Samsung", "Apple", "Huawei", "Xiaomi", "Sony", "LG", "Nokia", "Motorola", "HTC", "Google",
#     "OnePlus", "Asus", "Acer", "Infinix", "Realme", "Tecno", "Micromax", "Lava", "Gionee", "Vivo",
#     "Panasonic", "Sharp", "LeEco", "Umidigi", "Elephone", "BLU", "Coolpad", "Doogee", "Wileyfox",
#     "Vertu", "CAT", "Blackview"
# ]
# # models = ["ModelA", "ModelB", "ModelC"]  # Add more models as needed
# # Additional mobile phone brands and models
# google_models = ["Pixel 6 Pro", "Pixel 5a", "Pixel 4a", "Pixel 3 XL", "Nexus 6P"]
# sony_models = ["Xperia 1 III", "Xperia 5 III", "Xperia 10 III", "Xperia 1 II", "Xperia 5 II"]
# oppo_models = ["Find X3 Pro", "Reno6 Pro", "A74", "F19 Pro", "A53"]
# vivo_models = ["X60 Pro", "V21", "Y20", "S1 Pro", "Vivo X50 Pro"]
# motorola_models = ["Moto G Power", "Moto G Stylus", "Edge+", "Razr 5G", "Moto G Fast"]
# samsung_models = ["Galaxy S21", "Galaxy Note 20", "Galaxy A52", "Galaxy Z Fold 3", "Galaxy M32"]
# apple_models = ["iPhone 13 Pro", "iPhone 12 Mini", "iPhone SE (2020)", "iPhone 11", "iPhone XR"]
# xiaomi_models = ["Mi 11", "Redmi Note 10", "POCO X3", "Mi 10T Pro", "Redmi 9"]
# oneplus_models = ["OnePlus 9 Pro", "OnePlus 8T", "OnePlus Nord", "OnePlus 8", "OnePlus 7T"]
# huawei_models = ["P40 Pro", "Mate 40 Pro", "Nova 8", "P30 Lite", "Y9a"]
# # Combine all models into a single list
# all_mobile_models = samsung_models + apple_models + xiaomi_models + oneplus_models + huawei_models + google_models + sony_models + oppo_models + vivo_models + motorola_models




# # Mobile phone brands
# mobile_brandsx = ["Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Huawei", "Sony", "LG", "Motorola", "Nokia"]

# # Models for each brand
# brand_modelsx = {
#     "Apple": ["iPhone 13 Pro", "iPhone 13", "iPhone SE (2020)", "iPhone 12", "iPhone 11"],
#     "Samsung": ["Galaxy S21 Ultra", "Galaxy S21", "Galaxy Note 20 Ultra", "Galaxy A52", "Galaxy Z Fold 3"],
#     "Google": ["Pixel 6 Pro", "Pixel 6", "Pixel 5a", "Pixel 4a", "Pixel 4"],
#     "OnePlus": ["OnePlus 9 Pro", "OnePlus 9", "OnePlus 8T", "OnePlus Nord 2", "OnePlus 8"],
#     "Xiaomi": ["Xiaomi Mi 11 Ultra", "Xiaomi Mi 11", "Redmi Note 10 Pro", "Poco X3 Pro", "Redmi 9"],
#     "Huawei": ["Huawei P40 Pro", "Huawei Mate 40 Pro", "Huawei P30 Lite", "Huawei Nova 7i", "Huawei Y9 Prime"],
#     "Sony": ["Sony Xperia 1 III", "Sony Xperia 5 III", "Sony Xperia 10 III", "Sony Xperia 1 II", "Sony Xperia 5 II"],
#     "LG": ["LG Velvet", "LG Wing", "LG G8 ThinQ", "LG Stylo 6"],
#     "Motorola": ["Moto G Power (2021)", "Moto G Stylus (2021)", "Motorola Edge (2021)", "Moto G Fast"],
#     "Nokia": ["Nokia 8.3 5G", "Nokia 5.4", "Nokia 3.4", "Nokia 1.4"]
# }


mobile_brands_and_models = {
    "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52", "Galaxy M32", "Galaxy Z Fold 3", "Galaxy S20", "Galaxy A71", "Galaxy Note 10", "Galaxy Z Flip", "Galaxy A12", "Galaxy A32"],
    "Apple": ["iPhone 13 Pro", "iPhone 12", "iPhone SE", "iPhone 11", "iPhone XR", "iPhone 8", "iPhone XS", "iPhone 7", "iPhone 6S", "iPhone X", "iPhone 13 Mini"],
    "Xiaomi": ["Redmi Note 10", "Mi 11", "Redmi 9", "POCO X3", "Mi 10T Pro", "Redmi Note 8", "Mi 9T", "Mi 10", "POCO F3", "Redmi Note 9", "Mi Note 10"],
    "OnePlus": ["OnePlus 9 Pro", "OnePlus 8T", "OnePlus Nord", "OnePlus 9R", "OnePlus 8 Pro", "OnePlus 7T", "OnePlus 7 Pro", "OnePlus 6T", "OnePlus 6", "OnePlus 5T", "OnePlus 5"],
    "Google": ["Pixel 6 Pro", "Pixel 5a", "Pixel 4a", "Pixel 3 XL", "Pixel 2", "Pixel 3a", "Pixel 4", "Pixel 5", "Pixel 4 XL", "Pixel 3a XL", "Pixel 2 XL"],
    "Huawei": ["P40 Pro", "Mate 40", "Nova 8", "Honor 9X", "Y9 Prime", "P30 Pro", "Mate 30 Pro", "Nova 7i", "Honor 10", "Y7 Prime", "P20 Pro"],
    "Oppo": ["Find X3 Pro", "Reno 6 Pro", "A94", "F19 Pro", "A74", "Reno 5 Pro", "Find X2 Pro", "Reno 4 Pro", "A53", "A31", "Reno 3 Pro"],
    "Vivo": ["X60 Pro", "V21", "Y72", "iQOO 7", "Y31", "Vivo X50 Pro", "Vivo V20 Pro", "Y20", "iQOO Neo 5", "X50", "Vivo V15"],
    "Motorola": ["Moto G Power", "Moto G Stylus", "Moto G Play", "Moto G Fast", "Moto G9 Plus", "Moto E7", "Moto G10", "Moto G30", "Moto G100", "Moto Edge", "Moto G6"],
    "Sony": ["Xperia 1 III", "Xperia 5 III", "Xperia 10 III", "Xperia 1 II", "Xperia 5 II", "Xperia 10 II", "Xperia 1", "Xperia 5", "Xperia 10", "Xperia XZ3", "Xperia XZ2"],
    "LG": ["LG V60 ThinQ", "LG G8 ThinQ", "LG Velvet", "LG Stylo 6", "LG K92 5G", "LG Q92", "LG K51S", "LG K42", "LG WING", "LG G7 ThinQ", "LG V40 ThinQ"],
    "Nokia": ["Nokia 8.3", "Nokia 5.4", "Nokia 3.4", "Nokia 2.4", "Nokia 9 PureView", "Nokia 8.1", "Nokia 7.2", "Nokia 6.2", "Nokia 4.2", "Nokia 3.2", "Nokia 2.3"],
    "BlackBerry": ["BlackBerry KEY2", "BlackBerry KEY2 LE", "BlackBerry Evolve", "BlackBerry Motion", "BlackBerry KEYone", "BlackBerry DTEK60", "BlackBerry Priv", "BlackBerry Classic", "BlackBerry Passport", "BlackBerry Z30", "BlackBerry Q10"],
    "HTC": ["HTC U12+", "HTC U11", "HTC U Ultra", "HTC 10", "HTC Desire 20 Pro", "HTC U Play", "HTC Desire 10 Pro", "HTC One M9", "HTC One A9", "HTC Desire 626", "HTC One M8"],
    "Nubia": ["Nubia Red Magic 6 Pro", "Nubia Red Magic 6", "Nubia Red Magic 5G", "Nubia Red Magic 3", "Nubia Red Magic 2", "Nubia Z30 Pro", "Nubia Z30", "Nubia Z20", "Nubia Z18", "Nubia X", "Nubia Z17"],
    "Asus": ["Asus ROG Phone 5", "Asus ZenFone 7 Pro", "Asus ZenFone 6", "Asus ROG Phone 3", "Asus ZenFone 5Z", "Asus ROG Phone 2", "Asus ZenFone 4 Pro", "Asus ZenFone AR", "Asus ZenFone 3 Deluxe", "Asus ZenFone 2", "Asus ZenFone"],
    "Lenovo": ["Lenovo Legion Phone Duel 2", "Lenovo Legion Phone Duel", "Lenovo K12 Note", "Lenovo K10 Note", "Lenovo Z6 Pro", "Lenovo Z6 Lite", "Lenovo Z5 Pro", "Lenovo K9", "Lenovo K8 Note", "Lenovo K6 Note", "Lenovo P2"],
    "ZTE": ["ZTE Axon 30 Ultra", "ZTE Axon 20 5G", "ZTE Nubia Red Magic 6 Pro", "ZTE Nubia Red Magic 6", "ZTE Axon 11", "ZTE Nubia Red Magic 5S", "ZTE Axon 10 Pro", "ZTE Nubia Red Magic 3S", "ZTE Axon 9 Pro", "ZTE Nubia X", "ZTE Axon M"],
    "Alcatel": ["Alcatel 3L (2021)", "Alcatel 1S (2020)", "Alcatel 3X (2020)", "Alcatel 1V (2019)", "Alcatel 3 (2019)", "Alcatel 1X (2019)", "Alcatel 7", "Alcatel 1X Evolve", "Alcatel 3V (2018)", "Alcatel 1 (2019)", "Alcatel 5V"],
    "Realme": ["Realme GT", "Realme 8 Pro", "Realme Narzo 30 Pro", "Realme X7 Pro", "Realme 7", "Realme X50 Pro", "Realme 6 Pro", "Realme X2 Pro", "Realme 5 Pro", "Realme C15", "Realme 6"],
}


phone_descriptions = [
    "Latest tech, sleek design, powerful features",
    "Capture every detail with advanced camera",
    "Effortless multitasking, stunning visuals",
    "Stay connected and productive with sleek phone",
    "Elevate your mobile experience with flagship",
    "Slim, stylish, powerful - designed for excellence",
    "Unleash creativity with camera-centric phone",
    "5G-enabled, speed, innovation, cutting-edge",
    "Embrace sophistication with elegantly designed",
    "Powerful, stylish, feature-packed - your gateway",
    "Innovation meets style with our new device",
    "Seamless experience across entertainment",
    "Discover a world of possibilities with our phone",
    "Unlock new features with our advanced device",
    "Perfect blend of style and high performance",
    "Experience the future of connectivity",
    "Top-notch security, vivid display, advanced features",
    "Designed for excellence and maximum efficiency",
    "Captivate your senses with our latest device",
    "Precision and power in a compact design"
]


os_options = ["Android", "iOS", "Windows"]  # Add more OS options as needed
storage_options = ["32GB", "64GB", "128GB", "256GB"]  # Add more storage options as needed
ram_options = ["2GB","4GB", "8GB", "16GB"]  # Add more RAM options as needed
battery_options = ["3000mAh", "4000mAh", "5000mAh", "6000mAh"]  # Add more battery options as needed
camera_options = ["12 MP","16 MP","20 MP","24 MP","32 MP","48 MP","64 MP","108 MP","200 MP","256 MP"]  # Add more camera options as needed
display_options = [ "5.5 inches","6.0 inches","6.4 inches","6.7 inches","6.9 inches","7.2 inches","7.5 inches","8.0 inches","8.5 inches","9.0 inches",]  # Add more display options as needed
processor_options = [ "Snapdragon 888","Apple A15 Bionic","Exynos 2100","Dimensity 1200","Kirin 9000","Snapdragon 870","Apple A14 Bionic","Exynos 990","Dimensity 1100","Kirin 990","Snapdragon 765G","Apple A13 Bionic","Exynos 980","Dimensity 800U","Kirin 820","Snapdragon 730","Apple A12 Bionic","Exynos 9611","Helio G90T",]  # Add more processor options as needed
warranties = [ "6 months","8 months","10 months", '1 year', '1.5 year', '2 years' ]


# # Insert fake data into the Products table
# for count in range(100):  # Adjust the number of records as needed
#     # product_id = fake.unique.random_int(min=1, max=1000000)
#     # shipment_id = random.choice(shipment_ids)
#     # brand = random.choice(brands)
#     # brand = random.choice(mobile_brandsx)
#     brand = random.choice(list(mobile_brands_and_models.keys()))
#     # model_number = random.choice(models)
#     # model_number = f"{brand}:{random.choice(brand_modelsx.get(brand, []))}"
#     # model_number = f"{brand}:{random.choice(mobile_brands_and_models[brand])}"
#     model_number = random.choice(mobile_brands_and_models[brand])
    
#     unit_price = f'{fake.random_int(min=30, max=200)}000'  # Adjust the price range as needed
#     stock_quantity = fake.random_int(min=10, max=100)  # Adjust the stock quantity range as needed
#     description = random.choice(phone_descriptions)
#     os = random.choice(os_options)
#     storage = random.choice(storage_options)
#     ram = random.choice(ram_options)
#     battery = random.choice(battery_options)
#     camera = random.choice(camera_options)
#     display = random.choice(display_options)
#     processor = random.choice(processor_options)
#     warranty = random.choice(warranties)

#     # # SQL query to insert data into the Products table
#     # query = f"INSERT INTO Products (ProductID, ShipmentID, Brand, ModelNumber, UnitPrice, StockQuantity, Descriptionn, OS, Storage, RAM, Battery, Camera, Display, Processor) " \
#     #         f"VALUES ({product_id}, {shipment_id}, '{brand}', '{model_number}', {unit_price}, {stock_quantity}, '{description}', '{os}', '{storage}', '{ram}', '{battery}', '{camera}', '{display}', '{processor}')"
#     # SQL query to insert data into the Products table
#     query = f"INSERT INTO Products (ProductID, Brand, ModelNumber, UnitPrice, StockQuantity, Descriptionn, OS, Storage, RAM, Battery, Camera, Display, Processor) " \
#             f"VALUES ({count+101}, '{brand}', '{model_number}', {unit_price}, {stock_quantity}, '{os}', '{storage}', '{ram}', '{battery}', '{camera}', '{display}', '{processor}','{warranty}', '{description}')"

#     # Execute the query
#     cursor.execute(query)




# count =0
# Insert fake data into the Products table
for brand, models in mobile_brands_and_models.items():
    for model in models:    # product_id = fake.unique.random_int(min=1, max=1000000)
        # shipment_id = random.choice(shipment_ids)
        # brand = random.choice(brands)
        # brand = random.choice(mobile_brandsx)
        # brand = random.choice(list(mobile_brands_and_models.keys()))
        # model_number = random.choice(models)
        # model_number = f"{brand}:{random.choice(brand_modelsx.get(brand, []))}"
        # model_number = f"{brand}:{random.choice(mobile_brands_and_models[brand])}"
        # model_number = random.choice(mobile_brands_and_models[brand])
        
        unit_price = f'{fake.random_int(min=30, max=200)}000'  # Adjust the price range as needed
        # stock_quantity = fake.random_int(min=10, max=50)  # Adjust the stock quantity range as needed
        stock_quantity = 0
        description = random.choice(phone_descriptions)
        os = random.choice(os_options)
        storage = random.choice(storage_options)
        ram = random.choice(ram_options)
        battery = random.choice(battery_options)
        camera = random.choice(camera_options)
        display = random.choice(display_options)
        processor = random.choice(processor_options)
        warranty = random.choice(warranties)

        # # SQL query to insert data into the Products table
        # query = f"INSERT INTO Products (ProductID, ShipmentID, Brand, ModelNumber, UnitPrice, StockQuantity, Descriptionn, OS, Storage, RAM, Battery, Camera, Display, Processor) " \
        #         f"VALUES ({product_id}, {shipment_id}, '{brand}', '{model_number}', {unit_price}, {stock_quantity}, '{description}', '{os}', '{storage}', '{ram}', '{battery}', '{camera}', '{display}', '{processor}')"
        # SQL query to insert data into the Products table
        # query = f"INSERT INTO Products (ProductID, Brand, ModelNumber, UnitPrice, StockQuantity, OS, Storage, RAM, Battery, Camera, Display, Processor ,Warranty, Descriptionn) " \
        #         f"VALUES ({count+101}, '{brand}', '{model}', {unit_price}, {stock_quantity}, '{os}', '{storage}', '{ram}', '{battery}', '{camera}', '{display}', '{processor}','{warranty}', '{description}')"
        query = f"INSERT INTO Products (Brand, ModelNumber, UnitPrice, StockQuantity, OS, Storage, RAM, Battery, Camera, Display, Processor ,Warranty, Descriptionn) " \
                f"VALUES ('{brand}', '{model}', {unit_price}, {stock_quantity}, '{os}', '{storage}', '{ram}', '{battery}', '{camera}', '{display}', '{processor}','{warranty}', '{description}')"

        # Execute the query
        cursor.execute(query)
        
        # count = count+1




# Commit the changes and close the connection
connection.commit()
connection.close()









