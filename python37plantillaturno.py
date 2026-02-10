import oracledb
#creamos conexion oracle
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
print("conectado")
print ("Dame un turno (T,M,N)")
turno = input()
sql = "select APELLIDO, FUNCION from PLANTILLA where TURNO='" + turno + "'"
print(sql)#pintar la consulta que hacemos dinamicamente
cursor = connection.cursor()
cursor.execute (sql)
for row in cursor:
    apellido = row[0]
    funcion = row[1]
    print(apellido + ", " + funcion)
cursor.close()
connection.close()   
print("Fin de programa")
