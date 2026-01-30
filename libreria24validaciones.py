def validarISBN(isbn):
    if (len(isbn) != 10):
        return False
    else:
        suma = 0
        for i in range(len(isbn)):
            #recuperamos cada caracter
            caracter = isbn[i]
            #convertimos a numero el caracter
            numero = int(caracter)
            multi = numero * (i+1)
            suma = suma + multi
        #preguntamos si al dividir entre 11 da resto 0
        if (suma  % 11 == 0):
            return True
        else: 
            return False


def getLetraDNI(numerodni):
#( nº DNI - (ENTERO(nº DNI / 23) * 23
    resultado = numeroDni - (int(numeroDni / 23) * 23)
    muestraletras = "TRWA"
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

def validarDni(dni):#12345678Z
    #separamos el numero de la letra
    numeros = dni[0: len(dni)]
