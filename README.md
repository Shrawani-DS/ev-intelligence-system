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
