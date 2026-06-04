M= [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

sum1=0
mult1=1
sum2=0
mult2=1
for i in range(4):
    for j in range(4):
        if(i==j):
            sum1= sum1 +M[i][j]
            mult1= mult1 *M[i][j]
        if(i+j ==3):
            sum2= sum2 +M[i][j]
            mult2= mult2 *M[i][j]
            
print("--PRIMERA DIAGONAL--")
print("Suma=",sum1)
print("Multiplicacion=",mult1)

print("--SEGUNDA DIAGONAL--")
print("Suma=",sum2)
print("Multiplicacion=",mult2)