din=0
mil=0
dos=0
rest=0
restf=0

print("ingrese la cantidad de dinero que desea extraer")
din=int(input())

mil=din//1000
rest=din%1000

dos=rest//200
restf=rest%200

print("billetes de 1000:", mil)
print("billetes de 200:", dos)
print("Monto que no se puede extraer:", restf)