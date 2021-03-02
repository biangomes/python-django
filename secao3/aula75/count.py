"""
count - itertools (iterador)
"""
from itertools import count

contador = count(start=10, step=-1)      # iterador

for valor in contador:
    print(round(valor, 2))

    if valor <= 1:
        break