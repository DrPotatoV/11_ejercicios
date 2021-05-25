import random

numero = random.randrange(1,50)
usuario = int (input("Adivina el número secreto entre el 1 al 50: "))
vidas = 0

while usuario != numero:
    if usuario < numero:
        print("El numero que buscas no es este")
        usuario = int (input("\nAdivina el número entre el 1 al 50: "))
        vidas = vidas + 1
    elif usuario == "0":
            exit()
    else:
        print("Necesitas poner un número dentro del limite. Prueba de nuevo")
        usuario = int (input("\nAdivina el número entre el 1 al 7: "))
        vidas = vidas + 1

print("Felicidades, tienes el número correcto")
print("Probaste en " + str(vidas) + " intentos")