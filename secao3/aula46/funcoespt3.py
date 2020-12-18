"""
Funções - def em Python (parte 3) - *args, **kwargs
"""
def func(a, b, c, d, e, nome=None):
    print(a, b, c, d, e)
func(1,2,3,4,5)


# quando nao sabe quantos parametros a funcao recebe
def func_args(*args):
    print("Parâmetros: ", args)
    print("Primeiro elemento: ", args[0])
    print("Último elemento: ", args[-1])
    print("Quantidade de parâmetros: ", len(args))

# ----------------------------------------------------------------------------------------------------------------------

print("-" * 100)
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista          # desempacotando os dois primeiros valores, empacotando o restante da lista na variavel n
print(n1, n2, n)

lista_2 = [1, 2, 4, 6]
print(*lista_2)             # desempacotando TODOS os valores da lista_2

print(*lista_2, sep=", ")   # desempacotando TODOS os valores da lista_2 com um separador ", "

# ----------------------------------------------------------------------------------------------------------------------
print("-" * 100)
func_args(2, 4, 6, 8, 10, 12, 14)
print("-" * 100)
def func_args_2(*args):
    args = list(args)
    args[0] = 20
    i=0
    for v in args:
        i += 1
        print("Parâmetro", i, ":", v)

def func_args_3(*args):
    print(args)

lista_3 = [0, 2, 4, 6]
lista_4 = [1, 3, 5, 7]
func_args_3(*lista_3, *lista_4)

print("-" * 100)

def func_args_kwargs(*args, **kwargs):
    print(args)
    #print(kwargs["nome"], kwargs["sobrenome"])
    idade = kwargs["idade"]
    print(idade)

func_args_kwargs(*lista_3, *lista_4, nome="Bia", sobrenome="Gomes", idade=22)