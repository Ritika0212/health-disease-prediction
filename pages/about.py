
import streamlit as st

st.set_page_config(page_title="About", page_icon="🩺")

st.title("🩺 About This Project")

st.markdown("---")

st.write("""
Welcome to the **Health Disease Prediction System** 💙

This project uses **Machine Learning** to predict different diseases
based on user health data.

The main purpose of this project is to provide:
- Fast health prediction
- Easy user interface
- Health awareness
- Simple medical analysis
""")

st.markdown("---")

st.subheader("🚀 Diseases Included")

st.write("""
✅ Diabetes Prediction  
✅ Heart Disease Prediction  
✅ Kidney Disease Prediction  
✅ BMI Calculator  
""")

st.markdown("---")

st.subheader("⚙️ Technologies Used")

st.write("""
- Python 🐍  
- Streamlit 🌐  
- Pandas 📊  
- NumPy 🔢  
- Scikit-learn 🤖  
""")

st.markdown("---")

st.info("💡 Note: This prediction system is for educational purposes only.")

st.markdown("---")

st.success("❤️ Stay Healthy & Take Care!")
