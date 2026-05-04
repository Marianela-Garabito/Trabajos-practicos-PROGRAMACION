import datetime
dia=0
mes=0
año=0
naci=0
actual=0
edad=0

print('ingrese su fecha de nacimiento')
print("dia:")
dia=int(input())
print("mes:")
mes=int(input())
print("año:")
año=int(input())

actual= datetime.date.today()
naci=datetime.date(año,mes,dia)

print(actual)
print(naci)

edad=actual-naci
print("dias:",edad.days)
print("años:",años)



