# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
usuario_correcto = "alumno"
clave_correcta = "python123"
count = 1
print(f"Intento 1/3")
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if usuario != usuario_correcto or clave != clave_correcta:
    print("Error: credenciales inválidas.")

while count < 3:
    count += 1
    if count != 1:
        print(f"Intento {count}/3")

    if usuario == usuario_correcto and clave == clave_correcta:
        autorizado = True
        print("Acceso permitido.")
        break

    if count <= 3:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        if count != 1 and (usuario != usuario_correcto or clave != clave_correcta):
            print("Error: credenciales inválidas.")
        elif usuario == usuario_correcto and clave == clave_correcta:
                autorizado = True
                print("Acceso permitido.")
                break
if count == 3 and (usuario != usuario_correcto or clave != clave_correcta):
    print("Cuenta bloqueada")


if autorizado:
    salir = False
    while salir == False:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = (input("Opción deseada: "))
        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = (input("Opción deseada: "))
        opcion = int(opcion)
        while opcion > 4 or opcion < 1:
            print("Error: ingrese un número entre 1 y 4.")
            opcion = (input("Opción deseada: "))
            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = (input("Opción deseada: "))
            opcion = int(opcion)
        if opcion == 1:
            print("--------------------------------------------------------------------------------------------------------------")
            print("Estado")
            print("Inscripto")
        elif opcion == 2:
            print("--------------------------------------------------------------------------------------------------------------")
            print("Cambio de clave")
            nueva_clave = input("Ingrese su nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Ingrese su nueva clave: ")
            confirmar_nueva_clave = input("Confirme su nueva clave: ")
            while confirmar_nueva_clave != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmar_nueva_clave = input("Confirme su nueva clave: ")
            confirmar = input(f"¿Está seguro que desea cambiar su clave actual \"{clave_correcta}\" por \"{nueva_clave}\"? (S/N): ").upper()
            while confirmar != "S" and confirmar != "N":
                print("Error: ingrese S o N.")
                confirmar = input(f"¿Está seguro que desea cambiar su clave actual \"{clave_correcta}\" por \"{nueva_clave}\"? (S/N): ").upper()
            if confirmar == "S":
                print("Clave cambiada con éxito.")
                clave_correcta = nueva_clave
            else:
                print(f"Se mantuvo la contraseña \"{clave_correcta}\"")
            
        elif opcion == 3:
            print("--------------------------------------------------------------------------------------------------------------")
            print("Mensaje")
            print("¡Vamos! Tenés alma, cuerpo y espíritu, ¿qué tan difícil puede ser una carrera?")
        elif opcion == 4:
            salir = True
        

input("Presione enter para salir.")