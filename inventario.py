class Inventario:
    def __init__(self):
        self.items = []
    
    def agregar_item(self, item):
        self.items.append(item)
        print(f"Se ha agregado {item.nombre} al inventario.")
    
    def listar_items(self):
        if not self.items:
            print("El inventario está vacío.")
        for i, item in enumerate(self.items, start=1): # enumerate es para enumerar los items desde el numero 1
            print(f"{i}. {item.nombre} (Daño: {item.danio})")
    
    def inventario_vacio(self):
        return len(self.items) == 0
    
    def sacar_item(self, numero):
        return self.items.pop(numero - 1) 
            
    
    