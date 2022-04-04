import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from joblib import load

#from model.mymodel import features_targets_client



def predict_linear_regression(X):
    X_final = X.drop(labels=["log_price"])
    # model evaluation for testing set
    input = np.array(X_final.values).reshape(1,-1)
    #taking the model in the joblib file
    model = load("./model/model.joblib")
    y_hat_test = model.predict(input)
    #taking the value from the numpy array
    new_price = np.array(y_hat_test).item()
    #converting the log price in a normal price value
    new_price = round(np.exp(new_price), 2)

    return new_price



