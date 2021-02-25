from itertools import groupby, tee


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Bia', 'nota': 'C'},
    {'nome': 'Luiz Felipe', 'nota': 'A'},
    {'nome': 'Luiz Pedro', 'nota': 'B'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'José', 'nota': 'A'},
    {'nome': 'Josué', 'nota': 'B'},
    {'nome': 'Flávia', 'nota': 'C'},
    {'nome': 'Luiza', 'nota': 'A'},
    {'nome': 'Luisa', 'nota': 'B'},
]

ordena = lambda item: item["status"]
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamentos, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamentos}')
    print(f'{len(valores_agrupados)}')