"""
Zip - unindo iteráveis
Zip_longest - itertools
"""
from itertools import zip_longest, count


# Código
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,     # eh um gerador
    estados,    # iteravel
    cidades,    # iteravel
)

# Iteráveis empacotados
for valor in cidades_estados:
    print(valor)

# Para desempacotar
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)


#print(list(cidades_estados))

# print(cidades_estados)
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))


# for valor in cidades_estados:
#     print(valor)