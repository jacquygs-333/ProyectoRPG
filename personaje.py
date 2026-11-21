from inventario import Inventario

class Personaje:
    def __init__(self, nombre, vida, arma):
        self.nombre = nombre
        self.__vida = vida # privada: nadie puede modificarla directamente
        self.vida_maxima = vida
        self.arma = arma
        self.inventario = Inventario()
    
    def consultar_salud(self):
        return self.__vida
    
    def atacar(self, arma):
        danio = arma.usar()
        print(f"{self.nombre} ataca con {arma.nombre} causando {danio} de daño.")
        return danio
    
    def recibir_danio(self, danio):
        if danio < 0:
            return
        self.__vida = max(0, self.__vida - danio)
        print(f"{self.nombre} recibe {danio} de daño. Vida restante: {self.__vida}")
    
    def curar(self, cantidad):
        if cantidad <0:
            return
        self.__vida = min(self.vida_maxima, self.__vida + cantidad)
        print(f"{self.nombre} recupera {cantidad} de vida. Vida: {self.__vida}")

    def esta_vivo(self):
        return self.__vida > 0