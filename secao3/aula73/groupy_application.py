from itertools import groupby


alunos_matriculados = [
   {"nome": "Ana", "status": 0.94},
   {"nome": "Clarice", "status": 0.23},
   {"nome": "Danilo", "status": 0.60},
   {"nome": "Danara", "status": 0.94},
   {"nome": "Edlailson", "status": 0.23},
   {"nome": "Edu", "status": 0.91},
   {"nome": "Fabricio", "status": 0.23},
   {"nome": "Hiago", "status": 0.23},
   {"nome": "Hugo", "status": 0.23},
   {"nome": "Igor", "status": 0.45},
]

ordena = lambda item: item["status"]
alunos_matriculados.sort(key=ordena)
alunos_agrupados = groupby(alunos_matriculados, ordena)

for agrupamentos, agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamentos}')   
    {print('aprovado') if agrupamentos >= 0.59 else print('reprovado')}
    {print(f'Status: {aluno}') for aluno in agrupados}