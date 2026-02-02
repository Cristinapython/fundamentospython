from class32mes import Mes
print("Trabajando con clases")
for i in range(3):
    #aqui creamos un nuevo mes
    mes = Mes()
    print("Introuzca el mes", (i+1))
    mes.nombre = input()
    print("Temperatura maxima")
    mes.temperaturaMaxima = int(input())
    print("Temperatura Minima")
    mes,temperaturaMinima = int(input())
    listaMeses.append(mes)
#Recorremos los meses que hemos almacenado
mediaAnual = 0
for dato in listaMeses:
    print(dato.nombre + ", Maxima " + str(dato.temperaturaMaxima)) 
    print("Minima" + str(dato.temperaturaMinima))
    print("Media ", dato.getTemperaturaMedia())
    mediaAnual = mediaAnual + dato.getTemperaturaMedia()
print("Media anual ", mediaAnual)    
print("Fin programa")    
