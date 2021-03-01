logged_user = False

# operador ternario

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    eh_maior = (int(idade)>=18)
    msg = 'Pode acessar!' if eh_maior else 'Nao pode acessar'

print(msg)