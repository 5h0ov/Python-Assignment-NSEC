Dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
keys = ["name", "salary"]

newDict = {key: Dict[key] for key in keys}

print(newDict)
