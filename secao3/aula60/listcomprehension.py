# criando uma lista
l1 = [1, 2, 3, 4, 5]
# utilizando list comprehension
l2 = [print(f'Imprime i={i}', sep=',') for i in l1]

# exemplo 2 utilizando list comprehension
ex2 = [v * 2 for v in l1]
print('Multiplica 2: ', ex2)

# exemplo 3
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

# exemplo 4
l3 = ['Beatriz', 'Ana Flávia', 'Ayala']
ex4 = [v.replace('a', '@').replace('A', '@').replace('á', '@') for v in l3]
print(ex4)

# criando uma tupla
tupla = (
    ('chave', 'valor1'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
print(f'Alterando a tupla: {ex5}')
# convertendo tupla pra dicionario
ex5 = dict(ex5)
print(ex5)

# filtrando uma lista
l4 = list(range(100))
# numeros divisiveis por 2
ex6 = [i for i in l4 if (i%2==0) if (i%8==0)]

# exemplo 7
ex7 = [print('É par') if v%2 == 0 else print('É ímpar') for v in l4]

