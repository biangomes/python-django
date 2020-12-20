# criando um dicionario com as perguntas
perguntas = {
    "Pergunta 1": {"pergunta": "Quanto é 2 + 2? ", "respostas": {"a": "1", "b": "4", "c": "2" }, "resposta_certa": "b"},
    "Pergunta 2": {"pergunta": "Quanto é 3 * 2? ", "respostas": {"a": "6", "b": "9", "c": "5" }, "resposta_certa": "a"}
}

respostas_certas = 0        # contador das respostas acertadas
respostas_erradas = 0       # contador das respostas erradas
taxa_de_acerto = 0          # percentual de acerto

# estrutura para acessar os dicionarios
for chave_pergunta, valor_pergunta in perguntas.items():
    print(f'{chave_pergunta}: {valor_pergunta["pergunta"]}')
    print("Escolha uma das opções: ")

    for chave_resposta, valor_resposta in valor_pergunta["respostas"].items():
        print(f'[{chave_resposta}]: {valor_resposta}')

    resposta_usuario = input("Sua resposta: ")

    # validando a resposta do usuario (resposta_usuario)
    if resposta_usuario == valor_pergunta["resposta_certa"]:
        respostas_certas += 1       # adicionando no contador das respostas acertadas
    else:
        respostas_erradas += 1      # adicionando no contador das respostas erradas

    # calculo taxa de aproveitamento do usuario
    taxa_de_acerto = (100 * respostas_certas)/len(perguntas.keys())
    print()
print(f'Respostas certas: {respostas_certas}\nRespostas erradas: {respostas_erradas}\nTaxa de acerto: {taxa_de_acerto:.0f}%')
