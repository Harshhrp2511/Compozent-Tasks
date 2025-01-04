from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and label encoder
model = joblib.load('regression_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = request.form['gender']
        race_ethnicity = request.form['race_ethnicity']
        parental_education = request.form['parental_education']
        lunch = request.form['lunch']
        test_preparation = request.form['test_preparation']
        math_score = float(request.form['math_score'])
        reading_score = float(request.form['reading_score'])
        writing_score = float(request.form['writing_score'])

        # Preprocess the input data
        gender = label_encoder.transform([gender])[0]
        race_ethnicity = label_encoder.transform([race_ethnicity])[0]
        parental_education = label_encoder.transform([parental_education])[0]
        lunch = label_encoder.transform([lunch])[0]
        test_preparation = label_encoder.transform([test_preparation])[0]

        input_features = np.array([[gender, race_ethnicity, parental_education, lunch, test_preparation,
                                    math_score, reading_score, writing_score]])

        # Make prediction
        total_score = model.predict(input_features)
        return render_template('index.html', prediction_text='Predicted Total Score: {:.2f}'.format(total_score[0]))

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
