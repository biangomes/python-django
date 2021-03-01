"""
Considerando duas lsitas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
--------------------------------
lista_soma = [2, 4, 6, 8]
"""
lista_A = [1, 3, 5, 7]

lista_B = [2, 4, 6]

resultado = [x + y for x, y in zip(lista_A, lista_B)]