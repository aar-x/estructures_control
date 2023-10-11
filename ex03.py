def nom_repetit(nombre, nom):
    if nombre > 0:
        print((nom+' ')*nombre)
    elif nombre == 0:
        print("Error: el nombre no pot ser 0!")

nom = input("Quin és el teu nom de pila: ")
nombre = int(input("Introdueix un nombre positiu: "))

nom_repetit(nombre, nom)
