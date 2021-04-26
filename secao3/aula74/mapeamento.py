from map_dados import produtos, pessoas, lista

"""
funcao map: usa uma funcao como primeiro argumento
"""
nova_lista = map(lambda x: x*2, lista)
print('-'*10, '\nUsando map')
print(lista)
print(nova_lista)       # devolve um iterador
print(list(nova_lista)) # devolve uma lista

"""
a funcao map pode ser representada com uma list comprehension
"""
print('-'*10, '\nUsando list comprehension')
nova_lista_2 = [x * 2 for x in lista]
print(nova_lista_2)