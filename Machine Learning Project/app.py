from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('regression_model.pkl')  # Ensure you save your trained model as 'regression_model.pkl'

@app.route('/')
def index():
    return app.send_static_file('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the request
        data = request.json
        feature1 = float(data.get('feature1', 0))
        feature2 = float(data.get('feature2', 0))

        # Predict using the loaded model
        prediction = model.predict(np.array([[feature1, feature2]]))[0]

        return jsonify({'prediction': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
