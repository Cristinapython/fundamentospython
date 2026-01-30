print("Calcular letra NIF")
print("Introduzca numero DNI")
dni = int(input())
#( nº DNI - (ENTERO(nº DNI / 23) * 23
resultado = dni - (int((dni / 23)) * 23)
print(resultado)
if (resultado == 0):
    print("T")
elif (resultado == 1):
    print("R")
elif (resultado == 2):
    print("W")
elif (resultado == 3):
    print("A")
elif (resultado == 4):
    print("G")
elif (resultado == 5):
    print("M")
elif (resultado == 6):
    print("Y")
elif (resultado == 7):
    print("F")
elif (resultado == 8):
    print("P")
elif (resultado == 9):
    print("D")
elif (resultado == 10):
    print("X")
elif (resultado == 11):
    print("B")
elif (resultado == 12):
    print("N")
elif (resultado == 13):
    print("J")
elif (resultado == 14):
    print("Z")
elif (resultado == 15):
    print("S")
elif (resultado == 16):
    print("Q")
elif (resultado == 17):
    print("V")
elif (resultado == 18):
    print("H")
elif (resultado == 19):
    print("L")
elif (resultado == 20):
    print("C")
elif (resultado == 21):
    print("K")
elif (resultado == 22):
    print("E")
elif (resultado == 23):
    print("T")
print("Fin de programa")