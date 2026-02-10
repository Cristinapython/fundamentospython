import oracledb

print("Conectando Oracle")
#tenemos un objeto connection quenospedira 
#usser, password, server
connection = oracledb.connect(user="SYSTEM"
                              , password="oracle"
                              ,dsn="localhost/FREEPDB1")
print("Estamos conectados")
#Creamos nuestra consulta SQL con los departamentos 
#la consulta SQL desde Python no finaliza en 
sql = "select * from DEPT"
cursor = connection.cursor()
#Debemos ejecutar la consulta para que nos devuelva los datos de oracle
cursor.execute(sql)
#aqui ya estna los datos
#una vez que tenemos el cursor, debemos leer los datos
#tenemos un metodo llamado fetchone() que se mueve una fila 
#cada vez que lo ejecutamos
#nos devuelve la fila en la que estamos posicionados
#Comentarios en bloque en VS code
#seleccionamos lo que deseamos comentar
#Comentar:Command/control +k+c
#Descomentar : Command/control +k + u
# row = cursor.fetchone()#primera fila
# print(row)
# row = cursor.fetchone()#segunda fila
# print(row)
# row = cursor.fetchone()#tercera fila
# print(row)
# row = cursor.fetchone()#cuarta fila
# print(row)
# #que sucede cuando leeemos una fila si no tenemos mas??
# row = cursor.fetchone()#quinta fila
# print(row)
# row = cursor.fetchone()#sexta fila
# print(row)
#siempre que finaleicemos las acciones , debemos
#liberar los recursos
cursor.close()
connection.close()
print("Fin de programa")
#si queremos leer todos los registros del cursor:
#1)while
# row = cursor.fetchone ()
# while (cursor.fetchone()!=None):
#     print("leer filas")
#     row = cursor.fetchone()
#2)for
for row in cursor:
    print(row)
    #Tambien podemos extraer los datos de alguna
    #columna mediante su indice
    print(row[0]) #DEPT_NO
    print(row[1]) #DNOMBRE
    #En algunas BBDD nos permite extraer el dato
    # de la fila por el NOMBRE de ka columna
    # #Oracle no contiene la info de las columnas
    # nombre = row.DNOMBRE
    #print(nombre)
#3)Recorrer con variables el cursor
#Nuestra consulta tiene 3 columnas
for numero, nombre, localidad in cursor:
    print(nombre) 
    

 