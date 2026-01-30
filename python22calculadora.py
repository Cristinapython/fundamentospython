#Creamos un metodo que devolvera el numero introducido
#En este metodo, tendremos un bucle infinito hasta que nos de 
#un numero
def getNumero():
    print("Introduzca numero")
    #AKMACENAMOS LO QUE ESCRIBA EL USUARIO
    #EN UNA VARIABLE STRING
    aux = input()
    #Entramos en un bucle mientras que NO sean NUMEROS
    while (aux.isdigit() == False):
        print("Eso no es un numero")
        print(("Introduzca numero"))
        aux = input()
    #Convertimos el texto en numero
    num = int(aux)  
    #Devolvemos el numero desde ek metodo
    return num
getNumero()
  

