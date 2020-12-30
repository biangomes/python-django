# criando uma lista de tuplas
lista = [
    ('A', 1),
    ('B', 2)
]

# dict comprehension
d1 = {x: y*2 for x, y in lista}
# virou um dicionario
print('d1: ', type(d1), d1)

# criando outro dict comprehension
d2 = {x: y for y, x in enumerate(range(5))}
print('d2: ',type(d2), d2)

# list comprehension terminando em dicionario
d3 = {x for x in range(5)}
print('d3: ', type(d3), d3)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
keys_values = {keys: values for keys, values in zip(keys, values)}
print(f'keys: {keys}\nvalues: {values}\nkeys_values: {keys_values}')