# Split, Join, Enumerate
# * split - dividir uma string #str
# * join - juntar uma lista #str
# * enumerate - enumerar elementos da lista #list

# ----------------------------------------------------------------------------------------------------------------------

# SPLIT
string = "O Brasil é o país do futebol, o Brasil é penta, o Brasil é o maior!"
lista1 = string.split(' ')      # separando a string por espaços
lista2 = string.split(',')      # separa a string por vírgula (,)


#for valor in lista2:

    #print(valor.strip().capitalize()),

    # strip: remove espaço do início e fim,

    # capitalize: deixa o primeiro caracter maiúsculo

lista3 = string.split(' ')      # deixa a string como uma lista de cada caracter