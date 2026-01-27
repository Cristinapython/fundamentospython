print("suma numeros letras")
print("introduce una cifra:")
textonumeros = input()
if (textonumeros.isdigit() == False):
    print("esto no son numeros: ", textonumeros)
else:
    #1+2+3+4
    suma = 0
    #recorremos cada caracter del texto
    for i in range(len(textonumeros)):
        #necesito cada letra del texto
        letra = textonumeros [i] 
        #convertimos la letra a numero
        numero = int(letra)
        suma = suma + numero
print("la suma de " + textonumeros + " es " + str(suma))    
print("fin de programa")   
