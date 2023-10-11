import random

n = random.sample(range(1, 5), 1)[0]
llista = []

def coincidencia():
  comptador = 0
  for x in range (n):
    if llista[x] == x+1:
      comptador +=1
  print('\n', llista, end = '\n\n')
  print('Hi ha '+str(comptador)+' nombres que coincideixen amb la seva posició.')

print("Se't demanaran "+str(n)+' nombres.')
for i in range(n):
  llista.append(int(input('\nIntrodueix un nombre enter: ')))

coincidencia()
