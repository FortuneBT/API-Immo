import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


def linear_regression_model(df_reg:pd.DataFrame):
    # ## Linear Regression Model
    # Declare the features and targets
    X = df_reg.drop(['log_price'], axis =1).to_numpy()
    y = df_reg['log_price'].to_numpy().reshape(-1,1)
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
    # Create a scaler object
    scaler = StandardScaler()
    # Fit the inputs (calculate the mean and standard deviation feature-wise)
    scaler.fit(X_test)
    scaler.fit(X_train)
    scaler.transform(X_train)
    regressor = LinearRegression().fit(X_train, y_train)

    joblib.dump(regressor, "./model/model.joblib")
    #model_columns = list(X.columns)
    #joblib.dump(model_columns, "./model/model.joblib")

    

def features_targets_client(df_reg:pd.DataFrame,X_value):
    # Declare the features and targets
    X = df_reg.drop(['log_price'], axis =1)
    X_value.drop(labels=["log_price"],inplace=True)
    X = X_value
    #X = df_reg
    y = df_reg['log_price']
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
    return [X_train, X_test, y_train, y_test,X, y]


def linear_regression_model_client(df_reg:pd.DataFrame,X_value) -> pd.DataFrame:
    # ## Linear Regression Model
    #X_train, X_test, y_train, y_test, X, y = features_targets_client(df_reg)
    X = df_reg.drop(['log_price'], axis =1)
    #X_value.drop(labels=["log_price"],inplace=True)
    #X = X_value
    #X = df_reg
    y = df_reg['log_price']
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
    X = X_value.to_numpy()
    #regressor = LinearRegression()
    
    return X_train, X_test, y_train, y_test 