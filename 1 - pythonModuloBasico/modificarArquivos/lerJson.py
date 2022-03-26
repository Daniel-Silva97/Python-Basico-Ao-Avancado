import json

with open('testeJson.json', 'r') as file:
    dicionarioJSON = file.read()
    # Convertendo o JSON para dicionário
    dicionarioJSON = json.loads(dicionarioJSON)

for chave, valor in dicionarioJSON.items():
    print(chave)
    for pessoa, idade in valor.items():
        print(pessoa, idade)