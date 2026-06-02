import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("final_model.pkl", "rb"))

st.title("Diabetes Prediction App")

st.write("Enter patient details below:")

Pregnancies = st.number_input("Pregnancies", 0, 20)
Glucose = st.number_input("Glucose", 0, 200)
BloodPressure = st.number_input("Blood Pressure", 0, 150)
SkinThickness = st.number_input("Skin Thickness", 0, 100)
Insulin = st.number_input("Insulin", 0, 900)
BMI = st.number_input("BMI", 0.0, 70.0)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
Age = st.number_input("Age", 1, 120)

# Prediction button
if st.button("Predict"):

    input_data = np.array([[
        Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Person is likely to have Diabetes")
    else:
        st.success("Person is unlikely to have Diabetes")