import random

def generar_numero_par():
    return random.choice([2, 4, 6, 8, 10])

if __name__ == "__main__":
    while True:
        numero_par = generar_numero_par()
        print(f" {numero_par}")
