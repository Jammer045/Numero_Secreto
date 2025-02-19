numero_incognita = 7  
intentos = 3

print("¡Bienvenido al juego de adivinanza!")
print(f"Tienes {intentos} intentos para adivinar un número entre 1 y 10.")


for i in range(intentos):
    numero_ingresado = int(input(f"Intento {i + 1}: Ingresa un número entre 1 y 10: "))
    if numero_ingresado == numero_incognita:
        print("¡Ganaste, has adivinado el número!")
        break
    elif numero_ingresado < numero_incognita:
        print("El número ingresado es menor, vuelve a intentarlo.")
    else:
        print("El número ingresado es mayor, vuelve a intentarlo.")
    if i == intentos - 1:
        print(f"Lo siento, has agotado tus {intentos} intentos. El número era {numero_incognita}.")