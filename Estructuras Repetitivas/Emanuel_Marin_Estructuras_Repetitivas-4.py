# Ejercicio 4 — "Escape Room: La Bóveda"
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

nombre = input("Ingrese el nombre del agente: ")

while nombre.isalpha() == False:
    print("Error: el nombre solo puede contener letras.")
    nombre = input("Ingrese el nombre del agente: ")

print(f"Bienvenido, agente {nombre}.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print("---------------------------------------------------------------------------------------")
    print("INFORMACIÓN DE LA BÓVEDA")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")
    print("---------------------------------------------------------------------------------------")

    print(f"¿Que vas a hacer, agente {nombre}?")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción: ")

    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 3:
        print("Error: debe ingresar una opción entre 1 y 3.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    if opcion == 1:

        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            print("La cerradura se trabó.")
            print("¡ALARMA ACTIVADA!")
            alarma = True

        else:

            if energia < 40:
                print("¡Riesgo de alarma!")
                numero = input("Ingrese un número del 1 al 3: ")

                while numero.isdigit() == False or int(numero) < 1 or int(numero) > 3:
                    print("Error: debe ingresar un número entre 1 y 3.")
                    numero = input("Ingrese un número del 1 al 3: ")

                numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("¡ALARMA ACTIVADA!")

            if alarma == False:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")


    elif opcion == 2:

        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        print("Hackeando panel...")

        for i in range(4):
            codigo_parcial += "A"
            print(f"Paso {i + 1}/4 - Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completado! Se abrió una cerradura.")


    elif opcion == 3:

        forzar_seguidas = 0

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma == True:
            energia -= 10

        print("Has descansado.")


    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡SISTEMA BLOQUEADO!")
        print("La alarma se activó y ya no hay tiempo suficiente.")
        break



print("------------------------------------------")

if cerraduras_abiertas == 3:
    print("¡VICTORIA!")
    print("Has abierto las 3 cerraduras.")

elif alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
    print("¡DERROTA!")
    print("La bóveda quedó bloqueada por la alarma.")

elif energia <= 0 or tiempo <= 0:
    print("¡DERROTA!")
    print("Te quedaste sin energía o sin tiempo.")

print("------------------------------------------")

input("Presione enter para salir.")

