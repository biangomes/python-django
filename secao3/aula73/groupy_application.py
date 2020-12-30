from itertools import groupby


alunos_matriculados = [
    {"nome": "Ana Kesia do Nascimento", "status": 0.94},
    {"nome": "Claudiane Magalhães", "status": 0.23},
    {"nome": "Daniel Garzon", "status": 0.60},
    {"nome": "Daíne Nogueira", "status": 0.94},
    {"nome": "Eder Silva dos Santos Júnior", "status": 0.23},
    {"nome": "Eduardo Goes", "status": 0.91},
    {"nome": "Fabricia Braga", "status": 0.23},
    {"nome": "Helmut Muniz", "status": 0.23},
    {"nome": "Hermann Duarte", "status": 0.23},
    {"nome": "Ian Ferreira", "status": 0.45},
]
ordena = lambda item: item["status"]
alunos_matriculados.sort(key=ordena)
alunos_agrupados = groupby(alunos_matriculados, ordena)

for agrupamentos, agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamentos}')   
    {print('aprovado') if agrupamentos >= 0.59 else print('reprovado')}
    {print(f'Status: {aluno}') for aluno in agrupados}