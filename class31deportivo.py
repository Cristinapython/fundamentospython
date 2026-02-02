from class31coche import Coche

class Deportivo(Coche):
    def turbo(self):
        self.velocidad += 100
        print("turbo a tope ", self.velocidad)

    def acelerar(self):
        self.velocidad += 45
        print("Acelerando el deportivo", self.velocidad)