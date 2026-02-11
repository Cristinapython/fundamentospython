import oracledb
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
sql = "select DEPT_NO from DEPT"
cursor.execute(sql)
print("------Menu departamentos -------")
for row in cursor:
    print(row[0])
print("SEleccione un departamento") 
iddept = int((input()))  
sql = "select APELLIDO, OFICIO from EMP where DEPT_NO=:iddept" 
cursor.execute(sql, (iddept,))
print("-------Empleados departamento--------")
for ape, ofi, in cursor:
    print(f"{ape}, oficio: {ofi}")
cursor.close()
connection.close()
print("Fin de programa")