from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('house_price_model.pkl')

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        square_feet = float(data.get('square_feet'))
        bedrooms = int(data.get('bedrooms'))
        bathrooms = int(data.get('bathrooms'))
        location = int(data.get('location'))  
        age_of_house = int(data.get('age_of_house'))
        floor_number = int(data.get('floor_number'))
        features = np.array([[square_feet, bedrooms, bathrooms, location, age_of_house, floor_number]])
        prediction = model.predict(features)[0]

        return jsonify({'prediction': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
