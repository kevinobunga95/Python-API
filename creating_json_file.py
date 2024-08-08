from python_dict import Client_string
import json
# #opening a JSON file
with open("clients.json", 'w') as file:
    json.dump(Client_string, file, indent=4)


with open('clients.json', 'r') as file:
    print(file.read())

with open('clients.json', 'r',) as file:
   my_new = json.load(file)
print(my_new)

