# credit-risk-with-xgboost
A binary classifier leveraging boosted trees.

<img src="https://miro.medium.com/max/3280/1*1kjLMDQMufaQoS-nNJfg1Q.png" alt="XGBoost Value" width=500>

Run the app with: ```python -m uvicorn --app-dir src app:app --host 0.0.0.0 --port 5000 --workers 2```

You can test the prediction endpoint with a JSON like:

{
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
}

### Docker
docker build . -t predictionapi:latest
docker run -p 5000:5000 -i -t predictionapi:latest   