"""Test API calls and save to file"""
import os
import json
import requests
URL = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"
api_key = os.environ.get("X_RAPIDAPI_KEY")

# Declare an array with a list of items to iterate through
ingredients = ["milk", "cream", "salt", "carrot", "onion", "mayonnaise", "ham"]

# Set a for loop to iterate through the array
DATA_STRING = "["
for ingredient in ingredients:
    querystring = {"query": ingredient}
    headers = {
        'x-rapidapi-host': "nutrition-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': api_key
        }
    response = requests.request("GET",
                                URL,
                                headers=headers,
                                params=querystring)
    data = response.text
    for X in data:
        if X == "[":
            continue
        if X == "]":
            X = ", "
        DATA_STRING += X
DATA_STRING = DATA_STRING[:-2]
DATA_STRING += "]"
print("DATA_STRING = ", DATA_STRING)

DATA_STRING = json.loads(DATA_STRING)
json.dump(DATA_STRING, open("home/fixtures/api.json", 'w', encoding="utf8"))
