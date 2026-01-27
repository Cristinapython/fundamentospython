print("ejemplos clase de string")
texto = "primero python"
#vamos a ir probando diferentes metodos
print("upper ", texto.upper())
print("lower ", texto.lower())
print("replace", texto.replace("o", "@"))
print("letra o: ", texto[0])
print("longitud: ", len(texto))
print("find(p): ", texto.find("p"))
print("find(z): ", texto.find("z"))
#sobrecarga de un metodo
print("find(p, index): ", texto.find("p", 1))
print("rfind(p): ", texto.rfind("p"))
print("startswith(a) ", texto.startswith("a"))
print("endswith(n) ", texto.endswith("n"))
print("isdigit() ", texto.isdigit())
print("isalpha() ", texto.isalpha())
print("isalnum() ", texto.isalnum())
#probamos slicing, llamado substring
#recuperar una parte del texto
subcadena = texto[2: ]
print("texto[2:]:", subcadena)
#en python tambien podemos recuperar desde una posicion
#hasta otra posicion
subcadena = texto[2: 5]
print("texto[2:5]", subcadena)
#podemos recorrer cada caracter con un bucle
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print("letra[" + str(i) + "] = " + letra)
#podemos validar lo que nos ofrece un usuario
print("introduce un numero")    
dato = (input())
if (dato.isdigit() == True):
   print("Me has dado un numero!!!")
else:
    print("Que me des un numero!!!")   