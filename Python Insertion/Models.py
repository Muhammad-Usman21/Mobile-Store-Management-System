def convert_prices_to_int(mobile_brands_and_models):
    for brand, models_data in mobile_brands_and_models.items():
        for model, price in models_data["prices"].items():
            # Remove the dollar sign and convert the price to an integer
            models_data["prices"][model] = int(price.replace('$', ''))



mobile_brands_and_models = {
    
    "Samsung": {
        "models": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52", "Galaxy M32", "Galaxy Z Fold 3", "Galaxy S20", "Galaxy A71", "Galaxy Note 10", "Galaxy Z Flip", "Galaxy A12", "Galaxy A32"],
        "prices": {"Galaxy S21": "$799", "Galaxy Note 20": "$999", "Galaxy A52": "$349", "Galaxy M32": "$249", "Galaxy Z Fold 3": "$1799", "Galaxy S20": "$699", "Galaxy A71": "$449", "Galaxy Note 10": "$949", "Galaxy Z Flip": "$1299", "Galaxy A12": "$179", "Galaxy A32": "$279"},
    },
    "Apple": {
        "models": ["iPhone 13 Pro", "iPhone 12", "iPhone SE", "iPhone 11", "iPhone XR", "iPhone 8", "iPhone XS", "iPhone 7", "iPhone 6S", "iPhone X", "iPhone 13 Mini"],
        "prices": {"iPhone 13 Pro": "$1099", "iPhone 12": "$799", "iPhone SE": "$399", "iPhone 11": "$699", "iPhone XR": "$499", "iPhone 8": "$449", "iPhone XS": "$999", "iPhone 7": "$349", "iPhone 6S": "$249", "iPhone X": "$899", "iPhone 13 Mini": "$699"},
    },
    "Xiaomi": {
        "models": ["Redmi Note 10", "Mi 11", "Redmi 9", "POCO X3", "Mi 10T Pro", "Redmi Note 8", "Mi 9T", "Mi 10", "POCO F3", "Redmi Note 9", "Mi Note 10"],
        "prices": {"Redmi Note 10": "$199", "Mi 11": "$699", "Redmi 9": "$149", "POCO X3": "$249", "Mi 10T Pro": "$499", "Redmi Note 8": "$179", "Mi 9T": "$349", "Mi 10": "$599", "POCO F3": "$399", "Redmi Note 9": "$229", "Mi Note 10": "$479"},
    },
    "OnePlus": {
        "models": ["OnePlus 9 Pro", "OnePlus 8T", "OnePlus Nord", "OnePlus 9R", "OnePlus 8 Pro", "OnePlus 7T", "OnePlus 7 Pro", "OnePlus 6T", "OnePlus 6", "OnePlus 5T", "OnePlus 5"],
        "prices": {"OnePlus 9 Pro": "$899", "OnePlus 8T": "$749", "OnePlus Nord": "$499", "OnePlus 9R": "$549", "OnePlus 8 Pro": "$899", "OnePlus 7T": "$599", "OnePlus 7 Pro": "$669", "OnePlus 6T": "$549", "OnePlus 6": "$529", "OnePlus 5T": "$499", "OnePlus 5": "$479"},
    },


    "Google": {
        "models": ["Pixel 6 Pro", "Pixel 5a", "Pixel 4a", "Pixel 3 XL", "Pixel 2", "Pixel 3a", "Pixel 4", "Pixel 5", "Pixel 4 XL", "Pixel 3a XL", "Pixel 2 XL"],
        "prices": {"Pixel 6 Pro": "$899", "Pixel 5a": "$449", "Pixel 4a": "$349", "Pixel 3 XL": "$799", "Pixel 2": "$649", "Pixel 3a": "$399", "Pixel 4": "$799", "Pixel 5": "$699", "Pixel 4 XL": "$899", "Pixel 3a XL": "$449", "Pixel 2 XL": "$849"},
    },
    "Huawei": {
        "models": ["P40 Pro", "Mate 40", "Nova 8", "Honor 9X", "Y9 Prime", "P30 Pro", "Mate 30 Pro", "Nova 7i", "Honor 10", "Y7 Prime", "P20 Pro"],
        "prices": {"P40 Pro": "$999", "Mate 40": "$899", "Nova 8": "$549", "Honor 9X": "$299", "Y9 Prime": "$249", "P30 Pro": "$899", "Mate 30 Pro": "$799", "Nova 7i": "$349", "Honor 10": "$449", "Y7 Prime": "$199", "P20 Pro": "$699"},
    },
    "Oppo": {
        "models": ["Find X3 Pro", "Reno 6 Pro", "A94", "F19 Pro", "A74", "Reno 5 Pro", "Find X2 Pro", "Reno 4 Pro", "A53", "A31", "Reno 3 Pro"],
        "prices": {"Find X3 Pro": "$1099", "Reno 6 Pro": "$699", "A94": "$399", "F19 Pro": "$349", "A74": "$249", "Reno 5 Pro": "$499", "Find X2 Pro": "$899", "Reno 4 Pro": "$549", "A53": "$199", "A31": "$179", "Reno 3 Pro": "$449"},
    },
    "Vivo": {
        "models": ["X60 Pro", "V21", "Y72", "iQOO 7", "Y31", "Vivo X50 Pro", "Vivo V20 Pro", "Y20", "iQOO Neo 5", "X50", "Vivo V15"],
        "prices": {"X60 Pro": "$899", "V21": "$449", "Y72": "$279", "iQOO 7": "$599", "Y31": "$249", "Vivo X50 Pro": "$699", "Vivo V20 Pro": "$499", "Y20": "$179", "iQOO Neo 5": "$449", "X50": "$599", "Vivo V15": "$349"},
    },
    "Motorola": {
        "models": ["Moto G Power", "Moto G Stylus", "Moto G Play", "Moto G Fast", "Moto G9 Plus", "Moto E7", "Moto G10", "Moto G30", "Moto G100", "Moto Edge", "Moto G6"],
        "prices": {"Moto G Power": "$249", "Moto G Stylus": "$299", "Moto G Play": "$149", "Moto G Fast": "$199", "Moto G9 Plus": "$349", "Moto E7": "$129", "Moto G10": "$179", "Moto G30": "$249", "Moto G100": "$499", "Moto Edge": "$699", "Moto G6": "$199"},
    },


    "Sony": {
        "models": ["Xperia 1 III", "Xperia 5 III", "Xperia 10 III", "Xperia 1 II", "Xperia 5 II", "Xperia 10 II", "Xperia 1", "Xperia 5", "Xperia 10", "Xperia XZ3", "Xperia XZ2"],
        "prices": {"Xperia 1 III": "$1199", "Xperia 5 III": "$999", "Xperia 10 III": "$699", "Xperia 1 II": "$1099", "Xperia 5 II": "$899", "Xperia 10 II": "$499", "Xperia 1": "$999", "Xperia 5": "$799", "Xperia 10": "$399", "Xperia XZ3": "$699", "Xperia XZ2": "$549"},
    },
    "LG": {
        "models": ["LG V60 ThinQ", "LG G8 ThinQ", "LG Velvet", "LG Stylo 6", "LG K92 5G", "LG Q92", "LG K51S", "LG K42", "LG WING", "LG G7 ThinQ", "LG V40 ThinQ"],
        "prices": {"LG V60 ThinQ": "$899", "LG G8 ThinQ": "$699", "LG Velvet": "$599", "LG Stylo 6": "$249", "LG K92 5G": "$499", "LG Q92": "$349", "LG K51S": "$199", "LG K42": "$179", "LG WING": "$999", "LG G7 ThinQ": "$449", "LG V40 ThinQ": "$599"},
    },
    "Nokia": {
        "models": ["Nokia 8.3", "Nokia 5.4", "Nokia 3.4", "Nokia 2.4", "Nokia 9 PureView", "Nokia 8.1", "Nokia 7.2", "Nokia 6.2", "Nokia 4.2", "Nokia 3.2", "Nokia 2.3"],
        "prices": {"Nokia 8.3": "$699", "Nokia 5.4": "$299", "Nokia 3.4": "$199", "Nokia 2.4": "$149", "Nokia 9 PureView": "$699", "Nokia 8.1": "$399", "Nokia 7.2": "$349", "Nokia 6.2": "$249", "Nokia 4.2": "$179", "Nokia 3.2": "$129", "Nokia 2.3": "$99"},
    },
    "BlackBerry": {
        "models": ["BlackBerry KEY2", "BlackBerry KEY2 LE", "BlackBerry Evolve", "BlackBerry Motion", "BlackBerry KEYone", "BlackBerry DTEK60", "BlackBerry Priv", "BlackBerry Classic", "BlackBerry Passport", "BlackBerry Z30", "BlackBerry Q10"],
        "prices": {"BlackBerry KEY2": "$699", "BlackBerry KEY2 LE": "$499", "BlackBerry Evolve": "$599", "BlackBerry Motion": "$399", "BlackBerry KEYone": "$349", "BlackBerry DTEK60": "$299", "BlackBerry Priv": "$249", "BlackBerry Classic": "$199", "BlackBerry Passport": "$299", "BlackBerry Z30": "$199", "BlackBerry Q10": "$149"},
    },
    "HTC": {
        "models": ["HTC U12+", "HTC U11", "HTC U Ultra", "HTC 10", "HTC Desire 20 Pro", "HTC U Play", "HTC Desire 10 Pro", "HTC One M9", "HTC One A9", "HTC Desire 626", "HTC One M8"],
        "prices": {"HTC U12+": "$699", "HTC U11": "$599", "HTC U Ultra": "$499", "HTC 10": "$399", "HTC Desire 20 Pro": "$349", "HTC U Play": "$299", "HTC Desire 10 Pro": "$249", "HTC One M9": "$199", "HTC One A9": "$179", "HTC Desire 626": "$129", "HTC One M8": "$149"},
    },
    "Nubia": {
        "models": ["Nubia Red Magic 6 Pro", "Nubia Red Magic 6", "Nubia Red Magic 5G", "Nubia Red Magic 3", "Nubia Red Magic 2", "Nubia Z30 Pro", "Nubia Z30", "Nubia Z20", "Nubia Z18", "Nubia X", "Nubia Z17"],
        "prices": {"Nubia Red Magic 6 Pro": "$899", "Nubia Red Magic 6": "$699", "Nubia Red Magic 5G": "$599", "Nubia Red Magic 3": "$499", "Nubia Red Magic 2": "$399", "Nubia Z30 Pro": "$999", "Nubia Z30": "$799", "Nubia Z20": "$599", "Nubia Z18": "$499", "Nubia X": "$699", "Nubia Z17": "$499"},
    },
    "Asus": {
        "models": ["Asus ROG Phone 5", "Asus ZenFone 7 Pro", "Asus ZenFone 6", "Asus ROG Phone 3", "Asus ZenFone 5Z", "Asus ROG Phone 2", "Asus ZenFone 4 Pro", "Asus ZenFone AR", "Asus ZenFone 3 Deluxe", "Asus ZenFone 2", "Asus ZenFone"],
        "prices": {"Asus ROG Phone 5": "$999", "Asus ZenFone 7 Pro": "$699", "Asus ZenFone 6": "$499", "Asus ROG Phone 3": "$899", "Asus ZenFone 5Z": "$599", "Asus ROG Phone 2": "$699", "Asus ZenFone 4 Pro": "$399", "Asus ZenFone AR": "$299", "Asus ZenFone 3 Deluxe": "$499", "Asus ZenFone 2": "$299", "Asus ZenFone": "$199"},
    },

    "ZTE": {
        "models": ["ZTE Axon 30 Ultra", "ZTE Axon 20 5G", "ZTE Nubia Red Magic 6 Pro", "ZTE Nubia Red Magic 6", "ZTE Axon 11", "ZTE Nubia Red Magic 5S", "ZTE Axon 10 Pro", "ZTE Nubia Red Magic 3S", "ZTE Axon 9 Pro", "ZTE Nubia X", "ZTE Axon M"],
        "prices": {"ZTE Axon 30 Ultra": "$799", "ZTE Axon 20 5G": "$599", "ZTE Nubia Red Magic 6 Pro": "$899", "ZTE Nubia Red Magic 6": "$699", "ZTE Axon 11": "$499", "ZTE Nubia Red Magic 5S": "$599", "ZTE Axon 10 Pro": "$699", "ZTE Nubia Red Magic 3S": "$499", "ZTE Axon 9 Pro": "$599", "ZTE Nubia X": "$699", "ZTE Axon M": "$299"},
    },
    "Alcatel": {
        "models": ["Alcatel 3L (2021)", "Alcatel 1S (2020)", "Alcatel 3X (2020)", "Alcatel 1V (2019)", "Alcatel 3 (2019)", "Alcatel 1X (2019)", "Alcatel 7", "Alcatel 1X Evolve", "Alcatel 3V (2018)", "Alcatel 1 (2019)", "Alcatel 5V"],
        "prices": {"Alcatel 3L (2021)": "$149", "Alcatel 1S (2020)": "$99", "Alcatel 3X (2020)": "$129", "Alcatel 1V (2019)": "$79", "Alcatel 3 (2019)": "$99", "Alcatel 1X (2019)": "$69", "Alcatel 7": "$199", "Alcatel 1X Evolve": "$59", "Alcatel 3V (2018)": "$89", "Alcatel 1 (2019)": "$49", "Alcatel 5V": "$129"},
    },
    "Realme": {
        "models": ["Realme GT", "Realme 8 Pro", "Realme Narzo 30 Pro", "Realme X7 Pro", "Realme 7", "Realme X50 Pro", "Realme 6 Pro", "Realme X2 Pro", "Realme 5 Pro", "Realme C15", "Realme 6"],
        "prices": {"Realme GT": "$399", "Realme 8 Pro": "$249", "Realme Narzo 30 Pro": "$199", "Realme X7 Pro": "$299", "Realme 7": "$179", "Realme X50 Pro": "$499", "Realme 6 Pro": "$299", "Realme X2 Pro": "$399", "Realme 5 Pro": "$249", "Realme C15": "$129", "Realme 6": "$229"},
    },


    "Infinix": {
        "models": ["Infinix Zero 8", "Infinix Note 8", "Infinix Hot 10", "Infinix Smart 5", "Infinix S5 Pro", "Infinix Hot 9", "Infinix Note 7", "Infinix S4", "Infinix Hot 8", "Infinix Smart 4", "Infinix Hot 7"],
        "prices": {"Infinix Zero 8": "$249", "Infinix Note 8": "$199", "Infinix Hot 10": "$149", "Infinix Smart 5": "$99", "Infinix S5 Pro": "$129", "Infinix Hot 9": "$89", "Infinix Note 7": "$149", "Infinix S4": "$129", "Infinix Hot 8": "$79", "Infinix Smart 4": "$69", "Infinix Hot 7": "$59"},
    },
    "Tecno": {
        "models": ["Tecno Phantom X", "Tecno Camon 17 Pro", "Tecno Spark 7 Pro", "Tecno Pova 2", "Tecno Camon 16 Premier", "Tecno Spark 6", "Tecno Camon 15", "Tecno Spark 5", "Tecno Pouvoir 4 Pro", "Tecno Camon 12 Air", "Tecno Spark Go"],
        "prices": {"Tecno Phantom X": "$349", "Tecno Camon 17 Pro": "$229", "Tecno Spark 7 Pro": "$149", "Tecno Pova 2": "$129", "Tecno Camon 16 Premier": "$199", "Tecno Spark 6": "$99", "Tecno Camon 15": "$149", "Tecno Spark 5": "$89", "Tecno Pouvoir 4 Pro": "$129", "Tecno Camon 12 Air": "$79", "Tecno Spark Go": "$69"},
    },
    "Meizu": {
        "models": ["Meizu 18 Pro", "Meizu 17 Pro", "Meizu Note 9", "Meizu 16s Pro", "Meizu X8", "Meizu 16th", "Meizu Note 8", "Meizu 15", "Meizu M6T", "Meizu PRO 7 Plus", "Meizu M5c"],
        "prices": {"Meizu 18 Pro": "$899", "Meizu 17 Pro": "$799", "Meizu Note 9": "$299", "Meizu 16s Pro": "$599", "Meizu X8": "$349", "Meizu 16th": "$449", "Meizu Note 8": "$179", "Meizu 15": "$499", "Meizu M6T": "$129", "Meizu PRO 7 Plus": "$299", "Meizu M5c": "$99"},
    },
    "Lenovo": {
        "models": ["Lenovo Legion Phone Duel 2", "Lenovo Legion Phone Duel", "Lenovo K12 Note", "Lenovo K10 Note", "Lenovo Z6 Pro", "Lenovo Z6 Lite", "Lenovo Z5 Pro", "Lenovo K9", "Lenovo K8 Note", "Lenovo K6 Note", "Lenovo P2"],
        "prices": {"Lenovo Legion Phone Duel 2": "$999", "Lenovo Legion Phone Duel": "$799", "Lenovo K12 Note": "$249", "Lenovo K10 Note": "$299", "Lenovo Z6 Pro": "$499", "Lenovo Z6 Lite": "$249", "Lenovo Z5 Pro": "$399", "Lenovo K9": "$199", "Lenovo K8 Note": "$249", "Lenovo K6 Note": "$199", "Lenovo P2": "$299"},
    },
    "Gionee": {
        "models": ["Gionee M12", "Gionee S12 Lite", "Gionee Max", "Gionee K30 Pro", "Gionee M30", "Gionee S11 Lite", "Gionee P10", "Gionee M7 Power", "Gionee S10 Lite", "Gionee M6", "Gionee S6 Pro"],
        "prices": {"Gionee M12": "$179", "Gionee S12 Lite": "$129", "Gionee Max": "$79", "Gionee K30 Pro": "$199", "Gionee M30": "$149", "Gionee S11 Lite": "$99", "Gionee P10": "$69", "Gionee M7 Power": "$129", "Gionee S10 Lite": "$89", "Gionee M6": "$199", "Gionee S6 Pro": "$149"},
    },
    "Honor": {
        "models": ["Honor 50 Pro", "Honor 30 Pro", "Honor 20S", "Honor 9X Lite", "Honor 20 Pro", "Honor 9X", "Honor 10 Lite", "Honor 8X", "Honor View 20", "Honor 7X", "Honor 6X"],
        "prices": {"Honor 50 Pro": "$599", "Honor 30 Pro": "$499", "Honor 20S": "$349", "Honor 9X Lite": "$199", "Honor 20 Pro": "$599", "Honor 9X": "$249", "Honor 10 Lite": "$199", "Honor 8X": "$179", "Honor View 20": "$399", "Honor 7X": "$129", "Honor 6X": "$99"},
    },
    "Sharp": {
        "models": ["Sharp Aquos R6", "Sharp Aquos Zero 2", "Sharp Aquos S3", "Sharp Aquos R2 Compact", "Sharp Aquos S2", "Sharp Aquos R", "Sharp Aquos Crystal", "Sharp Aquos Zeta", "Sharp Aquos XX3", "Sharp Aquos Xx", "Sharp Aquos C10"],
        "prices": {"Sharp Aquos R6": "$899", "Sharp Aquos Zero 2": "$799", "Sharp Aquos S3": "$499", "Sharp Aquos R2 Compact": "$399", "Sharp Aquos S2": "$349", "Sharp Aquos R": "$299", "Sharp Aquos Crystal": "$199", "Sharp Aquos Zeta": "$349", "Sharp Aquos XX3": "$299", "Sharp Aquos Xx": "$249", "Sharp Aquos C10": "$179"},
    },
    "Panasonic": {
        "models": ["Panasonic Eluga X1 Pro", "Panasonic P85 NXT", "Panasonic Eluga Ray 810", "Panasonic Eluga Z1 Pro", "Panasonic Eluga X1", "Panasonic P100", "Panasonic Eluga Ray 700", "Panasonic Eluga I9", "Panasonic Eluga Ray 500", "Panasonic Eluga A4", "Panasonic P71"],
        "prices": {"Panasonic Eluga X1 Pro": "$299", "Panasonic P85 NXT": "$129", "Panasonic Eluga Ray 810": "$149", "Panasonic Eluga Z1 Pro": "$199", "Panasonic Eluga X1": "$249", "Panasonic P100": "$79", "Panasonic Eluga Ray 700": "$99", "Panasonic Eluga I9": "$89", "Panasonic Eluga Ray 500": "$69", "Panasonic Eluga A4": "$129", "Panasonic P71": "$59"},
    },


}





# Call the function to convert prices to integers
convert_prices_to_int(mobile_brands_and_models)

# Print the updated dictionary with integer prices
print(mobile_brands_and_models)
