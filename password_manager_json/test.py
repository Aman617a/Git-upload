# website=input("website")
import json

with open("data.json", "r") as data:
    data_file=json.load(data)
    print(data_file["sdasd"])