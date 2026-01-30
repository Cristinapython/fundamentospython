print("Diccionarios")
#creamos el diccionario
provincias = dict()
#añadimos elementos
provincias ={
    924 : "Badajoz"
    956 : "Cadiz"
    958 : "Granada"
    959 : "Huelva"
    91 : "Madrid"
}
#recuperar el value de un elemento por su KEY
#si no existe devuelve None
print(provincias.get(959))
#recorrer cada Key, value mediante items
for clave, valor in provincias.items():
    print("Key" + str(clave) + ", Value: " + valor)
    #tambien podemos recorrer o solo claves(keys)
    #o solo calores (values)
for clave in provincias.keys():
    print(clave)   
for valor in provincias.values():
    print(valor)    
    #podemos añadir nuevos elementos key: value
provincias.setdefault(925, "Toledo") 
#no podemos repetir una key
provincias.setdefault(925, "Toledo")   
#podemos repetir el value
provincias.setdefault(933, "Toledo") 
#eliminamos un elemento por du key
#la clave debe existir o tendremos error
provincias.pop(924)
#eliminar todo el diccionasio
provincias.clear()
print(provincias)
