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


    
