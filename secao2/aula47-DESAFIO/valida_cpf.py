cpf = input("Seu CPF (apenas números): ")
multiplicador = list(range(10, 1, -1))
armazenador = []

for i in cpf:
    armazenador = cpf[i] * multiplicador[i]
    print(armazenador)