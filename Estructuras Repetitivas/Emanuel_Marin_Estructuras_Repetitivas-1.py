# Ejercicio 1— “Caja del Kiosco”
nombre = input("Ingrese el nombre del cliente: ")
while nombre.isalpha() == False:
    print("Error: El nombre solo puede contener letras.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad_prods = input("Ingrese la cantidad de productos que desea comprar: ")
while cantidad_prods.isdigit() == False or int(cantidad_prods) <= 0:
    print("Error: La cantidad de productos debe ser un número entero mayor que 0.")
    cantidad_prods = input("Ingrese la cantidad de productos que desea comprar: ")

cantidad_prods = int(cantidad_prods)
lista_prod = []
for i in range(0, cantidad_prods):
    producto = []
    producto.append(f"Producto {i + 1}")
    producto.append(input(f"Ingrese el precio del producto {i + 1}: "))
    while producto[1].isdigit() == False:
        print("Error: El precio debe ser un número entero.")
        producto[1] = input(f"Ingrese el precio del producto {i + 1}: ")
    producto[1] = int(producto[1])
    producto.append(input(f"""Si el producto {i + 1} tiene descuento ingrese "s" de lo contrario ingrese "n": """).lower())
    while producto[2] != "s" and producto[2] != "n":
        print("Error: Ingrese una letra válida.")
        producto[2] = input(f"""Si el producto {i + 1} tiene descuento ingrese "s" de lo contrario ingrese "n": """).lower()

    if producto[2] == "s":
        producto.append(producto[1] * 0.9)
    else:
        producto.append(producto[1])

    lista_prod.append(producto)

total = 0
total_desc = 0
for i in range(0, cantidad_prods):
    total += lista_prod[i][1]
    total_desc += lista_prod[i][3]

ahorro = total - total_desc
promedio = total_desc / cantidad_prods

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad_prods}")
for i in range(0, cantidad_prods):
    print(f"{lista_prod[i][0]} - Precio: {lista_prod[i][1]} - Descuento (S/N): {lista_prod[i][2]}")
print("")
print(f"Total sin descuentos: ${total}")
print(f"Total con descuentos: ${total_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: {promedio:.2f}")

input("Presione enter para salir.")