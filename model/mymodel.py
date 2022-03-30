def linear_regression_model(df_reg:pd.DataFrame) -> pd.DataFrame:
    # ## Linear Regression Model
    # Declare the features and targets
    X = df_reg.drop(['log_price'], axis =1)
    y = df_reg['log_price']
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
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

    # model evaluation for testing set
    y_test_predict = regressor.predict(X_test)
    rmse = (np.sqrt(MSE(y_test, y_test_predict)))
    r2 = r2_score(y_test, y_test_predict)
    regressor.coef_
    reg_summary = pd.DataFrame(X.columns.values, columns=['Features'])
    reg_summary['Weights'] = regressor.coef_
    reg_summary
    y_hat_test = regressor.predict(X_test)

    return y_hat_test



def polynomial_regression_model(degree,df_reg:pd.DataFrame):
    "Creates a polynomial regression model for the given degree"
    
    poly_features = PolynomialFeatures(degree=degree)

    # Declare the features and targets
    X = df_reg.drop(['log_price'], axis =1)
    y = df_reg['log_price']
    # ### Splitting the data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=365)
  
    # transforms the existing features to higher degree features.
    X_train_poly = poly_features.fit_transform(X_train)
    
    # fit the transformed features to Linear Regression
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train)
    
    # predicting on training data-set
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


