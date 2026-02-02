#definimos clase
class Mascota:
    def __init__(self):
        self.nombre = ""
        self.raza = ""
        self.anyonacimiento = 0
        self.anyoadopcion = 0
#metodo para saber años de adopcion desde el nacimiento
    def getaniosAdoptado(self):
        return 2026-self.anyoadopcion   