class CarritoCompras:
    def __init__(self):
        self.catalogo = {
            1: {"producto": "Laptop Gamer", "precio": 800.0},
            2: {"producto": "Smartphone", "precio": 400.0},
            3: {"producto": "Auriculares Bluetooth", "precio": 50.0}
        }
        self.items_seleccionados = []

    def mostrar_catalogo(self):
        print("\n--- CATALOGO DE PRODUCTOS ---")
        for codigo, info in self.catalogo.items():
            print(f"[{codigo}] {info['producto']} - ${info['precio']:.2f}")

    def agregar_al_carrito(self, codigo):
        if codigo in self.catalogo:
            self.items_seleccionados.append(self.catalogo[codigo])
            print(f"Confirmacion: {self.catalogo[codigo]['producto']} agregado al carrito.")
            return True
        print("Error: Codigo de producto no valido.")
        return False

    def calcular_total(self):
        return sum(item["precio"] for item in self.items_seleccionados)

    def vaciar_carrito(self):
        self.items_seleccionados = []
