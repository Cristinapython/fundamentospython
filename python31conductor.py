from class31coche import Coche
from class31deportivo import Deportivo

print("Conduciendo ...")
depor = Deportivo()
depor.arrancar()
depor.acelerar()
depor.turbo()
car = Coche()
car.marca = "Pontiac"
car.modelo = "Firebird"
print(car.marca + "" + car.modelo)
car.arrancar()
car.acelerar()
car.acelerar()
car.acelerar()
car.frenar()
