import formata.preco

def aumento(valor, porcentagem, formata=False):
    valor = valor + (porcentagem/100) * valor

    if formata:
        return f"O produto agora vale: R${preco.real}."
    else:
        return valor

def promocao(valor, porcentagem, formata=False):
    valor = valor - (porcentagem/100) * valor

    if formata:
        return f"O valor da promoção é: R${preco.real}."
    else:
        return valor