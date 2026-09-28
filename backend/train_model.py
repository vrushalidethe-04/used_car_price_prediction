import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load dataset
df = pd.read_csv("backend/dataset/used_car_data.csv")

print("Original dataset shape:", df.shape)


# 2. Remove duplicate records
df = df.drop_duplicates()

print("After removing duplicates:", df.shape)


# 3. Handle outliers using IQR
numeric_columns = [
    "Car_Age",
    "Kilometers_Driven",
    "Engine_Capacity",
    "Mileage",
    "Previous_Owners",
    "Selling_Price"
]

for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[
        (df[column] >= lower) &
        (df[column] <= upper)
    ]

print("After outlier handling:", df.shape)


# 4. Selected features
features = [
    "Car_Age",
    "Kilometers_Driven",
    "Engine_Capacity",
    "Mileage",
    "Previous_Owners",
    "Fuel_Type",
    "Transmission",
    "Car_Brand"
]

target = "Selling_Price"

X = df[features]
y = df[target]

print("Selected features:", features)


# 5. Numerical and categorical columns
numeric_features = [
    "Car_Age",
    "Kilometers_Driven",
    "Engine_Capacity",
    "Mileage",
    "Previous_Owners"
]

categorical_features = [
    "Fuel_Type",
    "Transmission",
    "Car_Brand"
]


# 6. Preprocessing
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])


# 7. Transform data
X_processed = preprocessor.fit_transform(X)


# 8. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_processed,
    y,
    test_size=0.20,
    random_state=42
)


# 9. Build Linear Regression model
model = LinearRegression()

model.fit(X_train, y_train)


# 10. Predictions
y_pred = model.predict(X_test)


# 11. Model evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print("\n========== MODEL EVALUATION ==========")
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))
print("=======================================")


# 12. Save model and preprocessor
joblib.dump(
    model,
    "backend/model/car_price_model.pkl"
)

joblib.dump(
    preprocessor,
    "backend/model/preprocessor.pkl"
)


# 13. Save evaluation results
with open("backend/model/evaluation_results.txt", "w") as file:
    file.write("Used Car Price Prediction - Model Evaluation\n")
    file.write("============================================\n")
    file.write(f"MAE  : {mae:.2f}\n")
    file.write(f"MSE  : {mse:.2f}\n")
    file.write(f"RMSE : {rmse:.2f}\n")
    file.write(f"R2 Score : {r2:.4f}\n")


print("\nModel saved successfully!")
print("Preprocessor saved successfully!")
print("Evaluation results saved successfully!")