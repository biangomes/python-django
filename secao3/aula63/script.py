alunos = {'Ana': [2.0, 4.0, 8.0, 10.0],
          'Beatriz': [8.0, 9.5, 10.0, 10.0],
          'Leonardo': [2.0, 1.0, 1.5, 10.0]
          }

media = {f'Média de {keys}: {(sum(values)/len(values)):.1f}' for (keys, values) in alunos.items()}
print(str(media))