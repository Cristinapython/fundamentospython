#este metodo convierte a mayusculas
#y nos devuelce el texto a mayusculas
def convertirMayusculas(texto):
    return texto.upper()
#otro metodo que convierte a minusculas
def convertirMinusculas(texto):
    return texto.lower()
def concatenar(texto1, texto2):
    resultado = texto1 + texto2
    return resultado
def mostrarMenu():
    print("seleccione una opcion")
    print("1.-Convertir a mayusculas")
    print("2.-Convertir a minusculas")
    print("3.-Concatenar textos")
#programa principal MAIN
print("Ejemplos metodos return")
print("Introduce un texto")
valor = input()
mostrarMenu()
opcion = int(input())
resultado = ""
if (opcion ==1):
    resultado = convertirMayusculas(valor)
elif (opcion == 2):
    resultado = convertirMinusculas(valor)   
elif (opcion == 3):
    print("Dame otro texto") 
    otro = input()
    resultado = concatenar(valor, otro) 
print(resultado)      
print("Fin de programa")    

