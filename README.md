# EV Intelligence System

## Problem Statement
Build an EV intelligence system that:
- Predicts driving behavior (Eco, Normal, Aggressive)
- Provides actionable recommendations

---

##  Approach
- Classification model for driving behavior
- SHAP for explainability
- FastAPI for backend
- Streamlit for frontend

---

##  Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
- SHAP

---

## Features
- Real-time prediction via API
- Interactive UI (Streamlit)
- Driving recommendations
- Model explainability

---

## Input Features
- Motor_temp
- MCU_temp
- MCU_Voltage_DC
- MCU_AC_Current
- Speed

---

## Sample Output

```json
{
  "prediction": "Normal",
  "confidence": {
    "Eco": 0.32,
    "Normal": 0.58,
    "Aggressive": 0.10
  },
  "recommendations": [
    "Maintain moderate speed",
    "Balanced driving"
  ]
}```


## **How to run**

Run FastAPI
uvicorn app.main:app --reload

Run Streamlit
streamlit run Streamlit_app/app.py

Explainability (SHAP)
Eco → Low current, high voltage, low temperature
Normal → Balanced values
Aggressive → High current, high temperature

** Key Learnings:**
Handling class imbalance
Model interpretability using SHAP
Building APIs using FastAPI
Creating UI using Streamlit
