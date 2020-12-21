string = '01234567890123456789012345678901234567890123456789'

"""
for i in string:

    if i != '9':
        nova_string = i
        print(nova_string)
    else:
        pass
nova_string = list(nova_string)
print(nova_string)

for j in string:
    nova_string.append(string[k:i])
    i = 2*10
    k += 10
lc = [(i=2*10), (k+=10), (nova_string.append(string[0:i])) for j in string]
"""

n = 10
comp = [string[i:i + n] for i in range(0, len(string), n)]

# torna a lista como uma string
retorno = '.'.join(comp)

print(comp)
print(retorno)