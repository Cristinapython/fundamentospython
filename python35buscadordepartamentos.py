import oracledb
#creamos conexion oracle
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
print("conectado")
#Pedimos el departamento al usuario
print("Introduce un ID de departamento")
iddepartamento = input()
#Necesitamos una consulta para buscar departamento
sql = "select *from DEPT where DEPT_NO=" + iddepartamento
print(sql)
#Creamos un cursor
cursor = connection.cursor()
#Ejecutamos la consulta oara traer los datos
cursor.execute (sql)
#Recuperamos la primera fila
row = cursor.fetchone()
#Comprobamos si tenemos datos en la fila
if(row==None):
    print("NO existe el departamento")
else:
    #Recuperamos los datos
    nombre = row [2]#DNOMBRE
    localidad = row[3]#LOC
    print(nombre + ", " + localidad)
#Libreamos recursos
cursor.close()
connection.close()
