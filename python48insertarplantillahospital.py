#insertar una persona en la plantilla 
#el id de la plantilla lo generamos dentro del programa
#pediremos ala usuario Apellido, funcion, turno y salario y codigo de sala
#mostraremos un menu de hospitales
import oracledb
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
sql = "select max(EMPLEADO_NO) + 1 as MAXIMO from PLANTILLA" # nos da el nº de EMPLEADO
#automatico eligiendo el ultimo + 1
cursor.execute(sql)
row = cursor.fetchone()
idempleado = row[0]
#comenzamos a pedir datos al usuario
apellido = input("Introduzca apellido: ")
funcion = input("Funcion:")
salario = int(input("Salario empleado:"))
turno = input("Turno (M,T,N):")
sala = int(input("Sala: "))
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
sql = "insert into PLANTILLA values (:hosp,:sala,:id,:ap,:func,:tur,:salar)"
cursor.execute(sql, (idHospital, sala, idempleado, apellido, funcion, turno, salario,))    
connection.commit
print("Empleado insertado")
cursor.close()
connection.close()
print("Fin de programa")
