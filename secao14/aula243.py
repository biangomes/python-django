"""
aula 243 - assertions
"""
from calculadora import soma, sub, mult, div


try:
    print(soma('15', 15))
except AssertionError as e:
    print(f"Conta inválida: {e}")


try:
    print(div(10, 0))
except AssertionError as e:
    print(f"Conta inválida: {e}")

print("Conta", soma(25, 25))