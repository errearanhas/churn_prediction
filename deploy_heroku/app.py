import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)
gen_features = joblib.load('churn_new_features.pkl')
churn_model = joblib.load('churn_model.joblib')

def return_prediction(model, gen_features, customer_json):
    
    json = gen_features.transform(customer_json)

    sample = [i for i in json.values()]

    customer = np.array(sample).reshape(-1,15)
        
    classes = np.array(['NO CHURN', 'CHURN'])

    class_ind = (model.predict(customer) > 0.5)*1
    
    return classes[class_ind][0]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = request.form
    prediction = return_prediction(churn_model, gen_features, features)

    return render_template('index.html',
                           provided_data = f'Provided data: {features}',
                           prediction_text = f'Prediction: {prediction}')

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = return_prediction(churn_model, gen_features, data)

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
