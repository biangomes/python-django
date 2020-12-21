"""
-> É uma lista de listas de números inteiros
-> As listas internas têm o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiro número
   duplicado considerando o segundo número como a duplicação na lista interna.
    Requisitos:
      - A ordem do número duplicado é considerada a partir da segunda
        ocorrência (o número duplicado em si).
          Exemplo: [1, 2, 3, ->3<-, 2, 1].
          Se não encontrar duplicados na lista, retorne -1.
"""

lista = [
    [1, 2, 3, 3, 2, 4, 5, 6, 9, 10],
    [0, 1, 4, 5, 7, 12, 3, 14, 15, 17],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

# def pega_duplicados(lista):
#atual_j=0
#for i in lista:
#    print(f'i={i}')
#    for j in lista:
#        print(f'j={j}')
#        atual_j = j
        #if j == j[-1]:
            #print(j)
        #else:
            #print(-1)

#pega_duplicados(lista)

# ---------------------------------------------------------------------------------------------------------------------
def pega_duplicados(n1):

    # cria um conjunto vazio
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in n1:
        # verifica se o número do for já está no conjunto
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        # a cada numero checado, adiciona no conj. numeros_checados
        numeros_checados.add(numero)
    return primeiro_duplicado

for lista_inteiros in lista:
    print(pega_duplicados(lista_inteiros))

# testando novamente
print(pega_duplicados([1, 1, 3, 2, 10, 10, 20, 20, 40, 40]))