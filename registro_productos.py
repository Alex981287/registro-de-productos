def mostrar_productos(productos):
    print("\n--- PRODUCTOS REGISTRADOS ---")

    if not productos:
        print("No hay productos registrados.")
    else:
        for codigo, producto in productos.items():
            print(f"Código: {codigo}")
            print(f"Producto: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            print("-----------------------------")


def agregar_producto(productos):
    codigo = input("Ingrese el código del producto: ")

    if codigo in productos:
        print("Ese código ya está registrado.")
        return

    nombre = input("Ingrese el nombre del producto: ")

    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Ingrese valores numéricos válidos.")
        return

    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    print("Producto agregado correctamente.")


def buscar_producto(productos):
    codigo = input("Ingrese el código que desea buscar: ")

    if codigo in productos:
        producto = productos[codigo]

        print("\n--- PRODUCTO ENCONTRADO ---")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
    else:
        print("Producto no encontrado.")


def eliminar_producto(productos):
    codigo = input("Ingrese el código del producto que desea eliminar: ")

    if codigo in productos:
        del productos[codigo]
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def main():
    productos = {}

    while True:
        print("\n===== REGISTRO DE PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(productos)

        elif opcion == "2":
            mostrar_productos(productos)

        elif opcion == "3":
            buscar_producto(productos)

        elif opcion == "4":
            eliminar_producto(productos)

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()