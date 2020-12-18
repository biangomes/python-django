"""
Funcoes - parte 4
"""

variavel = "valor"              # escopo global

def func():
    print(variavel)

def func2(arg=None):
    arg = arg.replace("o", "0").replace("v", "c")
    return arg

def func3():
    print(variavel)

func3()