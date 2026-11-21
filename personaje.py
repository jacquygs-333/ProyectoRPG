from inventario import Inventario

class Personaje:
    def __init__(self, nombre, vida, arma):
        self.nombre = nombre
        self.vida = vida
        self.arma = arma
        self.inventario = Inventario()
    
    def atacar(self, arma):
        danio = arma.usar()
        print(f"{self.nombre} ataca con {arma.nombre} causando {danio} de daño.")
        return danio
    
    def recibir_danio(self, danio):
        self.vida -= danio
        print(f"{self.nombre} recibe {danio} de daño. Vida restante: {self.vida}")