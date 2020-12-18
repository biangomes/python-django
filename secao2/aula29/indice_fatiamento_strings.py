"""
Manipulando strings

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

"""

# positivos [012345678]
texto = "Python s2"

print('Elemento da posicao 2: ', texto[2])
print('Último elemento da string: ', texto[8])
print('Elemento da posição 6: ', texto[6])
#print('Elemento da posição 9: ', texto[9])

# negativos -[987654321]
#url = "www.google.com.br/"
#print("Url: ", url)
#print("Removendo o último elemento da URL: ", url[:-1])

nova_string = texto[2:6]
print("Fatiando string: ", nova_string)