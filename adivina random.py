import random

numero =random.randint(1,100)
intentos=0

jugando = True

print("ADIVINA UN NUMERO DEL 1 AL 100")
while jugando:
    intentos=intentos+1
    if intentos<=7:
        eleccion = int(input("Dime un numero: "))

        if eleccion==numero:
            print("has acertado. has necesitado",intentos,"intentos.")
            jugando=False
        elif eleccion == -1:
            print("SALIDA.")
            print("el numero generado es", numero, ".")
        elif eleccion>numero:
            print("Demasiado alto. Llevas", intentos, "intentos")
            print("Puedes rendirte escribiendo el -1")
        elif eleccion <numero:
            print("Demasiado bajo. Llevas",intentos, "intentos.")
            print("Puedes rendirte escribiendo el -1")

    else:
        print("se te acaboron los intentos. Has perdido.")
        jugando= False





