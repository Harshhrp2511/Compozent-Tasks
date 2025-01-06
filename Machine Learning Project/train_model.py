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
    'location': [0, 0, 1, 1, 0, 1, 1],  # 0: City, 1: Suburb
    'age_of_house': [10, 15, 20, 5, 8, 3, 2],
    'floor_number': [1, 1, 2, 2, 3, 3, 4],
    'price': [500000, 600000, 750000, 850000, 1000000, 1200000, 1500000]
}

df = pd.DataFrame(data)

# Define features and target
X = df.drop(columns=['price'])
y = df['price']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Save the trained model
joblib.dump(model, 'house_price_model.pkl')
