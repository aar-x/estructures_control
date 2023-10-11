def classifica_nota (valor):
    if valor < 5:
        print('Suspès')
    elif valor < 7:
        print('Aprovat')
    elif valor < 9:
        print('Notable')
    elif valor <= 10:
        print('Excel·lent')

valor = -1
while not(valor >= 0 and valor <= 10):
    valor = float(input ("Introdueix una nota entre 0 i 10:"))

classifica_nota (valor)
