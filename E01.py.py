nom=''
naci=0
año=0
edad=0

print("¿Cual es tu nombre?")
nom=input()

print("hola" ,nom,"!")
print("¿En que año naciste?")
naci=int(input())
print("¿En que año estamos?")
año=int(input())

edad=año-naci

print("tienes", edad)