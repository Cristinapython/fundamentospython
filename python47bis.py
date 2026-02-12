#vamos a realizar un programa para insertar doctor.
#los datos que vamos a pedir del doctor son los diguientes:
#id doctor, apellido. especialidad y salario
#insert
#una vez que pedimos ESTOS DATOS
#MOSTRAREMOS MENU CON LOS HOSPITALES PARA QUE EL USUARIO
#SELECCIONE A QUE HOSPITAL QUIERE LLEVAR AL DOCTOR
import oracledb
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
sql = "select max(DOCTOR_NO) + 1 as MAXIMO from DOCTOR" # nos da el nº de doctor 
#automatico eligiendo el ultimo + 1
cursor.execute(sql)
row = cursor.fetchone()
iddoctor = row[0]
#comenzamos a pedir datos al usuario
apellido = input("Introduzca apellido: ")
espe = input("Especialidad:")
salario = int(input("Salario doctor:"))
#Necesitamos mostrar los hospitales
#lo que nos interesa son los codigos de los hospitales
print("Debe selecciona un hospital a continuacion")
sql = "select NOMBRE, HOSPITAL_COD from HOSPITAL"
cursor.execute(sql)
listaCodigos = []
contador = 1 #seleccionamos un contador para que el usuario pueda elegir
for row in cursor:
    print(f"{contador}.-{row[0]}")
    listaCodigos.append(row[1])
    contador = contador + 1
print("Seleccione un hospital")
opcion = int(input())   
idHospital = listaCodigos[opcion - 1] 
sql = "insert into DOCTOR values (:hosp,:id,:ap,:fun,:sal)"
cursor.execute(sql, (idHospital, iddoctor, apellido, espe, salario,))
connection.commit
print("Doctor insertado")
cursor.close()
connection.close()
print("Fin de programa")
