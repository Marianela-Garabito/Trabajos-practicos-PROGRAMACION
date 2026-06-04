import math

print('CALCULADORA DE AREA Y VOLUMEN(circulo y cilindro)')

def area_circ(radio):
    area= math.pi * (radio**2)
    return(area)
    
print('ingrese el radio del circulo')
radio=int(input())
area=area_circ(radio)

print('el area del circulo es',area)


def vol_cilindro(radio, altura):
    volumen = area_circ(radio) * altura
    return volumen

print('ingrese la altura del cilindro')
altura=int(input())
volumen=vol_cilindro(radio, altura)

print('el volumen del cilindro es:', volumen)
