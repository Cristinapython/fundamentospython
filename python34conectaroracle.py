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
row = cursor.fetchone()#primera fila
print(row)
row = cursor.fetchone()#segunda fila
print(row)
row = cursor.fetchone()#tercera fila
print(row)
row = cursor.fetchone()#cuarta fila
print(row)
#que sucede cuando leeemos una fila si no tenemos mas??
row = cursor.fetchone()#quinta fila
print(row)
row = cursor.fetchone()#sexta fila
print(row)
#siempore que finaleicemos las acciones , debemos
#liberar los recursos
cursor.close()
connection.close()
print("Fin de programa")