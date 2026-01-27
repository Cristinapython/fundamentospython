print("Rango de numeros pares")
inicial = int(input("Inicio del bucle: "))
numero_final = int(input("Final del bucle: "))
while (inicial <= numero_final):
    if (inicial % 2 == 0):
        print(inicial)
    #incrementamos el valor inicial
    inicial = inicial + 1
    print("------------")
inicial = 6
numero_final = 20
#que tipo de bucle podriamos utilizar
for i in range(inicial, numero_final + 1):
    #deberiamos preguntar si el numero es par
    if (i % 2 == 0):
    #par
       print(i)
print ("fin de programa")       