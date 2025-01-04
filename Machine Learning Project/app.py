from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('regression_model.pkl')

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the frontend
        data = request.json
        
        # Assuming you have the following input fields (e.g., number of rooms, square footage, etc.)
        feature1 = float(data.get('feature1'))  # E.g., number of rooms
        feature2 = float(data.get('feature2'))  # E.g., square footage
        feature3 = float(data.get('feature3'))  # Add more features as needed
        
        # Create a prediction using the model
        prediction = model.predict(np.array([[feature1, feature2, feature3]]))[0]
        
        # Return the prediction result
        return jsonify({'prediction': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
