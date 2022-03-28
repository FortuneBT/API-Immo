from flask import request
import requests


url = "http://127.0.0.1:5000/"

params = {"superficie":3000,
            "livingroom":200,
            "kitchen":True
}

r = requests.get(url=url,params=params)

data=r.json()

print(data)