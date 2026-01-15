import streamlit as st
import joblib
import numpy as np

model = joblib.load("model/solar_rf_small.pkl")

st.title("☀️ Solar Power Generation Prediction")

ambient = st.number_input("Ambient Temperature (°C)")
module = st.number_input("Module Temperature (°C)")
irradiation = st.number_input("Irradiation (W/m²)")
dc_power = st.number_input("DC Power (kW)")
daily_yield = st.number_input("Daily Yield (kWh)")

if st.button("Predict AC Power"):
    features = np.array([[ambient, module, irradiation, dc_power, daily_yield]])
    prediction = model.predict(features)
    st.success(f"Predicted AC Power: {prediction[0]:.2f} kW")
