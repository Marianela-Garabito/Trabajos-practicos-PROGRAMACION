def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9


print('ingrese la temperatura en Celsius:')
temp_c=int(input())
print('La temperatura en Fahrenheit es:',celsius_a_fahrenheit(temp_c))

print('ingrese la temperatura en Fahrenheit:')
temp_f=int(input())
print('La temperatura en Celsius es:',fahrenheit_a_celsius(temp_f))
