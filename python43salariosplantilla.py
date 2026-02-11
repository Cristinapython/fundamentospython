import oracledb
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
print("Introduzca Codigo Hospital: ")
idhospital = int(input())
print("Introduzca incremento salario:")
incremento = int(input())
sql = "update PLANTILLA set SALARIO= SALARIO + :subida where HOSPITAL_COD =:codigo"
#de izquierda a derecha buscara dentro de la condulta los : (dos puntos)
cursor.execute(sql, (incremento, idhospital,))
registros = cursor.rowcount# nos dice el numero de registros afectados por la consulta (update, delete o insert)
connection.commit()
print(f"Salarios subidos:{registros}")  
sql ="select * from PLANTILLA where HOSPITAL_COD=:codigo" #esta parte es para que nos muestre 
cursor.execute(sql, (idhospital,))
for row in cursor:
    print(f"Apellido: {row[3]}, Salario: {row[6]}, Hospital: {row[1]}")#row 3 apellido row 6 salario row 0 codigo hospital
cursor.close()
connection.close()
print("Fin de programa")    