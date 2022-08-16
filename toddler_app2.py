import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import sklearn

model = pickle.load(open('model.pickle','rb'))
st.header("Autism in Toddlers Prediction")
st.subheader("General Details of Toddler")
Gender = st.selectbox('Enter Gender of Toddler", ("Male","Female"))

if Gender == "Male":
    Gender = 1
else:
    Gender = 0

Jaundice= st.selectbox('Was the Toddler Diagnosed with Neonatal Jaundice",("Yes","No"))
Family = st.selectbox('Does he/she have a family member with ASD",("Yes","No"))
Age= st.selectbox('How old is the toddler?",(1,2,3))

st.subheader("Quantitative Checklist Questions")
st.write("Reply with 0 for Always/Usually and 1 for Rarely/Never")
AQ1= st.selectbox('How often does your toddler look at you when you call his/her name",("Always/Usually","Rarely/Never"))
AQ2= st.selectbox('How often does your toddler make eye contact",("Always/Usually","Rarely/Never"))
AQ3= st.selectbox('How often does your toddler point to indicate he/she wants something",("Always/Usually","Rarely/Never"))
AQ4= st.selectbox('How often does your toddler point to show interest",("Always/Usually","Rarely/Never"))
AQ5= st.selectbox('How often does your toddler play pretend",("Always/Usually","Rarely/Never"))
AQ6= st.selectbox('How often does your toddler follow where you are looking",("Always/Usually","Rarely/Never"))
AQ7= st.selectbox('How often does your toddler show signs of comfort to someone who is visibly upset",("Always/Usually","Rarely/Never"))
st.write("Reply with 0 for Typical and 1 for Unusual/Doesn't speak")
AQ8= st.selectbox('Describe your his/her first words",("Typical","Unusual/Doesn't Speak"))
if AQ8 == 'Typical':
    AQ8 = 0
else:
    AQ8 = 1
AQ9= st.selectbox('How often does your toddler use gestures e.g. waving goodbye",("Always/Usually","Rarely/Never"))

st.write("Reply with 1 for Always/Usually and 0 for Rarely/Never")
AQ10 = st.selectbox("How often does your toddler stare at nothing for no apparent reason",("Always/Usually","Rarely/Never"))
if AQ10 == "Always/Usually":
    AQ10 = 0
else: 
    AQ10 = 1


data = {'A1': AQ1,
        'A2':AQ2,
	'A3':AQ3,
	'A4':AQ4,
	'A5':AQ5,
	'A6':AQ6,
	'A7':AQ7,
	'A8':AQ8,
	'A9':AQ9,
	'A10':AQ10,
	'Gender':Gender,
	'Jaundice':Jaundice,
	'Family_Record_ASD':Family,
	'Age':Age}

features = pd.DataFrame(data, index=[0])
features = features.replace("Male", "Female", "Always/Usually", "Rarely/Never"], [1,0,0,1])

prediction = model.predict(features)
if prediction[0] == 0:
    value = "There is a low chance of ASD"
else:
    value = "There is a high chance of ASD"

st.write(features)

if st.button('Predict'):
     st.write(value)
else:
     st.write('Click to predict')
