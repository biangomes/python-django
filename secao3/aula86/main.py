# Criando pacotes

from vendas.calc_precos import aumento, promocao
from vendas.formata import preco

precos = 10.0
precos_com_aumento = aumento(precos, 10, formata=True)
produto_com_promocao = promocao(precos, 20, formata=True)
print(precos_com_aumento)
print(produto_com_promocao)