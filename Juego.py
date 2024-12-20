import random


def palabra_al_azar(lista):
    print("Bienvenido al juego del AHORCADO.")
    print("Tienes 6 intentos para adivinar la palabra secreta.")
    print("¡Buena suerte!")
    return random.choice(lista)


def iniciar_juego(palabra):
    # Convertimos la palabra oculta en una lista de caracteres (cada "_" es un lugar vacío)
    palabra_oculta = list("_" * len(palabra))
    intentos_restantes = 6
    letras_falladas = set()
    letras_acertadas = set()

    # Pistas según la palabra seleccionada
    pistas = {
        "gato": [
            "Es un animal",
            "Es un felino",
            "Es buena mascota para un egipcio"
        ],
        "perro": [
            "Es un animal",
            "Tiene colmillos",
            "Es amigo del hombre"
        ],
        "conejo": [
            "Es un animal",
            "Es vegetariano",
            "Es doméstico"
        ]
    }

    pista_index = 0  # Para seguir el índice de las pistas a mostrar

    while intentos_restantes > 0 and "_" in palabra_oculta:
        # Mostrar la palabra oculta
        print(f"\nPalabra: {''.join(palabra_oculta)}")  # Convertimos la lista de vuelta a string
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras falladas: {', '.join(letras_falladas)}")
        print(f"Letras acertadas: {', '.join(letras_acertadas)}")

        # Mostrar pistas cuando los intentos restantes son 3, 2 y 1
        if intentos_restantes == 3 and pista_index < len(pistas[palabra]):
            print(f"\nPista: {pistas[palabra][pista_index]}")
            pista_index += 1
        elif intentos_restantes == 2 and pista_index < len(pistas[palabra]):
            print(f"\nPista: {pistas[palabra][pista_index]}")
            pista_index += 1
        elif intentos_restantes == 1 and pista_index < len(pistas[palabra]):
            print(f"\nPista: {pistas[palabra][pista_index]}")
            pista_index += 1

        # Pedir al jugador que introduzca una letra
        jugador = input("Introduce una letra: ").lower()

        # Validaciones
        if len(jugador) != 1 or not jugador.isalpha():
            print("Por favor, introduce solo una letra.")
            continue

        if jugador in letras_falladas or jugador in letras_acertadas:
            print("Ya intentaste esa letra. Prueba con otra.")
            continue

        if jugador in palabra:
            letras_acertadas.add(jugador)
            # Reemplazar los "_" por la letra acertada
            for i, letra in enumerate(palabra):
                if letra == jugador:
                    palabra_oculta[i] = jugador  # Cambiar la letra en la lista
            print(f"Correcto. La letra {jugador} está en la palabra.")
        else:
            intentos_restantes -= 1
            letras_falladas.add(jugador)
            print(f"Incorrecto. La letra {jugador} no está en la palabra.")

    if "_" not in palabra_oculta:
        print(f"\n¡Felicidades! Has adivinado la palabra: {''.join(palabra_oculta)}")
    else:
        print(f"\nSe te han acabado los intentos. La palabra era: {palabra}")


# Lista de palabras para el juego
lista_final = ["gato", "perro", "conejo"]
palabra = palabra_al_azar(lista_final)

# Iniciar el juego
iniciar_juego(palabra)
