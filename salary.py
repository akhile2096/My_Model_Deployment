from tkinter import Y
import pandas as pd 
import numpy as np
import matplotlib as plt 
from sklearn.linear_model import LinearRegression

def salary_prediction(years):
    data = pd.read_csv('data.csv')
    X = data['YearsExperience'].values
    y = data['Salary'].values
   
    X = X.reshape(-1,1)
    y = y.reshape(-1,1)

    model = LinearRegression()
    model.fit(X,y)

    x_test = np.array(years)
    x_test = x_test.reshape((1,-1))
    pred = model.predict(x_test)
    
    return pred
