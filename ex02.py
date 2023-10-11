def compara_nombres (n1, n2):
    if n1 > n2:
        print('\nEl primer nombre: '+str(n1)+', és més gran que el segon: '+str(n2)+'.')
    elif n2 > n1:
        print('\nEl segon nombre: '+str(n2)+', és més gran que el primer: '+str(n1)+'.')
    elif n1 == n2:
        print('\nEls dos nombres: '+str(n1)+', són iguals'+'.')

n1 = 0
n2 = 0

n1 = input ("Introdueix el primer nombre: ")
n2 = input ("Introdueix el segon nombre: ")

compara_nombres (n1, n2)
