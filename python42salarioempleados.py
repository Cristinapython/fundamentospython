import oracledb
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
print("Introduzca Oficio: ")
oficio= input()
print("Introduzca incremento salario:")
incremento = int(input())
sql = "update EMP set SALARIO= SALARIO + :dato1 where OFICIO =:dato2"
#de izquierda a derecha buscara dentro de la condulta los : (dos puntos)
cursor.execute(sql, (incremento, oficio,))
registros = cursor.rowcount# nos dice el numero de registros afectados por la consulta
connection.commit()
print(f"Empleados afectados:{registros}")  
sql ="select * EMP where OFICIO=:inventado"
cursor.execute(sql, (oficio,))
for row in cursor:
    print(f"{row[1]}, Salario: {row[5]}")#row 1 apellido row 5 salario
cursor.close()
connection.close()
print("Fin de programa")    