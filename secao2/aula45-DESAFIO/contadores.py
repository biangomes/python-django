"""
for / while
0       10
1       9
2       8
3       7
4       6
5       5
6       4
7       3
8       2
"""
# minha resolucao
j=10

for i in range(10, 1, -1):
    while j >= 2:
        print(i, j)
        j -= 1
        i += 1

# resolucao do professor
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)