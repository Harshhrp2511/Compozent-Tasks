import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# Preprocess the data
label_encoder = LabelEncoder()
df['gender'] = label_encoder.fit_transform(df['gender'])  # Male: 1, Female: 0
df['race/ethnicity'] = label_encoder.fit_transform(df['race/ethnicity'])
df['parental level of education'] = label_encoder.fit_transform(df['parental level of education'])
df['lunch'] = label_encoder.fit_transform(df['lunch'])
df['test preparation course'] = label_encoder.fit_transform(df['test preparation course'])

# Define features and target
X = df[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score', 'reading score', 'writing score']]
y = df['math score'] + df['reading score'] + df['writing score']  # Total score

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model and label encoder
joblib.dump(model, 'regression_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')  # Save the label encoder

print("Model and LabelEncoder saved successfully.")
