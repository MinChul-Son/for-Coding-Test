import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)



#----------------------------------------------------------
import json

user = {
    "id": "minchul",
    "password": "1234",
    "age": 25,
    "hobby": ["coding", "game"]
}

json_date = json.dumps(user, indent=4)
print(json_date)