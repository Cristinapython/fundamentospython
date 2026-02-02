class Coche:
    #declaramos las propiedades del constructor
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.velocidad = 0
        self.estado = False

    def arrancar(self): 
        self.estado = True
        print("Coche arrancado")
    def detener(self):
        self.estado = False
        print("Coche apagado")
    def acelerar(self):
        if(self.estado ==False):
            print("Enciende coche !!!, Ande vas!!")  
        else:
            self.velocidad    




