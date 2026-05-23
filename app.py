import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("health_model.pkl", "rb"))

st.title("🩺 Health Disease Prediction App")

# Inputs
age = st.slider("Age", 18, 80)
bmi = st.number_input("BMI", 15.0, 40.0)
bp = st.number_input("Blood Pressure", 80, 200)
glucose = st.number_input("Glucose Level", 70, 200)
activity = st.selectbox("Physical Activity (0=No, 1=Yes)", [0, 1])

# Predict
if st.button("Predict"):
    input_data = np.array([[age, bmi, bp, glucose, activity]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Disease")
    else:
        st.success("✅ Low Risk (Healthy)")


