import json

file = open("student.json", "r")

data = json.load(file)

print("------Student Details--------")
for key, value in data.items():
    print(key, ":", value)

print("-----------------------------")

file.close()