import streamlit as st
import pandas as pd
import pickle
st.write("""
# SVM implementation app
 """)
svm_classifier = open('mdl.pkl','rb')
classifier = pickle.load(svm_classifier)

#GRE Score,TOEFL Score,University Rating,SOP,LOR,CGPA,Research
GRE = st.text_input("Enter GRE Score( out of 340 ) : ",)
TOEFL = st.text_input("Enter TOEFL Score( out of 120 ) : ")
UR =  st.text_input("Enter University Rating( out of 5 ) : ")
SOP = st.text_input("Enter Statement of Purpose strength( out of 5 ) : ")
LOR = st.text_input("Enter Recommendation Letter Strength( out of 5 ) : ")
GPA =  st.text_input("Enter UG CGPA( out of 10 ) : ")
RE = st.text_input("Research Experience ( either 0 or 1 ) : ")

submit = st.button("Classify")

if submit:
	result = classifier.predict([[GRE,TOEFL,UR,SOP,LOR,GPA,RE]])	
	st.write(result)
