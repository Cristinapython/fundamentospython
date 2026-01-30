print("introduzca ISBN")
isbn = input()
if (len(isbn) != 10):
    print("El ISBN debe tener 10 caracteres")
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
    print("ISBN correcto")