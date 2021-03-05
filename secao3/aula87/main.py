# https://docs.python.org/3/library/functions.html

"""
'w': apaga tudo que tá no arquivo e, então, escreve
'a': mantém tudo que há escrito no arquivo e inicia o cursor na última posição
"""


# Gerenciador de contexto:
# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#     file.seek(0,0)
#     print(file.read())
#
# with open('abc.txt', 'a+') as file:     # o 'a' adiciona coisas ao arquivo coloca o cursor no final do arquivo
#     file.write('Outra linha\n')
#     file.seek(0, 0)
#     print(file.read())



# REMOVER
# import os
# os.remove('abc.txt')

import json

d1 = {
    'Pessoa 1': {'nome': 'Luiz', 'idade': 25},
    'Pessoa 2': {'nome': 'Rose', 'idade': 30},
}

# convertendo dicionario para um json
d1_json = json.dumps(d1, indent=True)        # convertendo pra json

with open('abc.json', 'w+') as file:
    file.write(d1_json)