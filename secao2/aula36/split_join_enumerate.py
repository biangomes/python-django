"""
Split, join, enumerate em python
* Split - dividir uma string # str
* Join - juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list iteraveis
"""
# SPLIT

# string = "O brasil é o país do futebol, o brasil brasil brasil é penta."
# lista1 = string.split(" ")
# lista2 = string.split(",")
# print("Lista 1: ", lista)
# print("Lista 2: ", lista2)

# palavra = ''
# contagem = 0

# for valor in lista1:
#     qtd_vezes = lista1.count(valor)
#     print(f'A palavra "{valor}" apareceu {lista1.count(valor)}x na frase.')
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f"A palavra que apareceu mais vezes é: {palavra} ({contagem}x)")

#------------------------

# JOIN

string = "O Brasil é penta."
lista = string.split(" ")
string2 = " ".join(lista)

#print(string2)

# ENUMERATE: enumera elementos de uma lista
for indice, valor in enumerate(lista):
    print(indice, valor)

