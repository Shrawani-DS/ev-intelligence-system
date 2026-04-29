# ev-driving-behavior-ml-system

## Problem Statement
Build an EV intelligence system that:
- Predicts driving behavior (Eco, Normal, Aggressive)
- Estimates energy consumption
- Provides actionable recommendations
---

##  Approach
- Classification model for driving behavior
- SHAP for explainability
- FastAPI for backend
- Streamlit for frontend

---
## Why this project?

Electric vehicles generate large telemetry data.  
This system helps analyze driving patterns and improve efficiency.

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
## Architecture

- **Frontend**: Streamlit UI for user input  
- **Backend**: FastAPI handles API requests  
- **Model Layer**: Trained ML model for prediction  
- **Output**: Prediction + confidence + recommendations  

Flow:  
Streamlit → FastAPI → Model → Output

---

## Input Features
- Motor_temp → Motor operating temperature
- MCU_temp → Motor Controller temperature
- MCU_Voltage_DC → Voltage stability
- MCU_AC_Current → Controller AC Current
- Speed → Vehicle speed

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
}
```

---

## **How to run**

Run FastAPI
- **uvicorn app.main:app --reload**

Run Streamlit
- **streamlit run Streamlit_app/app.py**

**Explainability (SHAP)**
### Eco:
- Low current
- High voltage
- Low temperature

### Normal:
- Balanced values

### Aggressive:
- High current
- High temperature
- Voltage drop

---

## ** Key Learnings:**
- Handling class imbalance
- Model interpretability using SHAP
- Building APIs using FastAPI
- Creating UI using Streamlit
