"""
* Enumerate - Enumerar elementos da lista #list
"""
lista = [
        #  0       1       2
        ['Edu', 'João', 'Luiz'],        # 0
        ['Maria', 'Aline', 'Joana'],    # 1
        ['Beatriz', 'Flávia', 'Ana'],   # 2
]

#  lista[ posicao_no_elemento_pai ][ posicao_no_elemento_filho ]
# print(lista[1][2])
#
# enumerada = list(enumerate(lista))
# print(enumerada[1][1][2])

"""
[ <-- Enumerate
     0          1
    (0, ['Edu', 'João', 'Luiz']),       # 0
            0       1       2
    (1, ['Maria', 'Aline', 'Joana']),   # 1
            0         1        2
    (2, ['Beatriz', 'Flávia', 'Ana'])   # 2
            0           1        2
]
"""

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)