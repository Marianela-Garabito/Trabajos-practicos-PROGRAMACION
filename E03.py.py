num=0
resp=0
Binario=1
Hexadecimal=2
Decimal=3
ASCCII=4


print("¿en que sistema va a ingresar el numero?")
print("1-Binario")
print("2-Hexadecimal")
print("3-Decimal")
print("4-ASCCII")

resp=int(input())
print("ingrese el numero para convertir")
num=input()
    
if(resp==1):
    decimal= int(num, 2)
elif(resp==2):
    decimal= int(num, 16)
elif(resp==3):
    decimal= int(num, 10)
elif(resp==4):
    decimal=chr(num)
else:
    print("opcion no valida")
    
print("decimal:",decimal)
print("hexadecimal:",format(decimal,"x"))
print("binario:",format(decimal,"b"))
print("ASCII:", chr(decimal)) 
