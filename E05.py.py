carm=0
estu=0
div=0
cam=0
cam=0

print("¿Cuantos caramelos tienes?")
carm=int(input())

print("¿Cuantos estudiantes son?")
estu=int(input())

div=carm//estu
cam=carm%estu

print("a cada estudiante le tocan", div, "caramelos")
print("te quedan", cam)