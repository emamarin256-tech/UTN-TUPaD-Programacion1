# Ejercicio 1
import random
print("Ejercicio 1")
notas = [7, 8, 6, 9, 10, 5, 8, 7, 9, 6]


print("Notas de los estudiantes:")

for nota in notas:
    print(nota)


suma = 0

for nota in notas:
    suma += nota

promedio = suma / len(notas)

print(f"Promedio: {promedio:.2f}")


mayor = notas[0]
menor = notas[0]

for nota in notas:
    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

print("Nota más alta:", mayor)
print("Nota más baja:", menor)
print("Ejercicio 1 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 2
print("Ejercicio 2")
productos = []
salir = False
for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    while producto == "":
        producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
ordenados = sorted(productos)
print("Productos ordenados alfabeticamente:")
for ordenado in ordenados:
    print(f"{ordenado}")
eliminado = input("Seleccione el producto que desee eliminar (1 - 5): ")
while eliminado not in ['1', '2', '3', '4', '5']:
    eliminado = input("Seleccione el producto que desee eliminar (1 - 5): ")
eliminado = int(eliminado) - 1
productos.remove(productos[eliminado])
print("Productos restantes:")
for producto in productos:
    print(f"{producto}")

print("-----------------------------------------------------------------------")
# Ejercicio 3
print("Ejercicio 3")
lista = []
pares = []
impares = []
for i in range(15):
    aleatorio = random.randint(1, 100)
    lista.append(aleatorio)
print("Lista de números:")
for i in lista:
    print(i)
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("Números pares:")
count = 0
for i in pares:
    count += 1
    print(i)
print(f"Cantidad de números pares: {count}")
count = 0
print("Números impares:")
for i in impares:
    count += 1
    print(i)
print(f"Cantidad de números impares: {count}")
print("Ejercicio 3 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 4
print("Ejercicio 4")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
unicos = []
for i in datos:
    if i not in unicos:
        unicos.append(i)
print("Números únicos:")
for i in unicos:
    print(i)
print("Ejercicio 4 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 5
print("Ejercicio 5")
estudiantes = ["Carlos", "María", "Juan",
               "Ana", "Luis", "Lucía", "Diego", "Sofía"]
print("Estudiantes:")
for estudiante in estudiantes:
    print(estudiante)
pregunta = input(
    "¿Queres agregar un nuevo estudiante o eliminar alguno? (Agregar/Eliminar): ").capitalize()

while pregunta not in ["Agregar", "Eliminar"]:
    pregunta = input(
        "¿Queres agregar un nuevo estudiante o eliminar alguno? (Agregar/Eliminar): ")

if pregunta == "Agregar":
    estudiantes.append("Pedro")
    for estudiante in estudiantes:
        print(estudiante)
elif pregunta == "Eliminar":
    estudiantes.remove("Diego")
    for estudiante in estudiantes:
        print(estudiante)

print("Ejercicio 5 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 6
print("Ejercicio 6")

datos = [1, 3, 5, 3, 7, 1, 9]
datos_modificables = [1, 3, 5, 3, 7, 1, 9]
print("Datos originales:")
for i in datos:
    print(i)
datos_modificables = datos[-1:] + datos[:-1]
print("Datos modificados:")
for i in datos_modificables:
    print(i)

print("Ejercicio 6 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 7
print("Ejercicio 7")
temperaturas = [[15, 22], [16, 24], [14, 21],
                [13, 19], [15, 22], [17, 26], [18, 28]]
minimas = []
maximas = []
amplitudes_termicas = []
for temp in temperaturas:
    minimas.append(temp[0])
    maximas.append(temp[1])
    amplitud_termica = temp[1] - temp[0]
    amplitudes_termicas.append(amplitud_termica)
for amplitud in amplitudes_termicas:
    if amplitud == max(amplitudes_termicas):
        maxima = amplitud
        indice = amplitudes_termicas.index(amplitud)
promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)
print("Temperaturas:")
count = 0
for temp in temperaturas:
    count += 1
    print(f"Día {count}:")
    for i in range(2):
        if i == 0:
            print(f"Minima: {temp[i]}")
        else:
            print(f"Maxima: {temp[i]}")

print(f"Promedio de las minimas: {promedio_minimas:.2f}")
print(f"Promedio de las maximas: {promedio_maximas:.2f}")
print("Ejercicio 7 finalizado")
print(f"""Día con mayor amplitud termica: "Día {indice + 1}" """)
print(f"Amplitud termica: {maxima}")
print("-----------------------------------------------------------------------")
# Ejercicio 8
print("Ejercicio 8")
notas = [[8.5, 9.0, 7.5], [6.0, 8.2, 9.1], [
    7.0, 6.5, 8.0], [9.5, 10.0, 9.2], [5.5, 7.0, 6.8]]
promedios_estudiantes = []
promedios_materias = []
for nota in notas:
    promedio = (nota[0] + nota[1] + nota[2]) / 3
    promedios_estudiantes.append(promedio)
for i in range(3):
    promedio = (notas[0][i] + notas[1][i] + notas[2]
                [i] + notas[3][i] + notas[4][i]) / 5
    promedios_materias.append(promedio)
count = 0
print("Promedios de los estudiantes:")
for promedio in promedios_estudiantes:
    count += 1
    print(f"Estudiante {count}: {promedio:.2f}")
print("Promedios de las materias:")
count = 0
for promedio in promedios_materias:
    count += 1
    print(f"Materia {count}: {promedio:.2f}")
print("Ejercicio 8 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 9
print("Ejercicio 9")
tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

ganador = False
print("Columnas  | 1 | 2 | 3 |")
print("------------------------")

numero_fila = 1

for fila in tablero:
    print(f"Filas {numero_fila}   | {fila[0]} | {fila[1]} | {fila[2]} |")
    numero_fila += 1

print("------------------------")
while not ganador:

    jugadorX = input(
        'Hola "X" jugador, indica tu movimiento (Fila y Columna): ').split()

    while len(jugadorX) != 2 or not jugadorX[0].isdigit() or not jugadorX[1].isdigit() or int(jugadorX[0]) < 1 or int(jugadorX[0]) > 3 or int(jugadorX[1]) < 1 or int(jugadorX[1]) > 3:
        print("Error: Ingrese dos números entre 1 y 3.")
        jugadorX = input(
            'Hola "X" jugador, indica tu movimiento (Fila y Columna): ').split()

    jugadorX[0] = int(jugadorX[0]) - 1
    jugadorX[1] = int(jugadorX[1]) - 1

    while tablero[jugadorX[0]][jugadorX[1]] != "-":
        print("Error: Esa posición ya está ocupada.")
        jugadorX = input(
            'Hola "X" jugador, indica tu movimiento (Fila y Columna): ').split()

        while len(jugadorX) != 2 or not jugadorX[0].isdigit() or not jugadorX[1].isdigit() or int(jugadorX[0]) < 1 or int(jugadorX[0]) > 3 or int(jugadorX[1]) < 1 or int(jugadorX[1]) > 3:
            print("Error: Ingrese dos números entre 1 y 3.")
            jugadorX = input(
                'Hola "X" jugador, indica tu movimiento (Fila y Columna): ').split()

        jugadorX[0] = int(jugadorX[0]) - 1
        jugadorX[1] = int(jugadorX[1]) - 1

    tablero[jugadorX[0]][jugadorX[1]] = "X"

    print("Columnas  | 1 | 2 | 3 |")
    print("------------------------")

    numero_fila = 1

    for fila in tablero:
        print(f"Filas {numero_fila}   | {fila[0]} | {fila[1]} | {fila[2]} |")
        numero_fila += 1

    print("------------------------")

    if (tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X" or
        tablero[1][0] == "X" and tablero[1][1] == "X" and tablero[1][2] == "X" or
        tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X" or
        tablero[0][0] == "X" and tablero[1][0] == "X" and tablero[2][0] == "X" or
        tablero[0][1] == "X" and tablero[1][1] == "X" and tablero[2][1] == "X" or
        tablero[0][2] == "X" and tablero[1][2] == "X" and tablero[2][2] == "X" or
        tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X" or
            tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X"):

        ganador = "X"
        break

    if "-" not in tablero[0] and "-" not in tablero[1] and "-" not in tablero[2]:
        ganador = "Empate"
        break

    jugadorO = input(
        'Hola "O" jugador, indica tu movimiento (Fila y Columna): ').split()

    while len(jugadorO) != 2 or not jugadorO[0].isdigit() or not jugadorO[1].isdigit() or int(jugadorO[0]) < 1 or int(jugadorO[0]) > 3 or int(jugadorO[1]) < 1 or int(jugadorO[1]) > 3:
        print("Error: Ingrese dos números entre 1 y 3.")
        jugadorO = input(
            'Hola "O" jugador, indica tu movimiento (Fila y Columna): ').split()

    jugadorO[0] = int(jugadorO[0]) - 1
    jugadorO[1] = int(jugadorO[1]) - 1

    while tablero[jugadorO[0]][jugadorO[1]] != "-":
        print("Error: Esa posición ya está ocupada.")
        jugadorO = input(
            'Hola "O" jugador, indica tu movimiento (Fila y Columna): ').split()

        while len(jugadorO) != 2 or not jugadorO[0].isdigit() or not jugadorO[1].isdigit() or int(jugadorO[0]) < 1 or int(jugadorO[0]) > 3 or int(jugadorO[1]) < 1 or int(jugadorO[1]) > 3:
            print("Error: Ingrese dos números entre 1 y 3.")
            jugadorO = input(
                'Hola "O" jugador, indica tu movimiento (Fila y Columna): ').split()

        jugadorO[0] = int(jugadorO[0]) - 1
        jugadorO[1] = int(jugadorO[1]) - 1

    tablero[jugadorO[0]][jugadorO[1]] = "O"

    print("Columnas  | 1 | 2 | 3 |")
    print("------------------------")

    numero_fila = 1

    for fila in tablero:
        print(f"Filas {numero_fila}   | {fila[0]} | {fila[1]} | {fila[2]} |")
        numero_fila += 1

    print("------------------------")

    if (tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O" or
        tablero[1][0] == "O" and tablero[1][1] == "O" and tablero[1][2] == "O" or
        tablero[2][0] == "O" and tablero[2][1] == "O" and tablero[2][2] == "O" or
        tablero[0][0] == "O" and tablero[1][0] == "O" and tablero[2][0] == "O" or
        tablero[0][1] == "O" and tablero[1][1] == "O" and tablero[2][1] == "O" or
        tablero[0][2] == "O" and tablero[1][2] == "O" and tablero[2][2] == "O" or
        tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O" or
            tablero[0][2] == "O" and tablero[1][1] == "O" and tablero[2][0] == "O"):

        ganador = "O"
        break
if ganador == "Empate":
    print("Empate")
else:
    print(f"El ganador es: {ganador}")
print("Ejercicio 9 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 10
print("Ejercicio 10")
matriz_ventas = [
    [12, 15, 10, 18, 20, 22, 25],
    [5,  8,  6,  7,  9,  11, 14],
    [20, 18, 22, 25, 24, 30, 35],
    [0,  2,  1,  3,  2,  5,  4]
]
leche = matriz_ventas[0]
yogurt = matriz_ventas[1]
manteca = matriz_ventas[2]
chocolate = matriz_ventas[3]
leche_total = sum(leche)
yogurt_total = sum(yogurt)
manteca_total = sum(manteca)
chocolate_total = sum(chocolate)
totales = [leche_total, yogurt_total, manteca_total, chocolate_total]
nombres = ["Leche", "Yogurt", "Manteca", "Chocolate"]
ventas = 0
dia_nombre = 0
for j in range(7):
    suma = matriz_ventas[0][j] + matriz_ventas[1][j] + \
        matriz_ventas[2][j] + matriz_ventas[3][j]
    if suma > ventas:
        ventas = suma
        dia_nombre = j


print(f"Total de leche vendida: {leche_total}")
print(f"Total de yogurt vendido: {yogurt_total}")
print(f"Total de manteca vendida: {manteca_total}")
print(f"Total de chocolate vendido: {chocolate_total}")
print(
    f"El producto con mayor ventas es: {nombres[totales.index(max(totales))]}")

if dia_nombre == 0:
    print(f"El dia con mayor ventas es el lunes con {ventas}")

elif dia_nombre == 1:
    print(f"El dia con mayor ventas es el martes con {ventas}")

elif dia_nombre == 2:
    print(f"El dia con mayor ventas es el miercoles con {ventas}")

elif dia_nombre == 3:
    print(f"El dia con mayor ventas es el jueves con {ventas}")

elif dia_nombre == 4:
    print(f"El dia con mayor ventas es el viernes con {ventas}")

elif dia_nombre == 5:
    print(f"El dia con mayor ventas es el sabado con {ventas}")

elif dia_nombre == 6:
    print(f"El dia con mayor ventas es el domingo con {ventas}")
print("Ejercicio 10 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 11
print("Ejercicio 11")
estudiantes = ["Carlos", "María", "Juan", "Ana", "Luis",
               "Lucía", "Diego", "Sofía", "Pedro", "Miguel"]

buscar = input("Ingrese el estudiante a buscar: ").capitalize()
se_encontro = False
for estudiante in estudiantes:
    if buscar == estudiante:
        se_encontro = True
        posicion = estudiantes.index(estudiante) + 1
        break

if se_encontro:
    print(
        f"El estudiante {buscar} se encuentra en la lista en la posicion {posicion}")
else:
    print(f"El estudiante {buscar} no se encuentra en la lista")
print("Ejercicio 11 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 12
print("Ejercicio 12")
numeros = []
while len(numeros) < 8:
    numero = input("Ingrese un numero: ")
    while not numero.isdigit():
        numero = input("Ingrese un numero: ")
    numeros.append(int(numero))

print("Lista original:")
for i in numeros:
    print(i)

print("Lista con orden de menor a mayor:")
for i in sorted(numeros):
    print(i)

print("Lista con orden de mayor a menor:")
for i in sorted(numeros, reverse=True):
    print(i)
print("Ejercicio 12 finalizado")
print("-----------------------------------------------------------------------")
# Ejercicio 13
print("Ejercicio 13")
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
ordenado = sorted(puntajes, reverse=True)
print(f"Puntaje mas alto: {max(puntajes)}")
print(f"Puntaje mas bajo: {min(puntajes)}")
print("Lista ordenada de mayor a menor:")
for i in ordenado:
    print(i)

poscion = ordenado.index(990) + 1
print(f"El numero 990 se encuentra en la posición {poscion}")
print("Ejercicio 13 finalizado")
print("-----------------------------------------------------------------------")
input("Presione enter para salir...")
