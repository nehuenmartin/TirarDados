import random


# --- Usando solo randint --- #
while True:
    try: 
        cantidad_dados = int(input("¿Cuántos dados quieres tirar? "))
        for i in range(cantidad_dados):
            print(random.randint(1, 6) )

        repetir = input("¿Quieres tirar los dados otra vez? (s/n) ")
        if repetir == "s":
            continue
        else:
            break
    except ValueError:
        print("Debes ingresar un número")
        continue