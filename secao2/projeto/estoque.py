"""
Programa de Controle de Estoque - PCE
Data: 09/03/2021
"""


def adiciona_produto(nome, preco, quantidade):
    produtos[nome] = [preco, quantidade]


produtos = {}

escolhe = int(input('1. Adicionar produto\n2. Visualizar os produtos em estoque\n'))

if escolhe == 1:
    qtd_produtos = int(input('Quantidade de produtos que quer adicionar: '))
    for item in range(qtd_produtos):
        nome_produto = input('Nome do produto: ')
        preco_produto = float(input(f'Preço do {nome_produto}: '))
        qtd_produto = int(input(f'Quantidade de {nome_produto}: '))
        adiciona_produto(nome_produto, preco_produto, qtd_produto)

    print("#" * 30)
elif escolhe == 2:
    for key, value in produtos.items():
        print(key, value)
