"""
def funcao(arg, arg2):
    return arg * arg2
var = funcao(2,2)
"""
# a = lambda x, y: x * y
# print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
]

lista.sort(key=lambda item:item[1])
print("Lista ordenada usando lambda: ", lista)

print("Testando outra forma: ", sorted(lista, key=lambda i: i[1]))

"""
Usando item[0] (ou i[0]) - > nome do produto
Usando item[1] (ou i[1]) - > chave do produto
"""