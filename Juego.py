from random import choice

def jugar_ahorcado():
    # Variables iniciales
    palabras_y_pistas = {
        "gato": ["Es un felino", "Dice miau", "Le gusta cazar ratones", "Tiene bigotes largos"],
        "perro": ["Es el mejor amigo del hombre", "Dice guau", "Es muy leal", "Le gusta jugar con la pelota"],
        "conejo": ["Le encanta la zanahoria", "Es un animal saltarín", "Tiene orejas largas", "Es muy suave y peludo"],
    }
    palabra_elegida, pistas = choice(list(palabras_y_pistas.items()))
    letras_falladas = []
    letras_acertadas = []
    intentos_restantes = 6
    aciertos = 0
    juego_terminado = False

    # Función para pedir una letra válida
    def pedir_letra():
        letra_elegida = ""
        es_valida = False
        abecedario = "abcdefghijklmnñopqrstuvwxyz"

        while not es_valida:
            letra_elegida = input("Introduce una letra: ").lower()
            if letra_elegida in abecedario and len(letra_elegida) == 1:
                es_valida = True
            else:
                print("No has elegido una letra correcta")

        return letra_elegida

    # Función para mostrar el tablero
    def mostrar_nuevo_tablero():
        lista_oculta = []
        for l in palabra_elegida:
            if l in letras_acertadas:
                lista_oculta.append(l)
            else:
                lista_oculta.append("-")
        print(" ".join(lista_oculta))

    # Función para verificar la letra elegida
    def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
        fin = False

        if letra_elegida in palabra_oculta and letra_elegida not in letras_acertadas:
            letras_acertadas.append(letra_elegida)
            coincidencias += palabra_oculta.count(letra_elegida)  # Suma todas las ocurrencias de la letra
        elif letra_elegida in palabra_oculta and letra_elegida in letras_acertadas:
            print("Ya has encontrado esa letra. Intenta con otra diferente")


        elif letra_elegida not in palabra_oculta:
            if letra_elegida not in letras_falladas:  # Evita duplicados en las letras falladas
                letras_falladas.append(letra_elegida)
                vidas -= 1  # Resta una vida solo en caso de fallo
                print(f"Pista: {choice(pistas)}")  # Muestra una pista aleatoria

        # Verifica condiciones de victoria o derrota
        if vidas == 0:
            fin = perder(palabra_oculta)
        elif coincidencias == len(palabra_oculta):  # Todas las letras de la palabra descubiertas
            fin = ganar(palabra_oculta)

        return vidas, fin, coincidencias

    # Función para mostrar el mensaje de derrota
    def perder(palabra):
        print("Te has quedado sin vidas")
        print(f"La palabra oculta era {palabra}")
        return True

    # Función para mostrar el mensaje de victoria
    def ganar(palabra_descubierta):
        mostrar_nuevo_tablero()
        print("¡¡¡Felicidades, has encontrado la palabra correcta!!!")
        return True

    # Inicio del juego
    print("Bienvenido al juego del AHORCADO.")
    print("Tienes 6 intentos para adivinar la palabra secreta.")
    print("¡Buena suerte!")

    while not juego_terminado:
        print('\n' + '*' * 20 + '\n')
        mostrar_nuevo_tablero()
        print('\n')
        print('Letras incorrectas: ' + '-'.join(letras_falladas))
        print(f'Vidas: {intentos_restantes}')
        print(f'Te faltan {len(palabra_elegida) - aciertos} letras por descubrir.')
        print('\n' + '*' * 20 + '\n')
        letra = pedir_letra()
        intentos_restantes, juego_terminado, aciertos = chequear_letra(
            letra, palabra_elegida, intentos_restantes, aciertos
        )


def iniciar_juego():
    jugar_otra_vez = True

    while jugar_otra_vez:
        jugar_ahorcado()  # Llama a la función del juego
        respuesta = input("¿Quieres jugar otra partida? (s/n): ").lower()
        if respuesta != "s":
            jugar_otra_vez = False
            print("Gracias por jugar. ¡Hasta la próxima!")

# Llama a la función principal
iniciar_juego()
