try:
    a = {}
except (NameError, KeyError) as erro:
    print('Erro')
except Exception as erro:
    print('Ocorreu um erro inesperado')
finally:
    print('Código executado com sucesso!')
    print(a)