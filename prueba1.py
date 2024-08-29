class Articulos:
    def __init__(self, tipo, detalle, precio_compra):
        self.tipo = tipo
        self.detalle = detalle
        self.precio_compra = precio_compra
        self.margen_ganancia = 1.30
        self.precio_venta = round(precio_compra * self.margen_ganancia, 2)
        self.marca = "Hojitas" if tipo == "Cuaderno" else "Rayas"

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Detalle: {self.detalle}")
        print(f"Marca: {self.marca}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print("--------------------------------------------------------------")
