# Función para registrar un cliente
def registro_cliente():
    Nombre = input("Nombre: ")
    Dni = input("DNI: ")
    Numero_de_telefono = input("Numero de telefono: ")
    Nacionalidad = input("Nacionalidad: ")

    # Abre el archivo "Cliente.txt" en modo de apertura para registrar clientes
    with open("Cliente.txt", "a") as archivo:
        # Con archivo.write conseguimos que nos añada el nombre, dni, numero de telefono y nacionalidad
        archivo.write(f"{Nombre},{Dni},{Numero_de_telefono},{Nacionalidad}\n")
    print("Te has registrado con éxito")

# Función para visualizar todos los clientes
def visualizar_clientes():
    # Ahora abrimos el txt en modo lectura
    with open("Cliente.txt", "r") as archivo:
        for line in archivo:
            Nombre, Dni, Numero_de_telefono, Nacionalidad = line.strip().split(',')
            print(f"Nombre: {Nombre}, DNI: {Dni}, Numero de telefono: {Numero_de_telefono}, Nacionalidad: {Nacionalidad}")

# Función para buscar un cliente por su nombre o DNI
def buscar_cliente():
    busqueda = input("Introduce el Nombre o DNI del cliente que deseas buscar: ")
    encontrar_cliente = False
    with open("Cliente.txt", "r") as archivo:
        for line in archivo:
            Nombre, Dni, Numero_de_telefono, Nacionalidad = line.strip().split(',')
            if busqueda in Nombre or busqueda in Dni:
                encontrar_cliente = True
                print(f"Nombre: {Nombre}, DNI: {Dni}, Numero de telefono: {Numero_de_telefono}, Nacionalidad: {Nacionalidad}")
    if not encontrar_cliente:
        print("Cliente no encontrado.")

# Función para realizar una compra asociada a un cliente
def realizar_compra():
    # Solicitar información del cliente
    nombre_cliente = input("Introduce el nombre del cliente: ")

    # Verificar si el cliente existe
    if buscar_cliente_por_nombre(nombre_cliente):
        # Lista de productos con stock y precio
        productos = [
            {"nombre": "Pantalon", "stock": 10, "precio": 20.0},
            {"nombre": "Sudadera", "stock": 15, "precio": 30.0},
            {"nombre": "Camiseta", "stock": 5, "precio": 15.0},
            # Agrega más productos según sea necesario
        ]

        # Recopilar información de la compra
        print("Productos disponibles:")
        for i, producto in enumerate(productos, 1):
            print(f"{i}. {producto['nombre']} - Stock: {producto['stock']}, Precio: €{producto['precio']:.2f}")

        # Seleccionar producto, por el numero de posicion
        opcion_producto = int(input("Selecciona un producto(numero de posicion): "))
        producto_elegido = productos[opcion_producto - 1]

        cantidad = int(input("Cantidad a comprar: "))

        # Verificar disponibilidad de stock
        if cantidad <= producto_elegido["stock"]:
            total = cantidad * producto_elegido["precio"]

            # Actualizar el stock del producto
            producto_elegido["stock"] -= cantidad

            # Abrir el archivo "Compra.txt" en modo de apertura para registrar la compra
            with open("Compra.txt", "a") as archivo_compras:
                # Escribir la información de la compra en el archivo
                archivo_compras.write(f"{nombre_cliente},{producto_elegido['nombre']},{cantidad},{total}\n")

            print("Compra realizada con éxito.")
        else:
            print("No hay suficiente stock disponible.")
    else:
        print("Cliente no encontrado. Realiza el registro del cliente primero.")

# Función para buscar un cliente por su DNI
def buscar_cliente_por_nombre(nombre):
    with open("Cliente.txt", "r") as archivo_clientes:
        for line in archivo_clientes:
            nombre_cliente,_, _, _ = line.strip().split(',')
            if nombre == nombre_cliente:
                return True
    return False

# Función para visualizar todas las compras realizadas
def visualizar_compras():
    # Abre el archivo "Compra.txt" en modo lectura
    with open("Compra.txt", "r") as archivo_compras:
        print("Compras realizadas:")
        for line in archivo_compras:
            # Verificar si hay suficientes elementos para desempaquetar
            if line.strip():
                nombre_cliente, producto, cantidad, total = line.strip().split(',')
                print(f"Cliente: {nombre_cliente}, Producto: {producto}, Cantidad: {cantidad}, Total: €{total}")
            else:
                print("Error: Formato incorrecto en una línea del archivo 'Compra.txt'")


# Bucle while True con el menú completo
while True:
    print("\nGestión clientes y compras")
    print("1. Registrar cliente")
    print("2. Visualizar clientes")
    print("3. Buscar clientes")
    print("4. Realizar compra")
    print("5. Visualizar compras")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        registro_cliente()
    elif opcion == '2':
        visualizar_clientes()
    elif opcion == '3':
        buscar_cliente()
    elif opcion == '4':
        realizar_compra()
    elif opcion == '5':
        visualizar_compras()
    elif opcion == '6':
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
