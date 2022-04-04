import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from joblib import load

from model.mymodel import features_targets_client


def features_targets(df_reg:pd.DataFrame):
    # Declare the features and targets
    X = df_reg.drop(['log_price'], axis =1)
    y = df_reg['log_price']
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
    return [X_train, X_test, y_train, y_test,X, y]


def features_targets_client(df_reg:pd.DataFrame):
    # Declare the features and targets
    y = df_reg['log_price']
    X = df_reg.drop(['log_price'], axis =1)
    #X = df_reg
    
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
    return [X_train, X_test, y_train, y_test,X, y]


def predict_linear_regression(X):
    # model evaluation for testing set
    input = np.array(X).reshape(1,-1)
    model = load("./model/model.joblib")
    y_hat_test = model.predict(input)

    return y_hat_test





def predict_linear_regression_client(features,X_value):
    # model evaluation for testing set
    #X_train, X_test, y_train, y_test,X, y = features_targets_client(df_reg)
    #X = df.to_numpy()
    X_train, X_test, y_train, y_test = features
    #X = X_value
    """X = X.drop(labels=["log_price"])
    y_test_predict = regressor.predict(X_test)
    rmse = (np.sqrt(MSE(y_test, y_test_predict)))
    r2 = r2_score(y_test, y_test_predict)
    regressor.coef_
    reg_summary = pd.DataFrame(X.values, columns=['Features'])
    reg_summary['Weights'] = regressor.coef_
    reg_summary"""
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_hat_test = regressor.predict(X_test)

    return y_hat_test[0]   