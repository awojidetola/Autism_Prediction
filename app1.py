import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model.pickle','rb'))
st.header("Autism in Toddlers Prediction")
st.subheader("General Details of Toddler")
Gender = st.number_input('Enter Gender of Toddler, 1: Male, 0: Female', min_value=0, max_value=1, )
Jaundice= st.number_input('Was the Toddler Diagnosed with Neonatal Jaundice, 1: Yes, 0: No', min_value=0, max_value=1, )
Family = st.number_input('Does he/she have a family member with ASD, 1: Yes, 0:No', min_value=0, max_value=1, )
Age= st.number_input('How old is the toddler?', min_value=1, max_value=3, )

st.subheader("Quantitative Checklist Questions")
st.write("Reply with 0 for Always/Usually and 1 for Rarely/Never")
AQ1= st.number_input('How often does your toddler look at you when you call his/her name', min_value=0, max_value=1, )
AQ2= st.number_input('How often does your toddler make eye contact', min_value=0, max_value=1, )
AQ3= st.number_input('How often does your toddler point to indicate he/she wants something', min_value=0, max_value=1, )
AQ4= st.number_input('How often does your toddler point to show interest', min_value=0, max_value=1, )
AQ5= st.number_input('How often does your toddler play pretend', min_value=0, max_value=1, )
AQ6= st.number_input('How often does your toddler follow where you are looking', min_value=0, max_value=1, )
AQ7= st.number_input('How often does your toddler show signs of comfort to someone who is visibly upset', min_value=0, max_value=1, )
st.write("Reply with 0 for Typical and 1 for Unusual/Doesn't speak")
AQ8= st.number_input('Describe your his/her first words', min_value=0, max_value=1, )
st.write("Reply with 0 for Always/Usually and 1 for Rarely/Never")
AQ9= st.number_input('How often does your toddler use gestures e.g. waving goodbye', min_value=0, max_value=1, )
st.write("Reply with 1 for Always/Usually and 0 for Rarely/Never")
AQ10 = st.number_input("How often does your toddler stare at nothing for no apparent reason", min_value=0, max_value=1,)


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

prediction = model.predict(features)
if prediction[0] == 0:
    value = "There is a low chance of ASD"
else:
    value = "There is a high chance of ASD"

if st.button('Predict'):
     st.write(value)
else:
     st.write('Click to predict')
