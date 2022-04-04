import numpy as np
from joblib import load


def predict_linear_regression(X):
    X_final = X.drop(labels=["log_price"])
    # model evaluation for testing set
    input = np.array(X_final.values).reshape(1, -1)
    # taking the model in the joblib file
    model = load("./model/model.joblib")
    y_hat_test = model.predict(input)
    # taking the value from the numpy array
    new_price = np.array(y_hat_test).item()
    # converting the log price in a normal price value
    new_price = round(np.exp(new_price), 2)

    return new_price
