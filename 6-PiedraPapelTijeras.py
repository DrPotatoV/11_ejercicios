from random import randint
print("-------------------------------")

choice = ["Piedra", "papel", "Tijeras"]
def main():
    pc = choice[randint(0,2)]

    usuario = input("Escribe tu jugada: ").lower()
    print("La computadora ha seleccionado: " + pc)


    if usuario == pc:
        print("Empate")
    elif usuario == "piedra" and pc == "papel":
        print("La computadora gano")
    elif usuario == "piedra" and pc == "Tijeras":
        print("Tu ganaste")
    elif usuario == "papel" and pc == "piedra":
        print("Tu ganaste")
    elif usuario == "papel" and pc == "Tijeras":
        print("La computadora gano")
    elif usuario == "Tijeras" and pc == "piedra":
        print("La computadora gano")
    elif usuario == "Tijeras" and pc == "papel":
        print("Tu ganaste")
    main()
main()