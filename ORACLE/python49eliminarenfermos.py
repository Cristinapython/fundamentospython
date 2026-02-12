from oracle49enfermos import OracleEnfermos
print("Programa eliminar enfermo")
#Creamos nuestra clase oracle
oracle = OracleEnfermos()
print("Introduzca una inscrpcion")
dato = int(input())
registros = oracle.eliminarEnfermo(dato)
print(f"Enfermos eliminados: {registros}")
print("Fin del programa")
