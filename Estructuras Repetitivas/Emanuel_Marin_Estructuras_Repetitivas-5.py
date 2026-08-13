# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while nombre.isalpha() == False:
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")



vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
ataque_enemigo = 12

turno_gladiador = True


print("--- INICIO DEL COMBATE ---")



while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador == True:

        print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

        print(f"Elige acción para {nombre}:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        
        if opcion == 1:

            if vida_enemigo < 20:
                daño = ataque_pesado * 1.5
                print("¡Golpe Crítico!")
            else:
                daño = float(ataque_pesado)

            vida_enemigo -= daño

            print(f"¡Atacaste al enemigo por {daño} puntos de daño!")

        elif opcion == 2:

            print("¡Inicias una ráfaga de golpes!")

            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te has curado 30 puntos de vida!")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False

    if vida_enemigo > 0 and vida_jugador > 0 and turno_gladiador == False:

        vida_jugador -= ataque_enemigo

        print(f"¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")

        turno_gladiador = True

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
    
input("Presione enter para salir.")