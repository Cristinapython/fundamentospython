print("ejemplos de bucles")
print("WHILE")
#NECESITAMOS UNA VARIABLE FUERA DE BUCLE
#PARA NUESTRA COINDICION
contador = 0
while (contador <= 5):
    print ("contador", contador)
    #necesitamos cambiar el valor de algo
    #para salir del bucle
    contador = contador + 1
#En el bucle FOR, se declara la variable contador
#en la definicion del bucle
# dicha variable suele llamarse i, z k
# hacemos un FOR de 0 a 5
print ("FOR")
for i in range(5+1):
    print("valor de i: ", i)  
    #tenemos la posibilidad de indicar numero de inicio y
    # numero final 2--8
for z in range(2, 8 + 1):
    print("z: ", z) 
print ("fin de programa")    
    