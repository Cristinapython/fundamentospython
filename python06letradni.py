print ("calcular letra NIF")
print ("introduzca letra de DNI")
dni = int(input())
#(nº DNI - (ENTERO(nº DNI / 23) * 23 )
resultado = dni - (int(dni / 23) * 23)
print(resultado)
if (resultado == 0):
print ("A")
elif (resultado == 1 ):
print ("B")

