from class30persona import Persona
print("Manejando clases persona")
#Creamos una persona
persona1 = Persona()
persona1.nombre = "Roger"
persona1.apellidos = "Rabit"
persona1.anyonacimiento = 1989
persona1.pais = "EEUU"
print("Edad falsa: ", persona1.getEdad())
print(persona1.getNombreCompleto())
print("Edad persona 1: ", persona1.getEdad())
persona2 = Persona()
print("persona pais", persona2.pais)
print("fin programa")

