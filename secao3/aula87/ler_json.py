import json

with open('abc.json', 'r') as filejson:
    # acessando o arquivo
    d1_json = filejson.read()

    # voltando a ser dicionario
    d1_json = json.loads(d1_json)

# lendo o dicionario
for key, value in d1_json.items():
    print(key)
    for key1, value1 in value.items():
        print(key1, value1)