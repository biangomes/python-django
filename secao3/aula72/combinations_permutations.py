"""
Combinations, Permutations e Product - Itertools
Combinação - ordem NÃO importa
Permutação - Ordem IMPORTA
Ambos NÃO REPETEM valores únicos
Produto - ordem IMPORTA e REPETE valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

"""
for grupo in combinations(pessoas, 2):
    
    # combinacao da lista pessoas 2 a 2
    # ordem nao importa => andre e luiz = luiz e andre
    print(grupo)
"""

"""
for grupo in permutations(pessoas, 2):
    
    # ordem importa
    print(grupo)
"""

"""
for grupo in product(pessoas, repeat=2):
    print(grupo)
"""

for grupo in combinations(pessoas, 3):
    print(grupo)