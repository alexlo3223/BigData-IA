#Ejercicio 1
class Coche:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

coche1 = Coche("Toyota","Corola")
coche2 = Coche("Seat","Panda")
print("Ejercicio 1")
print(coche1.marca, "y",coche1.modelo)
print(coche2.marca, "y",coche2.modelo)

#Ejercicio 2
class CochePruebas:
    def __init__(self):
        self.velocidad = 0
    def acelerar(self):
        self.velocidad += 10
    def detener(self):
        self.velocidad = 0

cPrueba1 = CochePruebas()
cPrueba2 = CochePruebas()

for i in range(3):
    cPrueba1.acelerar()

for i in range(2):
    cPrueba2.acelerar()

cPrueba2.detener()

print("")
print("Ejercicio 2")
print("Velocidades: Coche 1:", cPrueba1.velocidad, "Coche 2:", cPrueba2.velocidad)

#Ejercicio 3
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def describir(self):
        return f"Vehículo: {self.marca} {self.modelo}"

class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
    
ev = CocheElectrico("Toyota", "Carola", 5)
print()
print("Ejercicio 3")
print(ev.describir())

#Ejercicio 4
class Motor:
    def __init__(self, modelo):
        self.modelo = modelo
    def arrancar(self):
        return f"Motor en marcha"
    
class MotorGasolina(Motor):
    def arrancar(self):
        return f"Motor de gasolina en marcha"

class MotorElectrico(Motor):
    def arrancar(self):
        return f"Motor de electrico en marcha"
    
m1 = MotorGasolina("TSI 1.5")
m2 = MotorElectrico("EV-200")

print()
print("Ejercicio 4")
print(m1.modelo, "->", m1.arrancar())
print(m2.modelo, "->", m2.arrancar())

#Ejercicio 5
def poner_en_marcha(motor):
    return motor.arrancar()

motores = [MotorGasolina("Modelo 1"), MotorElectrico("Modelo 2")]

print()
print("Ejercicio 5")
for motor in motores:
    print(poner_en_marcha(motor))

class MotorDiesel(Motor):
    def arrancar(self):
        return f"Motor de diesel en marcha"

motores.append(MotorDiesel("Modelo 3"))

print()
for motor in motores:
    print(poner_en_marcha(motor))

