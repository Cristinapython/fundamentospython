import oracledb
#creamos conexion oracle
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
print("conectado")
#Pedimos el Nº DE INSCRIPCION al usuario
print("Introduce N. DE INSCRIPCION")
ninscripcion = input()
#Necesitamos una consulta para buscar departamento
sql = "select APELLIDO, DIRECCION from ENFERMO where INSCRIPCION=" + ninscripcion
print(sql)
#Creamos un cursor
cursor = connection.cursor()
#Ejecutamos la consulta oara traer los datos
cursor.execute (sql)
#Recuperamos la primera fila
row = cursor.fetchone()
#Comprobamos si tenemos datos en la fila
if(row==None):
    print("No existe ese número de inscripcion")
else:
 #Recuperamos los datos
    apellido = row [0]#APELLIDO
    direccion = row [1]#DIRECCION
    print(apellido + ", " + direccion)   
#Libreamos recursos
cursor.close()
connection.close()  
print("Fin de programa")   