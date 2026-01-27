print("Calcular Salario trabajador")
horas = int(input("Horas trabajadas:"))
importe_hora = int(input("Importe hora:"))
km = int(input("kilometros viajados:"))
(horas > 36):
salario_base = 0
salario_extra = 0
salario_final = 0
destino = ""
retencion = ""
iva = 0
if (horas > 36):
    horas_extra = horas -36
    salario_base = importe_hora * 36
    salario_extra = (importe_hora + 1,5) * horas_extra
else:
    horas_extra= 0
    salario_extra = 0
    salario_base = importe_hora * horas
if (km >101 and km <900):
    dieta  = NACIONAL
else (km >900):
    dieta =  INTERNACIONAL
elif (km < 101 km):
    dieta PROVINCIAL        

salario horas_extra = salario total - 864    
salario total = 864 + ((precio hora extra + 1,5) * horas_extra)  
if (salario total >= 250):
    print ("Retencion 0%")
elif (salario total > 250 and <= 500):
    print ("Retencion 20%") 
else (Salario total > 500):
    print ("Retencion 50%")
print("HORAS TRABAJADAS:" , horas)
print("HORAS EXTRAS", horas_EXTRA)
print("IMPORTE HORA", importe_hora)
print("KILOMETROS", km)
print("DESTINO")
print("RETENCION")

           
