import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
churn_scaler = joblib.load("churn_scaler.pkl")
churn_model = joblib.load('churn_model.joblib')

def return_prediction(model, scaler, customer_json):
            
    sample = [i for i in customer_json.values()]
    customer = np.array(sample).reshape(-1,12)
    
    scaled_customer = scaler.transform(customer)
    
    classes = np.array(['NO CHURN', 'CHURN'])
    
    class_ind = (model.predict(scaled_customer) > 0.5)*1
    
    return classes[class_ind][0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = request.form
    prediction = return_prediction(churn_model, churn_scaler, features)

    return render_template('index.html',
                           provided_data = f'provided data: {features}',
                           prediction_text = f'prediction: {prediction}')

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = return_prediction(churn_model, churn_scaler, data)

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)