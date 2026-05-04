random=0
aciertos=0
resp=''
si='si'
import random

print("bienvenido al juego!, ¿Estas listo?")
resp=input()

if(resp.strip().lower() != 'si'):
    print("adios")
else:
    print("!Comenzemos¡")
    print("Tienes 6 intentos")
    
    numero_secreto=random. randint(1, 20)
    
    for i in range(1, 7, 1):
        
        print("Ronda N°", i, "adivina el numero")
        intentos=int(input())
        
        if(intentos==numero_secreto):
            print("¡Correcto acertaste, felicidades!")
            break
            numero_secreto=random. randint(1, 20)
            aciertos+=1
        else:
            if(intentos>numero_secreto):
                print("demasiado alto")
            else:
                print("demasiado bajo")
        