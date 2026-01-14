import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("car data.csv")

# Encode categorical data
data.replace({
    'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2},
    'Seller_Type': {'Dealer': 0, 'Individual': 1},
    'Transmission': {'Manual': 0, 'Automatic': 1}
}, inplace=True)

X = data.drop(['Car_Name', 'Selling_Price'], axis=1)
y = data['Selling_Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("car_price_model.pkl", "wb"))

print("Model trained and saved successfully!")
