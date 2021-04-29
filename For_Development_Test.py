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

json_data = json.dumps(user, indent=4)
print(json_data)


#------------------------------------------------------------
import json

user = {
    "id": "minchul",
    "password": "1234",
    "age": 25,
    "hobby": ["coding", "game"]
}

with open("user.json", "w", encoding="utf-8") as file:
    json_date = json.dump(user, file, indent=4)


#-----------------------------------------------------------------
import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

data = response.json()

name_list = []
for user in data:
    name_list.append(user['name'])

print(name_list)