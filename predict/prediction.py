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


def predict_linear_regression(regressor,df_reg):
    # model evaluation for testing set
    X_train, X_test, y_train, y_test,X, y = features_targets(df_reg)
    y_test_predict = regressor.predict(X_test)
    rmse = (np.sqrt(MSE(y_test, y_test_predict)))
    r2 = r2_score(y_test, y_test_predict)
    regressor.coef_
    reg_summary = pd.DataFrame(X.columns.values, columns=['Features'])
    reg_summary['Weights'] = regressor.coef_
    reg_summary
    y_hat_test = regressor.predict(X_test)

    return y_hat_test


def predict_polynomial_regression_model(poly_model,df_reg,X_train_poly,poly_features):
    # predicting on training data-set
    X_train, X_test, y_train, y_test, X, y = features_targets(df_reg)
    y_train_predicted = poly_model.predict(X_train_poly)
    
    # predicting on test data-set
    y_test_predict = poly_model.predict(poly_features.fit_transform(X_test))
    
    # evaluating the model on training dataset
    rmse_train = np.sqrt(MSE(y_train, y_train_predicted))
    r2_train = r2_score(y_train, y_train_predicted)
    
    # evaluating the model on test dataset
    rmse_test = np.sqrt(MSE(y_test, y_test_predict))
    r2_test = r2_score(y_test, y_test_predict)
    
    return y_test_predict