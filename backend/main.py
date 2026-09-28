from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib


app = FastAPI(
    title="Used Car Price Prediction API",
    description="ML API for predicting used car selling price",
    version="1.0"
)


# Allow frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Load trained model and preprocessor
model = joblib.load("backend/model/car_price_model.pkl")
preprocessor = joblib.load("backend/model/preprocessor.pkl")


class CarDetails(BaseModel):
    Car_Age: int
    Kilometers_Driven: int
    Engine_Capacity: int
    Mileage: float
    Previous_Owners: int
    Fuel_Type: str
    Transmission: str
    Car_Brand: str


@app.get("/")
def home():
    return {
        "message": "Used Car Price Prediction API is running!"
    }


@app.post("/predict")
def predict_price(car: CarDetails):

    data = pd.DataFrame([{
        "Car_Age": car.Car_Age,
        "Kilometers_Driven": car.Kilometers_Driven,
        "Engine_Capacity": car.Engine_Capacity,
        "Mileage": car.Mileage,
        "Previous_Owners": car.Previous_Owners,
        "Fuel_Type": car.Fuel_Type,
        "Transmission": car.Transmission,
        "Car_Brand": car.Car_Brand
    }])


    # Preprocess input
    processed_data = preprocessor.transform(data)


    # Predict price
    prediction = model.predict(processed_data)[0]


    return {
        "predicted_price": round(float(prediction), 2),
        "currency": "INR",
        "input_summary": car.model_dump()
    }