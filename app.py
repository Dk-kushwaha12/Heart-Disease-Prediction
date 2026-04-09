import streamlit as st
import numpy as np
import pickle

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Heart Disease Predictor")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details to predict heart disease risk")

# -------- INPUT FIELDS -------- #

age = st.number_input("Age", 20, 100)
sex = st.selectbox("Sex", [0, 1])  # 0 = Female, 1 = Male
cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200)
chol = st.number_input("Cholesterol", 100, 400)
fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])
restecg = st.selectbox("Rest ECG (0-2)", [0,1,2])
thalach = st.number_input("Max Heart Rate", 60, 220)
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("Oldpeak", 0.0, 6.0)
slope = st.selectbox("Slope (0-2)", [0,1,2])
ca = st.selectbox("Number of Vessels (0-3)", [0,1,2,3])
thal = st.selectbox("Thal (0-3)", [0,1,2,3])

# -------- PREDICTION -------- #

if st.button("Predict"):
    
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])
    
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")