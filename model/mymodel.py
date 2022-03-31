import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures



def features_targets(df_reg:pd.DataFrame):
    # Declare the features and targets
    X = df_reg.drop(['log_price'], axis =1)
    y = df_reg['log_price']
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
    return [X_train, X_test, y_train, y_test,X, y]

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


def linear_regression_model(df_reg:pd.DataFrame) -> pd.DataFrame:
    # ## Linear Regression Model
    X_train, X_test, y_train, y_test, X, y = features_targets(df_reg)
    # ### Standardization and Scaling
    # Create a scaler object
    scaler = StandardScaler()
    # Fit the inputs (calculate the mean and standard deviation feature-wise)
    scaler.fit(X_train)
    features_scal = scaler.transform(X_train)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    regressor.score(X_train, y_train)
    y_hat = regressor.predict(X_train)
    scaler.transform(X_test)
    regressor.score(X_test, y_test)
    y_hat = regressor.predict(X_train)
    rmse = (np.sqrt(MSE(y_train, y_hat)))
    r2 = r2_score(y_train, y_hat)
    return regressor



def polynomial_regression_model(degree,df_reg:pd.DataFrame):
    "Creates a polynomial regression model for the given degree"
    
    poly_features = PolynomialFeatures(degree=degree)
    
    X_train, X_test, y_train, y_test, X, y = features_targets(df_reg)
  
    # transforms the existing features to higher degree features.
    X_train_poly = poly_features.fit_transform(X_train)
    
    # fit the transformed features to Linear Regression
    poly_model = LinearRegression()
    return poly_model.fit(X_train_poly, y_train)
    



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