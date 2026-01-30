print("listas con Python")
listaNumeros = [3,5,7,11,2,9,88]
#PODEMOS DIBUJAR DIRECTAMENTE LAS LISTAS
#podemos ordenar de forma ascendente
#listanumeros.sort()
#orden descendente
#listaNumeros.sort(reverse=True)
#print(listaNumeros)
#podemos recorreer todos los elementos
#del conjunto 1 a 1 con un for (todo empieza de CERO)
for i in range(len(listaNumeros)):
    print(lista Numeros[i])
#listas pueden ser de cualquier tipo
listaNombres = ["Ana", "Maria", "Adrian", "Lucia", "Diana"] 
#accedemos a los nombres por su indice
print("Nombre[2]: " listaNombres[2]) 
print("Nombre[4]: " listaNombres[4]) 
listaNombres.apped("El nuevo")
#podemos insertar un nuevo elemento en una posicion
listaNombres.inser(1, "Infiltrado")
#el metodo remove() elimina ek primer elemento que se encuentre 
#listaNombres.remove("Adrian")
#Podemos eliminar por indice/posicion
listaNombres.pop(6)
#podemos borrar por rangos
del listaNombres[0:2]
#podemos preuntar por elementos dentro del conjunto
respuest = "Diana" in listaNombres
print("Diana existe", respuesta)
#podemos recorrer cada elemnto
for i in range(len(listaNombres)):
    print(listaNombres[i])
#Podemos borrar toda la lista
listaNombres.clear()
print(listaNombres)

print("tuplas")
#elementos estaticos 
tupla = ("Leche", "Cacao", "Avellenas", "Azucar")
print("tupla[1], ", tupla[1])
#la tupla no se puede modificar
tupla[1] = "Vainilla"
print(tupla)
#quiero reccorrer cada elemento de la tupla
for i in range(len(tupla)):
    elem = tupla[i]
    print(elem)
#otra forma:
#for elem in tupla:
    #print(elem)     


