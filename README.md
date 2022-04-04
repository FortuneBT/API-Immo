# API - Price Prediction 

The goal of this project is to predict the price of a house with machin learning and create an API that will manage the answer, the input and output. This api will be depploy to heroku with Docker. This API is using restful library.


### Base URL
https://api-house-fortune.herokuapp.com/

#### Methods
1. GET - No parameters required.

##### Response
```
The server is alive.
```
### Price Prediction
https://api-house-fortune.herokuapp.com/predict

#### Methods
1. GET - No parameters required. Returns a dictionary containing all required parameters and their formats to predict a property's price.

##### Response
```
    {"0": {
        "area": int,
        "property-type": str,
        "rooms-number": int,
        "zip-code": int,
        "land-area": Optional[int],
        "garden": Optional[bool],
        "garden-area": Optional[int],
        "equipped-kitchen": Optional[bool],
        "full-address": Optional[str],
        "swimming-pool": Optional[bool],
        "furnished": Optional[bool],
        "open-fire": Optional[bool],
        "terrace": Optional[bool],
        "terrace-area": Optional[int],
        "facades-number": Optional[int],
        "building-state": Optional[str],
    }
}
```

2. POST - Accepts a JSON request that should contains the required parameters and returns a JSON response containing the predicted price.

##### Response
1. 200 - OK (Success)

```
{
    "error": null,
    "prediction": [float]
}
```

2. 400 - Bad Request (Error) : Depending on the cause of the error, the response will either return the price prediction URL or identify the missing parameters or formats.

##### Response Type - 1
```
{
    "errors": {
        "parameter": "message"
    },
    "prediction": null
}
```

##### Response Type - 2
```
{
    "errors":-> list of ["error message(s)"],
}
```
 "Refer input format available at: https://api-house-fortune.herokuapp.com/predict with a get request"

## Cloning Repository 

### Installation
The project has been coded in Python 3.8.10 and requires the following packages and libraries:

1. [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask)
2. [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
3. [flask Restfull](https://pypi.org/project/Flask-RESTful/)
4. [Scikit-learn](https://scikit-learn.org/stable/install.html)
5. [Jsonschema](https://pypi.org/project/jsonschema/)
6. [Docker](https://docs.docker.com/engine/install/ubuntu/) --> if you want to wrap the app in a container.
7. Heroku - `sudo snap install --classic heroku`

Note: It is recommended to use virtual environment while installing the above packages and libraries.

### Usage
1. To deploy the program on a local machine, navigate to the root directory of the project and run `python3 app.py` on the terminal.
2. This will launch the app on a browser window where you can check the response for GET requests to the base URL (/) and the Price prediction (/predict).
3. Use a service like Postman to send a POST request with the required parameters to receive the price prediction.
4. To update/modify the data preprocessing elements, navigate to `preprocessing>cleaning_data.py`.
5. To update/modify the regression model, navigate to `model>model.py`.
6. To update/modify the error handling, navigate to `validation.py`.
7. To wrap app in a container, run `docker build . -t image-name` in the `/app/code` directory.
8. To deploy the container, run `docker run -t image-name`.
9. To deploy container on Heroku, refer [official documentation](https://devcenter.heroku.com/articles/container-registry-and-runtime).

### Contributors
1. Fortuné Beze Tshali