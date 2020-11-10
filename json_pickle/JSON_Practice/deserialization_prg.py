import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)
print(type(users))
# print(users)  #gives list of data

# for user in users:
#     print(user['email'], user['username'])



# Build a list of dictionaries with only "name" and "email" and serialise the data
data = [{"name": user['name'], "email": user['email']} for user in users]
with open('data1.json', 'w') as f:
    json.dump(data, f, indent=2)