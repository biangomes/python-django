from dados import produto, pessoas, lista
from functools import reduce


soma_precos = reduce(lambda ac, p: p['preco'] + ac, produto, 0)
print(round(soma_precos, 2))
print(f"A média dos preços é {round(soma_precos/len(produto), 2)}")
# ac: acumulador
# p: produto
# 0: início da contagem

soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(f"A soma das idades é {soma_idade}")
print(f"A média de idade dos clientes é {round(soma_idade/len(pessoas), 2)}")