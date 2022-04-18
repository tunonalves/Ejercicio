import sys

if len(sys.argv) == 3:
    nota1 = float(sys.argv[1])
    nota2 = float(sys.argv[2])
    if nota1 >= 7 and nota2 >= 7:
        print("Promocionado")
    elif nota1 >= 4 and nota2 >= 4:
        print("Aprobado")
    elif (nota1 < 4 or nota2 < 4) and (not (nota1 < 4 and nota2 < 4)):
        if nota1 < 4:
            print("Desaprobado, Recupera 1º ")
        else:
            print("Desaprobado, Recupera 2º")
    else:
        print("Desaprobo los 2 parciales")