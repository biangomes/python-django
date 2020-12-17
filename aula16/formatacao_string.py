"""
Iniciar com letra, pode conter número, separar com _
"""

nome = "Beatriz Nascimento"
idade = 22
altura = 1.63
e_maior = idade > 18
peso = 80.0
imc = peso / (altura ** 2)

# forma 1
print(f"{nome} tem {idade} anos de idade e seu imc é {imc:.2f}")

# forma 2
print("{} tem {} anos de idade e seu imc é {:.2f}".format(nome, idade, imc))

# forma 3
print("{0} tem {1} anos de idade e seu imc é {2:.2f}".format(nome, idade, imc))

# forma 4
print("{n} tem {i} anos de idade e seu imc é {im:.2f}".format(n=nome, i=idade, im=imc))

# brincando com a forma 4
print("{i} tem {im:.2f} anos de idade e seu imc é {i}".format(n=nome, i=idade, im=imc))