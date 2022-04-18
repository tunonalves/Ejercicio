from Atleta import *
from paquete import sumar

atletas = None
listado_atletas = []

while True:
    print("\n\n MENU \n")
    print("1 - AGREGA")
    print("2 - MODIFICA")
    print("3 - MUESTRA")
    print("4 - MUESTRA OBJ")
    print("5 - LISTADO")
    print("0 - SALIR")
    option = input("\n Option: ")
    if (option == "1"):
        print("\n")
        dni = int(input("DNI: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))
        telefono = int(input("Telefono: "))
        atletas = Atleta(dni,nombre,apellido,altura,peso,telefono)
        atletas.setRegistroAtleta()
    if (option == "2"):
        while True:
            print("\n\n MENU \n")
            print("1 - DNI")
            print("2 - NOMBRE")
            print("3 - APELLIDO")
            print("4 - ALTURA")
            print("5 - PESO")
            print("6 - TELEFONO")
            print("0 - SALIR")
            option2 = input("\n Option: ")
            if (option2 == "1"):
                dni = int(input("DNI: "))
                atletas.setDNI(dni)
            if (option2 == "2"):
                nombre = input("Nombre: ")
                atletas.setNombre(nombre)
            if (option2 == "3"):
                apellido = input("Apellido: ")
                atletas.setApellido(apellido)
            if (option2 == "4"):
                altura = float(input("Altura: "))
                atletas.setAltura(altura)
            if (option2 == "5"):
                peso = float(input("Peso: "))
                atletas.setPeso(peso)
            if (option2 == "6"):
                telefono = int(input("Telefono: "))
                atletas.setTelefono(telefono)
            if (option2 == "0"):
                break
    if (option == "3"):
        print("\n\n DATOS ATLETA: \n")
        print("DNI: "+ str(atletas.getDNI()))
        print("Nombre: "+ atletas.getNombre())
        print("Apellido: "+ atletas.getApellido())
        print("Altura: "+str(atletas.getAltura()))
        print("Peso: "+str(atletas.getPeso()))
        print("Telefono: "+str(atletas.getTelefono()))
        print("IMC: "+atletas.getIMC())
    if (option == "4"):
        print(atletas.getDatos())
    if (option == "5"):
        print(atletas.getListaAtleta())
    if (option == "0"):
        break