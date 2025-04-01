from random import choice

def jugar_ahorcado():
  
    palabras_y_pistas = {
        "gato": ["Es un felino", "Dice miau", "Le gusta cazar ratones", "Tiene bigotes largos"],
        "perro": ["Es el mejor amigo del hombre", "Dice guau", " Es muy leal", "Le gusta jugar con la pelota"],
        "conejo": ["Le encanta la zanahoria", "Es un animal saltarín", "Tiene orejas largas", "Es muy suave y peludo"],
    }

    palabra_elegida, pistas = choice(list(palabras_y_pistas.items()))  # 🎲 Selección aleatoria
    letras_falladas = []
    letras_acertadas = []
    intentos_restantes = 6
    aciertos = 0
    juego_terminado = False

    def pedir_letra():
        letra_elegida = ""
        abecedario = "abcdefghijklmnñopqrstuvwxyz"

        while True:
            letra_elegida = input("🎤 Introduce una letra: ").lower()
            if letra_elegida in abecedario and len(letra_elegida) == 1:
                return letra_elegida
            print("⚠️ No has elegido una letra válida.")

    def mostrar_nuevo_tablero():
        lista_oculta = [l if l in letras_acertadas else "🔲" for l in palabra_elegida]
        print("📝 Palabra: " + " ".join(lista_oculta))

    def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
        fin = False

        if letra_elegida in palabra_oculta and letra_elegida not in letras_acertadas:
            letras_acertadas.append(letra_elegida)
            coincidencias += palabra_oculta.count(letra_elegida) 
        elif letra_elegida in palabra_oculta and letra_elegida in letras_acertadas:
            print("🔄 Ya encontraste esa letra, prueba con otra.")
        else:
            if letra_elegida not in letras_falladas:
                letras_falladas.append(letra_elegida)
                vidas -= 1
                print(f"❌ Letra incorrecta. Pista: {choice(pistas)}") 

        if vidas == 0:
            fin = perder(palabra_oculta)
        elif coincidencias == len(palabra_oculta):
            fin = ganar(palabra_oculta)

        return vidas, fin, coincidencias

    def perder(palabra):
        print("💀 Te has quedado sin vidas.")
        print(f"⚠️ La palabra oculta era: {palabra.upper()}")
        return True

    def ganar(palabra_descubierta):
        mostrar_nuevo_tablero()
        print("🎉 ¡¡¡FELICIDADES!!! Has encontrado la palabra correcta. 🏆")
        return True

    print("🎮 ¡Bienvenido al juego del AHORCADO! 🔠")
    print("🔢 Tienes 6 intentos para adivinar la palabra secreta. ¡Buena suerte! 🍀")

    while not juego_terminado:
        print("\n" + "⭐" * 30 + "\n")
        mostrar_nuevo_tablero()
        print(f"❌ Letras incorrectas: {', '.join(letras_falladas) if letras_falladas else 'Ninguna'}")
        print(f"❤️ Vidas restantes: {intentos_restantes} {'💀' * (6 - intentos_restantes)}")
        print(f"🔎 Te faltan {len(palabra_elegida) - aciertos} letras por descubrir.")
        print("\n" + "⭐" * 30 + "\n")

        letra = pedir_letra()
        intentos_restantes, juego_terminado, aciertos = chequear_letra(
            letra, palabra_elegida, intentos_restantes, aciertos
        )

def iniciar_juego():
    jugar_otra_vez = True

    while jugar_otra_vez:
        jugar_ahorcado()
        respuesta = input("\n🔁 ¿Quieres jugar otra partida? (s/n): ").strip().lower()
        if respuesta != "s":
            jugar_otra_vez = False
            print("👋 ¡Gracias por jugar! Hasta la próxima. 🚀")


iniciar_juego()
