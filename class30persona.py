class Persona:
    #podemos declarar las propiedades aqui
    #debemos asignar un valor
    nombre = ""
    apellidos = ""
    pais = ""
    email = ""
    anyonacimiento = ""

    #Un constructor es el primer lugar que utiliza 
    #cualquier programa con mi clase persona
    def__init__(self):
        self.pais = "Francia"
    #Metodos son acciones sobre la clase persona
    def getNombreCompleto(self):
        return self.nombre + "" + self.apellidos  

    def getEdad(self):
        return 2026-self.anyonacimiento    

    def getEdadFalsa(self, anyosquitados):
        return 2026 - self.anyonacimiento - anyosquitados


