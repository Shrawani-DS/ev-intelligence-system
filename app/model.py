import joblib
import pandas as pd

# Load model
model = joblib.load("model.pkl")

features = [
    "Motor_temp",
    "MCU_temp",
    "MCU_Voltage_DC",
    "MCU_AC_Current",
    "Speed"
]

def predict(data: dict):
    df = pd.DataFrame([data])
    df = df[features]

    pred = model.predict(df)[0]

    proba = model.predict_proba(df)[0]

    confidence = dict(zip(model.classes_, proba))

    return pred,confidence