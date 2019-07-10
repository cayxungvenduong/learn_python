import json

with open('data.json') as f:
    data = json.load(f)

var1 = next(filter(lambda x: x["token"] == "token2", data), None)

print(var1)
