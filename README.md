# 🚗 AutoPrice AI – Used Car Price Prediction

AutoPrice AI is an end-to-end Machine Learning project that predicts the estimated selling price of a used car based on its important features.

## 🎯 Objective

The main objective of this project is to build a Machine Learning system that estimates the selling price of a used car using:

- Car Age
- Kilometers Driven
- Engine Capacity
- Mileage
- Previous Owners
- Fuel Type
- Transmission
- Car Brand

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- FastAPI
- Streamlit
- HTML
- CSS
- JavaScript

## 📊 Dataset

The project uses a dataset containing **500 used-car records**.

The dataset is synthetically generated for educational purposes.

File:

`backend/dataset/used_car_data.csv`

## 🔄 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Duplicate Removal
4. Outlier Handling
5. Feature Selection
6. Train-Test Split
7. Model Building
8. Model Evaluation
9. Model Saving
10. Price Prediction
11. Web Application Integration

## 🤖 Machine Learning Model

The project uses **Linear Regression** for predicting the used car selling price.

The trained model and preprocessing pipeline are saved using Joblib.

Files:

- `backend/model/car_price_model.pkl`
- `backend/model/preprocessor.pkl`

## 📈 Model Evaluation

The model was evaluated using:

- MAE
- MSE
- RMSE
- R² Score

### Results

| Metric | Value |
|---|---:|
| MAE | 24246.50 |
| MSE | 792204431.21 |
| RMSE | 28146.13 |
| R² Score | 0.9786 |

The R² score of **0.9786** means that the model explained approximately 97.86% of the variation in the test-set prices for this dataset.

**Note:** Because the dataset is synthetically generated for educational purposes, these results should not be treated as real-world used-car price accuracy.

## 🌐 FastAPI Backend

FastAPI is used to create the prediction API.

Run the backend using:

```bash
uvicorn backend.main:app --reload