from oracle50empleados import OracleEmpleados
print("Programa eliminar empleado")
#Creamos nuestra clase oracle
oracle = OracleEmpleados()
print("Introduzca numero de empleado")
dato = int(input())
registros = oracle.eliminarEmpleado(dato)
print(f"Empleados eliminados: {registros}")
print("Fin del programa")
