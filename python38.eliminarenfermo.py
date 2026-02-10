import oracledb
#creamos conexion oracle
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
#antes mostramos los enfermos (apellido, inscripcion)
cursor = connection.cursor()
sql = "select APELLIDO, INCRIPCION from ENFERMO"
cursor.execute(sql)
for row in cursor:
    print(row[0] + ", Inscripcion:" + str(row[1]))
#cursor.close()    
print("Introduzca inscripcion par eliminar:")
dato = input()
sql = "delete from ENFERMO where INSCRIPCION=" + dato
cursor.execute(sql)
#Como es una consulta de accion dibujamos los 
#registros eliminados
afectados = cursor.rowcount
print("Registros eliminados: " + str(afectados))
#if(afectados>20)
connection.commit()
cursor.close
connection.close()   
print("Fin de programa")
