import oracledb
#creamos conexion oracle
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
print ("Introduzca numero de departamento")
numero = int(input())
sql = "select apellido, oficio, dept_no from EMP where DEPT_NO=:deptno"

print (sql)
cursor.execute(sql, (numero,))
for apellido, oficio, dept in cursor:
    print(f"Apellido: {apellido}, Oficio: {oficio}, Departamento: {dept}")
cursor.close
connection.close()   
print("Fin de programa")