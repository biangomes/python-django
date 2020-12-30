# Dict Comprehensions e Itertools
**Data:** 30 de dezembro de 2020.

## Contexto

A fim de utilizar os connhecimentos adquiridos em um curso online e a necessidade de resolver uma problemática no projeto de extensão do qual participei, fiz um script simples que agrupa os alunos aprovados e reprovados. A teoria por detrás é baseada em dict comprehensions, método `.sort()`, `.groupby()`, `dict` e funções `lambda`. 

---

## Código

> `from itertools import groupby`

A partir do módulo `itertools`, importamos especificamente o `groupby`, com a finalidade de separar quem estava reprovado e quem estava aprovado.

> ```python
>alunos_matriculados = [
>    {"nome": "Ana", "status": 0.94},
>    {"nome": "Clarice", "status": 0.23},
>    {"nome": "Danilo", "status": 0.60},
>    {"nome": "Danara", "status": 0.94},
>    {"nome": "Edlailson", "status": 0.23},
>    {"nome": "Edu", "status": 0.91},
>    {"nome": "Fabricio", "status": 0.23},
>    {"nome": "Hiago", "status": 0.23},
>    {"nome": "Hugo", "status": 0.23},
>    {"nome": "Igor", "status": 0.45},
>]
> ```
Foi passando uma lista, cujo os elementos são dicionários com duas chaves-valor. As chaves são "nomes" e "status" e os valores são os nomes e a nota dos alunos em percentual. Para obter aprovação, o aluno precisaria ter um status igual ou superior a 60% (ou 0.6).

> ```python
> ordena = lambda item: item["status"]
> alunos_matriculados.sort(key=ordena)
> alunos_agrupados = groupby(alunos_matriculados, ordena)
>```

Na primeira linha, usamos uma função lambda para pegar especificamente a chave "status" dos dicionários, armazenando-as em uma variável denominada `ordena`.

Para utilizar o `.groupby()`, é necessário que os dados estajm ordenados previamente. Por isso, na segunda linha o método `.sort(key= ordena)` foi utilizado. Esta linha estava apenas querendo dizer: "Eu ordenei os meus dados partindo do status. Agora, `.sort()`, por favor, ordena tendo como chave a ordenação dada (`key=ordena`)."

Uma vez que os dados já estão ordenados, enfim é utilizado o `.groupby()`. Veja que este método recebe um iterável e uma função como parâmetros. Este agrupamento foi armazenado em uma variável chamada `alunos_agrupados`.

>```python
>for agrupamentos, agrupados in alunos_agrupados:
>    print(f'Agrupamento: {agrupamentos}')   
>    {print('aprovado') if agrupamentos >= 0.59 else prin ('reprovado')}
>{print(f'Status: {aluno}') for aluno in agrupados}

As `dict comprehensions` estão na linha 3 e 4 deste bloco de código, em que eu peço para imprimir "aprovado" se o `agrupamentos > 0.59`; reprovado, caso contrário. Por último, informo os alunos deste grupo.

A formatação da saída está abaixo:

>```python
> Status: {'nome': 'Clarice', 'status': 0.23}
> Status: {'nome': 'Edlailson', 'status': 0.23}
> Status: {'nome': 'Fabricio', 'status': 0.23}
> Status: {'nome': 'Hiago', 'status': 0.23}
> Status: {'nome': 'Hugo', 'status': 0.23}
> Agrupamento: 0.45
> reprovado
> Status: {'nome': 'Igor', 'status': 0.45}
> Agrupamento: 0.6
> aprovado
> Status: {'nome': 'Danilo', 'status': 0.6}
> Agrupamento: 0.91
> aprovado
> Status: {'nome': 'Edu', 'status': 0.91}
> Agrupamento: 0.94
> aprovado
> Status: {'nome': 'Ana', 'status': 0.94}
> Status: {'nome': 'Danara', 'status': 0.94}

O código pode ser melhorado, e muito, porém foi uma aplicação que consegui fazer e achei útil compartilhar.

