import json

listClient = []
with open('data.json') as f:
    data = json.load(f)

tk1 = next(filter(lambda x: x["token"] == "token2", data), None)

print(tk1)
