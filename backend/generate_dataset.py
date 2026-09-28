import pandas as pd
import numpy as np

np.random.seed(42)

brands = [
    "Maruti", "Hyundai", "Tata", "Honda",
    "Toyota", "Mahindra", "Kia", "Renault"
]

fuel_types = ["Petrol", "Diesel", "CNG"]
transmissions = ["Manual", "Automatic"]

data = []

for i in range(500):

    car_age = np.random.randint(1, 12)
    kilometers = np.random.randint(5000, 150000)
    engine = np.random.choice([800, 1000, 1200, 1500, 1600, 2000])
    mileage = np.round(np.random.uniform(12, 25), 1)
    previous_owners = np.random.randint(1, 4)
    fuel = np.random.choice(fuel_types)
    transmission = np.random.choice(transmissions)
    brand = np.random.choice(brands)

    base_price = {
        "Maruti": 500000,
        "Hyundai": 550000,
        "Tata": 520000,
        "Honda": 650000,
        "Toyota": 750000,
        "Mahindra": 600000,
        "Kia": 700000,
        "Renault": 480000
    }[brand]

    price = (
        base_price
        - (car_age * 30000)
        - (kilometers * 1.5)
        + (engine * 250)
        + (mileage * 8000)
        - (previous_owners * 25000)
    )

    if fuel == "Diesel":
        price += 50000
    elif fuel == "CNG":
        price += 25000

    if transmission == "Automatic":
        price += 80000

    price += np.random.randint(-50000, 50000)

    price = max(price, 100000)

    data.append([
        car_age,
        kilometers,
        engine,
        mileage,
        previous_owners,
        fuel,
        transmission,
        brand,
        round(price, 0)
    ])

columns = [
    "Car_Age",
    "Kilometers_Driven",
    "Engine_Capacity",
    "Mileage",
    "Previous_Owners",
    "Fuel_Type",
    "Transmission",
    "Car_Brand",
    "Selling_Price"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv(
    "backend/dataset/used_car_data.csv",
    index=False
)

print("Dataset created successfully!")
print("Total records:", len(df))
print("\nFirst 5 records:")
print(df.head())