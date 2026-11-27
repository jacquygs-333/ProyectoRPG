class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio
        
    def usar(self):
        print(f"Ataque con {self.nombre}")
        return self.danio