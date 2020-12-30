# conferindo se um objeto é iteravel
#list1 = [1, 2, 3, 4]
#print(hasattr(list1, '__iter__'))

#lista = list(range(100))

#print(sys.getsizeof(lista)) # quantos bytes essa lista consome de memoria

import sys
import time

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)     # interpretador 'dorme' por 0.1 ms

g = gera()

print(hasattr(g, '__next__'))   # gerador
print(hasattr(g, '__iter__'))   # geradores também sao interáveis

def gera2():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel

g2 = gera2()

print(next(g2))     # gera apenas o primeiro valor de g2
#print(next(g2))    # gera o segundo valor de g2
                    # e assim por diante...


# criar um gerador sem funcao
l1 = [x for x in range(1000)]
print(type(l1))
l2 = (x for x in range(1000))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))