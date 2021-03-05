# Modulos são uma boa prática para particionar os códigos, ou melhor,
# MODULARIZAR
import math


PI = math.pi


def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    m = 1
    for i in lista:
        m *= i
    return m

# Todo modulo executado diretamente se chama __main__
# É útil para testes
# Quer dizer que: quando esse arquivo for executado diretamente, ele
# testará o bloco de código 'if __name__ == '__main__'

if __name__ == '__main__':
    lista = [1, 2, 3, 4]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)