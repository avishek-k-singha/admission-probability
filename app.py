import streamlit as st
import pandas as pd 
import numpy as np 

st.write("""
# Find out your Admission probability for top 5 University of the world
""")
gre = st.number_input("Enter Your Gre Score")
toefl=st.number_input("Enter Your Toefl Score")
cgpa=st.number_input("Enter Your CGPA out of 10")
sop= st.slider('Score your SOP', min_value=1.0,max_value=5.0,step=.5)
lor= st.slider('Score your LOR', min_value=1.0,max_value=5.0,step=.5)
research=st.selectbox('Do you have any research paper',('Yes','No'))
ans=0
if research =='Yes':
	ans=1
else:
	ans=0

university=st.selectbox(
    'Unversity',
    ('University of Oxford','California Institute of Technology', 
    	'University of Cambridge','Stanford University',
    	'Massachusetts Institute of Technology')
)
uni=0
if university=='University of Oxford':
	uni==1
elif university=='Stanford University':
	uni=2
elif university=='University of Cambridge':
	uni=3
elif university=='Stanford University':
	uni=4
else:
	uni=5


df=pd.read_csv('datasets_14872_228180_Admission_Predict.csv')
df.drop(['Serial No.'],axis=1,inplace=True)
from sklearn.model_selection import train_test_split
X = df.drop(['Chance of Admit '],axis=1)
y = df['Chance of Admit ']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)
predictions = lm.predict(X_test)
test=[[gre,toefl,uni,sop,lor,cgpa,ans]]
data=lm.predict(test)*100

if data[0]>=90:
	st.write('You have a Great Chance of admission')
elif data[0]>=70 and data[0]<90 :
	st.write('You have a moderate chance of admission')
else:
	st.write("Sorry, You don't have any of chance admission")
