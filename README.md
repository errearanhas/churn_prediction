# Telco Customer Churn Prediction
## Building and deploy a machine learning model for Churn prediction

Customer churn occurs when customers stop using a company’s services. So, by monitoring churn, companies become prepared and can develop personalized customer retention campaigns.

Here, I use a machine learning to build a churn prediction model based on customer attributes from <a href="https://www.kaggle.com/blastchar/telco-customer-churn" target="_blank">Telco Customer dataset</a>. This dataset contains 7043 rows (customers) and 21 columns (features).

Also, the final model is deployed in production and can be tested <a href="https://telco-churn-app.herokuapp.com/" target="_blank">HERE<a/>. Just provide some data about a customer, and the system will classify it as CHURN or NO CHURN.
The application platform used was Heroku.

The project is organized as follows:

```
.
|-- README.md
|-- data
|   `-- Telco-Customer-Churn.txt
|-- deploy_heroku
|   |-- Procfile
|   |-- app.py
|   |-- churn_model.joblib
|   |-- churn_scaler.pkl
|   |-- requirements.txt
|   `-- templates
|       `-- index.html
|-- eda_and_model.ipynb
|-- requirements.txt
`-- test_request.py
```
