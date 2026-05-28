
import streamlit as st

st.title("🧪 Kidney Disease Prediction")

bp = st.number_input("Blood Pressure")
sugar = st.number_input("Sugar Level")

if st.button("Predict"):
    st.success("Kidney Prediction Done")
