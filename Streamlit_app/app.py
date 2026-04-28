import streamlit as st
import requests

st.title("🚗 EV Driving Behavior Predictor")

st.markdown("Enter vehicle parameters:")

motor_temp = st.slider("Motor Temperature", 20, 100, 40)
mcu_temp = st.slider("MCU Temperature", 20, 100, 40)
voltage = st.slider("DC Voltage", 200, 400, 300)
current = st.slider("AC Current", 0, 300, 100)
speed = st.slider("Speed", 0, 150, 50)

if st.button("Predict Driving Behavior"):

    input_data = {
        "Motor_temp": motor_temp,
        "MCU_temp": mcu_temp,
        "MCU_Voltage_DC": voltage,
        "MCU_AC_Current": current,
        "Speed": speed
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=input_data
    )

    result = response.json()

    st.subheader(f"Prediction: {result['prediction']}")

    st.subheader("Recommendations:")
    for r in result["recommendations"]:
        st.write(f"- {r}")