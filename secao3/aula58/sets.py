# add (adiciona), update (atualiza), clear, discard
# union | une
# interseccao &
# diferença -
# diferença simétrica ^

s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
print(f"União entre os sets s1 e s2: {s1 | s2}")
print(f"Diferença entre os sets s1 e s2: {s2 - s1}")
print(f"Intersecção entre os sets s1 e s2: {s1 & s2}")
print(f"Diferença simétrica entre os sets s1 e s2: {s1 ^ s2}")
