import streamlit as st

st.title("❤️ Heart Disease Prediction")

age = st.number_input("Age")
chol = st.number_input("Cholesterol")

if st.button("Predict"):
    st.success("Heart Prediction Done")