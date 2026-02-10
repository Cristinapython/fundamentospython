import oracledb
#creamos conexion oracle
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
#creamos un cursor para las consultas
cursor = connection.cursor()
print("Id departamento")
id = input()#88
print ("Nombre departamento")
nombre=input()#NUEVO
print("Localidad")
localidad = input()#NUEVO
#insert into DEPT values(88, 'NUEVO', 'NUEVO')
sql = f"insert into DEPT values({id}, '{nombre}', '{localidad}')"
#realizamos la accion de insertar
cursor.execute(sql)
connection.commit()
#Realizamos la consulta de seleccion
sql = "select * from DEPT"
cursor.execute(sql)
for row in cursor:
    num = row[0]
    nom = row[1]
    loc = row[2]
    print (f"id: {num}, Nombre: {nom}, Localidad: {loc}") 
cursor.close
connection.close()   
print("Fin de programa")    
#en python tenemos una forma de concatenar tambien
#utilizando solamente un string sin + y sin nada 
# para ello , se utiliza la letra f fuera del string
# y cada variable  ira dentro de llaves dentro del string
#                             