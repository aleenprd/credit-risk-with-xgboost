# Credit Risk with XGBoost
For the purpose of predicting the probability that a borrower will default on their loan, I will train an XGBoost classifier to deploy as a service in Google Cloud Run, by using FastAPI and Docker, with GitHub actions for building and deploying to Artifact Registry.

<img src="https://miro.medium.com/max/3280/1*1kjLMDQMufaQoS-nNJfg1Q.png" alt="XGBoost Value" width=500>

## How to run the app
Clone the repository, install the dependencies with pip and run the app with: ```python -m uvicorn --app-dir src app:app --host 0.0.0.0 --port 5000 --workers 2```.

Alternatively, use docker to build and run the image: ```docker build . -t xgboostclassifier:latest``` and 
```docker run -p 5000:5000 -i -t xgboostclassifier:latest```  

In case you just want to use my service, I have made it publicly available over the internet. You can test the prediction endpoint with a JSON sample. You can either use a curl command like below or just navigate to the swagger page on https://xgboostclassifier-y2xu5uxlra-uc.a.run.app/docs and test the prediction endpoint.

```
curl -X 'POST' \
  'https://xgboostclassifier-y2xu5uxlra-uc.a.run.app/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "loan_amnt": 5000,
  "term": 36,
  "int_rate": 11.99,
  "installment": 166.05,
  "sub_grade": 11,
  "emp_length": 0,
  "is_mortgage": true,
  "is_rent": true,
  "is_own": true,
  "is_any": true,
  "is_other": true,
  "annual_inc": 0,
  "is_verified": true,
  "is_source_verified": true,
  "purpose": 1,
  "addr_state": 85,
  "dti": 14.42,
  "open_acc": 10,
  "pub_rec": 0,
  "revol_bal": 8495,
  "revol_util": 48.0,
  "mort_acc": 0,
  "age": 29,
  "pay_status": -2,
  "fico_score": 672.0
}'
```