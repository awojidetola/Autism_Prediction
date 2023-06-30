import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import sklearn


st.header("Autism in Toddlers Prediction")

st.markdown('''
This web application is based on my research paper on the topic: "Evaluation of Autism Spectrum Disorder Diagnosis using Machine Learning Models."

The Web Application aims to predict the diagnosis of toddlers based on their personal details and there response
to the quantitative checklist (Q- CHAT-10 ) questions. The data used for this project was collected from [Kaggle](https://www.kaggle.com/datasets/fabdelja/autism-screening-for-toddlers) and has its origin from Dr. Fadi Thabtah of Manukau Institute of Technology. 

The full codes and dataset used for the project can be found on [Github](https://github.com/awojidetola/Autism_Prediction).

''')

model = pickle.load(open('model.pickle','rb'))

st.subheader("General Details of Toddler")
Sex = st.selectbox("Enter Gender of Toddler", ("Male","Female"))

if Sex == "Male":
    Sex = 1
else:
    Sex = 0

Jaundice= st.selectbox("Was the Toddler Diagnosed with Neonatal Jaundice",("Yes","No"))
Family_mem_with_ASD = st.selectbox("Does he/she have a family member with ASD",("Yes","No"))
Age_Years= st.selectbox("How old is the toddler?",(1,2,3))

st.subheader("Quantitative Checklist Questions")
AQ1= st.selectbox("How often does your toddler look at you when you call his/her name",("Always/Usually","Rarely/Never"))
AQ2= st.selectbox("How often does your toddler make eye contact",("Always/Usually","Rarely/Never"))
AQ3= st.selectbox("How often does your toddler point to indicate he/she wants something",("Always/Usually","Rarely/Never"))
AQ4= st.selectbox("How often does your toddler point to show interest",("Always/Usually","Rarely/Never"))
AQ5= st.selectbox("How often does your toddler play pretend",("Always/Usually","Rarely/Never"))
AQ6= st.selectbox("How often does your toddler follow where you are looking",("Always/Usually","Rarely/Never"))
AQ7= st.selectbox("How often does your toddler show signs of comfort to someone who is visibly upset",("Always/Usually","Rarely/Never"))

AQ8= st.selectbox("Describe your his/her first words",("Typical","Unusual/Doesn't Speak"))
if AQ8 == 'Typical':
    AQ8 = 0
else:
    AQ8 = 1
AQ9= st.selectbox("How often does your toddler use gestures e.g. waving goodbye",("Always/Usually","Rarely/Never"))

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
	'Sex':Sex,
	'Jaundice':Jaundice,
	'Family_mem_with_ASD':Family_mem_with_ASD,
	'Age_Years':Age_Years}

features = pd.DataFrame(data, index=[0])
features = features.replace(["Yes", "No", "Always/Usually", "Rarely/Never"], [1,0,0,1])

prediction = model.predict(features)
if prediction[0] == 0:
    value = "There is a low chance your toddler has ASD"
else:
    value = "There is a high chance your toddler has ASD"

if st.button('Predict'):
    st.write(value)
else:
    st.write('Click to predict')
