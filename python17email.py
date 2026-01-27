print("Escriba su direccion de correo:")
texto = input ()
#if (texto.find("@") == -1):
#if (texto.find("@") == 0):
if (texto.find("@") == -1):
   print("Falta @")  
elif (texto.find(".") == -1):
   print("Falta .") 
elif (texto.startswith("@") or texto.endswith("@")):
   print ("@ al inicio o al final")
elif (texto.find("@") != texto.rfind("@")):
   print("existe mas de una @")   
elif (texto.rfind(".") < texto.find("@")):
   print("debe existir un pinto despues d @") 
else:
   ultimopunto = texto.rfind(".")   
   dominio = texto[ultimopunto + 1:]
   longdominio = len (dominio)
   if(longdominio >= 2 and longdominio <= 3):
      print("Email correcto")
   else:
      print("El dominio debe ser de 2 a 4 caracteres") 
      print("fin de program")  


   
