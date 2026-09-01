import streamlit as st
import pandas as pd
import joblib

# The model was trained on these 5 features, in this exact order.
FEATURES = ["IRRADIATION", "DC_lag_1", "DC_lag_24", "DC_roll_3", "MODULE_TEMPERATURE"]

model = joblib.load("model/solar_rf_small.pkl")

st.title(" Solar Power Generation Prediction")
st.caption(
    "Predicts **DC power output** for a solar plant using current weather readings "
    "and recent power history. Trained on Plant 1 & 2 generation and weather sensor data."
)

st.subheader("Current sensor readings")
irradiation = st.number_input("Irradiation (W/m²)", min_value=0.0, value=0.60, step=0.05)
module_temp = st.number_input("Module temperature (°C)", min_value=0.0, value=45.0, step=0.5)

st.subheader("Recent power history")
st.caption("Readings are taken every 15 minutes.")
dc_lag_1 = st.number_input("DC power 15 minutes ago (kW)", min_value=0.0, value=6000.0, step=100.0)
dc_roll_3 = st.number_input("Average DC power over the last 45 minutes (kW)", min_value=0.0, value=5800.0, step=100.0)
dc_lag_24 = st.number_input("DC power 6 hours ago (kW)", min_value=0.0, value=3000.0, step=100.0)

if st.button("Predict DC Power"):
    # Build a DataFrame with named columns so scikit-learn validates the feature
    # names and order. Passing a bare numpy array would silently accept wrong columns.
    X = pd.DataFrame([[irradiation, dc_lag_1, dc_lag_24, dc_roll_3, module_temp]],
                     columns=FEATURES)
    prediction = model.predict(X)[0]
    st.success(f"Predicted DC Power: {prediction:.2f} kW")

    with st.expander("Model inputs"):
        st.dataframe(X.T.rename(columns={0: "value"}))
