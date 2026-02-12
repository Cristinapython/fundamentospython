#quiero un menu con las funciones de la PLANTILLA.
#el usuario seleccionara una funcion y mostrara los apellidos de la funcion seleccionada
import oracledb
connection = oracledb.connect(user="SYSTEM", password="oracle"
                              , dsn="localhost/FREEPDB1")
cursor = connection.cursor()
#Necesitamos una lista de funciones[]
listaFunciones = []
sql = "select distinct FUNCION from PLANTILLA"
cursor.execute(sql)#ejecutamos la consulta
#Recorremos las funciones
for row in cursor:
    #Agregamos cada FUNCION
    listaFunciones.append(row[0])
#Recorremos la lista para nuestro menu
#creamos un contador para el dibujo bonito
contador = 1
for fun in listaFunciones:
    print(f"{contador}.-{fun}")
    contador = contador + 1
print("seleccione una opcion")    
opcion = int(input())
funcionSeleccionada = listaFunciones[opcion - 1]
print(f"Opcion selecionada: {funcionSeleccionada}")    
#Consultamos los empleados con la funcion seleccionada
sql = "select APELLIDO from PLANTILLA where FUNCION=:funcion"
cursor.execute(sql, (funcionSeleccionada,))
print("-------Lista de empleados---------")
for row in cursor:
    print(f"-{row[0]}")
cursor.close
connection.close()
print("FIN DEL PROGRAMA")