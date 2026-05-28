import streamlit as st

st.title("⚖️ BMI Calculator")

weight = st.number_input("Weight (kg)")
height = st.number_input("Height (m)")

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write("BMI:", round(bmi, 2))