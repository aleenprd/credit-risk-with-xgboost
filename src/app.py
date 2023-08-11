import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, status
import uvicorn
from pydantic import BaseModel
from pathlib import Path

## path model
VERSION = "0.1.0"

## Create a instance 
app = FastAPI(
    title = "Credit Risk Prediction API",
    description = "An API that utilizes a Machine Learning model(XGBoost) to detect whether the borrower will default on the credit.",
    version = VERSION,
    debug = True
    )

BASE_DIR = Path(__file__).resolve(strict=True).parent
# Load Model
with open(f"{BASE_DIR}/model/xgboost_{VERSION}.pkl", "rb") as f:
    model = joblib.load(f)
    
## Schema validation
class Features(BaseModel):
    loan_amnt: int
    term: int
    int_rate: float
    installment: float
    sub_grade: int
    emp_length: int
    is_mortgage: bool
    is_rent: bool
    is_own: bool
    is_any: bool
    is_other: bool
    annual_inc: int
    is_verified: bool
    is_source_verified: bool
    purpose: int
    addr_state: int
    dti: float
    open_acc: int
    pub_rec: int
    revol_bal: int
    revol_util: float
    mort_acc: int
    age: int
    pay_status: int
    fico_score: float
    
# get path
@app.get("/")
def home():
    return {"health_check": "OK", "model_version": VERSION}

# Post path
@app.post("/predict", status_code= status.HTTP_201_CREATED)
def predict(data: Features):
    
    # Features
    features = data.dict()
    # Dataframe from features
    data_f = pd.DataFrame(features, index = [0])
    # predictions
    predictions = model.predict(data_f)

    proba = model.predict_proba(data_f)
    proba_no_default = np.round((proba[0][0])*100, 2)
    proba_default = np.round((proba[0][1])*100, 2)

    if predictions == 1:
        return {f"The probability that the customer defaults is {proba_default}%."}
    elif predictions == 0:
        return {f"The probability that the customer does not default is {proba_no_default}%."}