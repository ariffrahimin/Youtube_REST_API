import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 12345, "name": "How to bake a cake", "views": 543234543}, {"likes": 293450, "name": "Genshin News", "views": 2344352},
        {"likes": 198345890, "name": "Ariff", "views": 10000}]

for i in range(len(data)):
    response = requests.put(
        BASE + "video/", {"likes": 10, "name": "Ariff", "views": 10000})
response = requests.put(
    BASE + "video/1", {"likes": 10, "name": "Ariff", "views": 10000})
print(response.json())
input()
response = requests.get(BASE + "video/6")
print(response.json())
