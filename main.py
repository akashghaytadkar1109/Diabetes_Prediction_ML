# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:15:55 2022

@author: Akash
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

class model_input(BaseModel):
        
    Pregnancies:int
    Glucose : int
    BloodPressure : int
    SkinThikness: int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction: float
    Age : int 
    
    
#loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))


@app.post('/Diabetes_Prediction_Project')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.load(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThikness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    
    input_list = [preg,glu,bp,skin,insulin,bmi,dpf,age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person is not Diabetic'
    
    else:
        return 'The person is Diabetic'
    