import requests
from main import Pokemon_locations



BASE  = "http://127.0.0.1:5000/"

data = {"name": "Center", "region": 'Someplace', "game_index": 50}


response  = requests.post(BASE + "location/797", data)

print(response)

