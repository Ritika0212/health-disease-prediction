import streamlit as st

st.title("🩸 Diabetes Prediction")

preg = st.number_input("Pregnancies")
glucose = st.number_input("Glucose Level")
bp = st.number_input("Blood Pressure")

if st.button("Predict"):
    st.success("Prediction Complete")
