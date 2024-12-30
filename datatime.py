from datetime import datetime

def mostrar():
    ahora = datetime.now()
    fecha_y_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Fecha y hora actuales: {fecha_y_hora}")

if __name__ == "__main__":
    mostrar()



