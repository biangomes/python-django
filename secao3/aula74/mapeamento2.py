from map_dados import produtos, pessoas, lista

def aumenta_idade(p):
    p["nova_idade"] = round(p["idade"] * 1.20, 2)
    return p

nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)