with open(r'c:\caminho\do\arquivo.xml', 'r+') as file:
    tamanho = 0
    for linha in file:
        for letra in linha:
            tamanho += 1

print(tamanho)