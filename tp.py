def redondear(numero):

    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)

print(redondear(3.6)) 
print(redondear(3.5))  
print(redondear(3.2))  
