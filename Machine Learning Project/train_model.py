import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Sample house pricing dataset (replace with your own dataset if available)
data = {
    'square_feet': [1500, 1800, 2400, 3000, 3500, 4000, 5000],
    'bedrooms': [3, 3, 4, 4, 5, 5, 6],
    'bathrooms': [2, 2, 3, 3, 4, 4, 5],
    'location': ['city', 'city', 'suburb', 'suburb', 'city', 'city', 'suburb'],
    'age_of_house': [5, 10, 15, 5, 2, 3, 20],
    'floor_number': [2, 3, 1, 3, 2, 4, 2],
    'price': [400000, 500000, 600000, 650000, 700000, 750000, 800000]  # price in INR (Indian Rupees)
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical features like 'location' (you can use more advanced encoding methods)
df['location'] = df['location'].map({'city': 0, 'suburb': 1})

# Define features (X) and target variable (y)
X = df[['square_feet', 'bedrooms', 'bathrooms', 'location', 'age_of_house', 'floor_number']]
y = df['price']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model using Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Save the trained model
joblib.dump(model, 'house_price_model.pkl')
print("Model saved as 'house_price_model.pkl'.")
