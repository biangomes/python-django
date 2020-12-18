"""
Pass e Ellipsis como placeholders
"""

# Utilizando pass
valor = False
if valor:
    # serve para explicar oq faria aqui, por exemplo
    # "segura" o lugar
    pass
else:
    print("True")

# Utilizando ellipsis
valor = False
if valor:
    # "segura" o lugar
    # alternativa ao pass
    ...
else:
    print("True")