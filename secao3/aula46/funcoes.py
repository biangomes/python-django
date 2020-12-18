"""
Funções - def em Python (parte 1)
"""
def saudacao(msg="Olá", nome="Beatriz"):
    nome = nome.replace("e", "3").replace("a", "@").replace("i", "!")
    msg = msg.replace("e", "3")
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)