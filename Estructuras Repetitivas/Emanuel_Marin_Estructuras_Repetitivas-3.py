# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
operador = input("Ingrese un operador: ")

while operador.isalpha() == False:
    print("Error: El operador debe ser una letra.")
    operador = input("Ingrese un operador: ")

salir = False

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""
while salir == False:
    print("--------------------------------------------------------------------------------------------------------------")
    print(f"Hola {operador}, ¿qué desea hacer?")
    print("1) Reservar turno 2) Cancelar turno 3) Ver agenda del día 4) Ver resumen general 5) Salir")
    opcion = (input("Opción deseada: "))
    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = (input("Opción deseada: "))
    opcion = int(opcion)
    while opcion > 5 or opcion < 1:
        print("Error: ingrese un número entre 1 y 5.")
        opcion = (input("Opción deseada: "))
        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = (input("Opción deseada: "))
        opcion = int(opcion)
    if opcion == 1:
        print("--------------------------------------------------------------------------------------------------------------")
        print("Reservar turno")
        print("1) Lunes 2) Martes")
        dia = input("Elija el día deseado: ")
        while not dia.isdigit():
            print("Error: ingrese un número válido.")
            dia = input("Elija el día deseado: ")
        dia = int(dia)
        while dia > 2 or dia < 1:
            print("Error: ingrese un número entre 1 y 2.")
            dia = input("Elija el día deseado: ")
            while not dia.isdigit():
                print("Error: ingrese un número válido.")
                dia = input("Elija el día deseado: ")
            dia = int(dia)
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        while not nombre_paciente.isalpha():
            print("Error: ingrese un nombre válido.")
            nombre_paciente = input("Ingrese el nombre del paciente: ")

        if dia == 1:
            if lunes1 == nombre_paciente or lunes2 == nombre_paciente or lunes3 == nombre_paciente or lunes4 == nombre_paciente:
                print("El paciente ya tiene un turno reservado.")
            elif lunes1 == "":
                lunes1 = nombre_paciente
            elif lunes2 == "":
                lunes2 = nombre_paciente
            elif lunes3 == "":
                lunes3 = nombre_paciente
            elif lunes4 == "":
                lunes4 = nombre_paciente
            else:
                print("No hay turnos disponibles.")
        elif dia == 2:
            if martes1 == nombre_paciente or martes2 == nombre_paciente or martes3 == nombre_paciente:
                print("El paciente ya tiene un turno reservado.")
            elif martes1 == "":
                martes1 = nombre_paciente
            elif martes2 == "":
                martes2 = nombre_paciente
            elif martes3 == "":
                martes3 = nombre_paciente
            else:
                print("No hay turnos disponibles.")

    elif opcion == 2:
        print("--------------------------------------------------------------------------------------------------------------")
        print("Cancelar turno")
        print("1) Lunes 2) Martes")
        dia = input("Elija el día deseado: ")
        while not dia.isdigit():
            print("Error: ingrese un número válido.")
            dia = input("Elija el día deseado: ")
        dia = int(dia)
        while dia > 2 or dia < 1:
            print("Error: ingrese un número entre 1 y 2.")
            dia = input("Elija el día deseado: ")
            while not dia.isdigit():
                print("Error: ingrese un número válido.")
                dia = input("Elija el día deseado: ")
            dia = int(dia)
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        while not nombre_paciente.isalpha():
            print("Error: ingrese un nombre válido.")
            nombre_paciente = input("Ingrese el nombre del paciente: ")

        if dia == 1:
            if lunes1 == nombre_paciente:
                lunes1 = ""
                print("Turno cancelado.")
            elif lunes2 == nombre_paciente:
                lunes2 = ""
                print("Turno cancelado.")
            elif lunes3 == nombre_paciente:
                lunes3 = ""
                print("Turno cancelado.")
            elif lunes4 == nombre_paciente:
                lunes4 = ""
                print("Turno cancelado.")
            else:
                print("El paciente no tiene un turno reservado.")
        elif dia == 2:
            if martes1 == nombre_paciente:
                martes1 = ""
                print("Turno cancelado.")
            elif martes2 == nombre_paciente:
                martes2 = ""
                print("Turno cancelado.")
            elif martes3 == nombre_paciente:
                martes3 = ""
                print("Turno cancelado.")
            else:
                print("El paciente no tiene un turno reservado.")

    elif opcion == 3:
        print("--------------------------------------------------------------------------------------------------------------")
        print("Ver agenda del día")
        print("Lunes")
        if lunes1 == "":
            print("Turno 1: (libre)")
        else:
            print(f"Turno 1: {lunes1}")

        if lunes2 == "":
            print("Turno 2: (libre)")
        else:
            print(f"Turno 2: {lunes2}")

        if lunes3 == "":
            print("Turno 3: (libre)")
        else:
            print(f"Turno 3: {lunes3}")

        if lunes4 == "":
            print("Turno 4: (libre)")
        else:
            print(f"Turno 4: {lunes4}")
        print("Martes")
        if martes1 == "":
            print("Turno 1: (libre)")
        else:
            print(f"Turno 1: {martes1}")

        if martes2 == "":
            print("Turno 2: (libre)")
        else:
            print(f"Turno 2: {martes2}")

        if martes3 == "":
            print("Turno 3: (libre)")
        else:
            print(f"Turno 3: {martes3}")

    elif opcion == 4:
        print("--------------------------------------------------------------------------------------------------------------")
        print("Ver resumen general")
        count_lunes = 0
        count_martes = 0
        if lunes1 == "":
            count_lunes += 1
        if lunes2 == "":
            count_lunes += 1
        if lunes3 == "":
            count_lunes += 1
        if lunes4 == "":
            count_lunes += 1

        if martes1 == "":
            count_martes += 1
        if martes2 == "":
            count_martes += 1
        if martes3 == "":
            count_martes += 1

        ocupados_lunes = 4 - count_lunes
        ocupados_martes = 3 - count_martes
        print("Lunes")
        print(
            f"Turnos ocupados: {ocupados_lunes} Turnos disponibles: {count_lunes}")
        print("Martes")
        print(
            f"Turnos ocupados: {ocupados_martes} Turnos disponibles: {count_martes}")

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es lunes.")
        elif ocupados_lunes < ocupados_martes:
            print("El día con más turnos es martes.")
        else:
            print("Los días tienen la misma cantidad de turnos.")

    elif opcion == 5:
        salir = True

input("Presione enter para salir.")