"""
Formatando valores com modificadores

:s - strings
:d - inteiros
:f - floats
:.(NÚMERO)f - quantidade de casas decimais
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

n1 = 10
n2 = 3
divisao = n1 / n2

print("Imprimindo a divisão:\n", divisao)
print("Outra forma de imprimir a divisão: \n{}".format(divisao))
print("Outra forma de imprimir a divisão, trucando:\n{:.2f}".format(divisao))
print(f"Outra forma de imprimir a divisão, também trucando:\n{divisao:.2f}")
print(f"Imprimindo a variável 'seca':\nn1")
print(f"Adicionando zeros à esquerda, ficando com 10 casas decimais:\n{n1:0>10}")


nome = "Beatriz Nascimento"
print("Imprimindo strings de formas diferentes:\n")
print("Forma 1:\n{}".format(nome))
print(f"{nome:#^50}")