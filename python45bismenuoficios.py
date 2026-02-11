import oracledb
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
#Necesitamos una lista de oficios[]
listaOficios = []
sql = "select distinct OFICIO from EMP"
cursor.execute(sql)#ejecutamos la consulta
#Recorremos los oficios
for row in cursor:
    #Agregamos cada oficio
    listaOficios.append(row[0])
#Recorremos la lista para nuestro menu
#creamos un contador para el dibujo bonito
contador = 1
for ofi in listaOficios:
    print(f"{contador}.-{ofi}")
    contador = contador + 1
print("seleccione una opcion")    
opcion = int(input())
oficioSeleccionado = listaOficios[opcion - 1]
print(f"Opcion selecionada: {oficioSeleccionado}")3
#Consultamos los empleados con el oficio seleccionado
sql = "select * from EMP where OFICIO=:oficio"
cursor.execute(sql, (oficioSeleccionado,))
print("-------Lista de empleados---------")
for row in cursor:
    #print("-" + row[1] + ", Salario: " + str(row[5])) ----esta es otra opcion
    print(f"-{row[1]}")
cursor.close
connection.close()
print("FIN DEL PROGRAMA")