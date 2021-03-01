"""
Desempacotamento de listas e Python
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4]

# *outra_lista pega todos os valores que "sobraram" da lista
n1, n2, n3, *outra_lista, ultimo_valor_da_lista = lista

print(ultimo_valor_da_lista)

lista2 = ['Ana', 'Bia', 'Carlos', 'Carla', 5, 6, 7, 8, 9, 10, 11]
n4, n5, *_ = lista2     # *_ : descarta os valores da lista que sobraram