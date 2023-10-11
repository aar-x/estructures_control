import random

def simetria():
  i = 0
  while i < n/2 and llista[i] == llista[n-i-1]:
    i += 1

  print('\n', llista, end = '\n\n')

  if i == (n+1)/2 or i == n/2:
    print('La llista és simètrica: '+str(n)+' elements.')
  else:
    print('La llista no és simètrica.')

n = random.sample(range(1, 5), 1)[0]
llista = []

print("Se't demanaran "+str(n)+' nombres per crear una llista.')
for i in range(n):
  llista.append(int(input('\nIntrodueix un nombre enter: ')))

simetria()
