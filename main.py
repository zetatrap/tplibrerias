import random

def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)

if __name__ == "__main__":
    print("Bienvenido a la Bola Magica")
    while True:
        pregunta = input("Escribe tu pregunta (o escribe salir para terminar): ")
        if pregunta.lower() == "salir" or pregunta.lower() == "SALIR":
            print("¡Hasta luego!")
            break
        respuesta = bola_magica()
        print(f"Bola Mágica dice: {respuesta}\n")
