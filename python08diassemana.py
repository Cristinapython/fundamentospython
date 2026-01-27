
print ("dia de la semana")
print("introduzca dia de nacimiento")
dia = int (input())
print("introduzca mes de nacimiento")
mes = int (input())
print("introduzca ano de nacimiento")
ano = int (input())
if (mes == 1):
    mes = 13
    ano = ano - 1
elif (mes == 2):
    mes = 14
    ano = ano - 1    
resultado1 = int(((mes + 1) * 3) / 5)
resultado2 = int(ano / 4)
resultado3 = int(ano / 100)
resultado4 = int(ano / 400)
resultado5 = int(dia + (2 * mes) + ano + resultado1 + resultado2 - resultado3 + resultado4 + 2)
resultado6 = int(resultado5 / 7)
resultado7 = int(resultado5 - (resultado6 * 7))
if (resultado7 == 0):
    print("Sabado")
elif (resultado7 == 1):
    print("Domingo")
elif (resultado7 == 2):
    print("Lunes")     
elif (resultado7 == 3):
    print("Martes")
elif (resultado7 == 4):
    print("Miercoles") 
elif (resultado7 == 5):
    print("Jueves")    
elif (resultado7 == 6):
    print("Viernes")  
print("fin de programa")               
