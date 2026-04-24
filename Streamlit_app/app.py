import streamlit as st
import requests

st.title("EV Driving Behavior App")

torque = st.slider("Torque Load", 0.0, 1.0, 0.3)
current = st.slider("MCU Current", 0, 300, 100)
speed = st.slider("Speed", 0, 120, 40)

if st.button("Predict"):

    response = requests.post(
        "http://localhost:8000/predict",
        json={
            "Torque_Load": torque,
            "MCU_Current_DC": current,
            "Speed": speed
        }
    )

    result = response.json()

st.write("Prediction:", result["prediction"])
st.write("Recommendations:", result["recommendations"])