import libreria24validaciones
print("Main de validaciones")
print("Introduzca ISBN")
isbn = input()
repuesta = libreria24validaciones.validarISBN(isbn)
if (respuesta == True):
    print("El ISBN esta bien")
else: 
    print("El ISBN no es correcto")  
print("Fin del programa Main")    

Print("INTRUDUZCA DNI")
letra = libreria24validaciones.getLetraDni(numDni)
print("letra")
dni = "12345678Z"
#separamos el numero de la letra que nos han dado
numeros = dni[0: len(dni) - 1]
letraEscrita = dni[len(dni) -1 :]
print (numeros)
