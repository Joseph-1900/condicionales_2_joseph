productos_en_oferta = ["manzanas", "bananas", "leche", "pan", "yogur"]

while True:
    producto = input("Ingrese un producto para verificar si está en oferta (o 'salir' para finalizar): ").lower()

    if producto == 'salir':
        break 
    if producto in productos_en_oferta:
        print(f"{producto.capitalize()} está en oferta.")
    else:
        print(f"{producto.capitalize()} no está en oferta.")


