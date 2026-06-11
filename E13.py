mensaje= ""
desp= 0

def cifrado_cesar(mensaje, desplazamiento):
    resultado=''
    
    for letra in (mensaje):
        LNueva= chr((ord(letra) - ord('a') + desplazamiento)% 26 + ord ('a'))
        resultado += LNueva
        
    return resultado

print('ingrese el mensaje:')
mensaje=input()
print('ingrese el desplazamiento:')
desp=int(input())

print(cifrado_cesar(mensaje, desp))