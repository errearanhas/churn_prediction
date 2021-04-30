import requests

# url = "http://localhost:5000/results"
url = "https://telco-churn-app.herokuapp.com/results"

r = requests.post(url,
                  json={"SeniorCitizen": 0.0, 
                        "Partner": 0.0, 
                        "Dependents": 0.0, 
                        "OnlineSecurity": 0.0, 
                        "OnlineBackup": 0.0, 
                        "DeviceProtection": 0.0, 
                        "TechSupport": 0.0, 
                        "Contract": 0.0, 
                        "PaperlessBilling": 1.0, 
                        "PaymentMethod": 2.0, 
                        "MonthlyCharges": 70.7, 
                        "TotalCharges": 151.64999389648438})

print(r.json())
