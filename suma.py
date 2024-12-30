
from tp import redondear

def suma(a, b):

    suma = a + b
    return redondear(suma)

if __name__ == "__main__":
    resultado = suma(2.3, 1.4)
    print(f" {resultado}") 
