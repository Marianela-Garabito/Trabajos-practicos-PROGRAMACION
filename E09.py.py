def calcular_factorial():
    while True:
        try:
            print('ingrese un numero positivo')
            num=int(input())
            
            if (num < 0):
                print("Error: el número debe ser positivo.")
            else:
                break
        except ValueError:
            print("Error: ingresá un número válido.")

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("El factorial de", num, "es:", factorial)

calcular_factorial()
