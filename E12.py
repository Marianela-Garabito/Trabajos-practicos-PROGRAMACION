import random

estudiantes = ["juan", "Lucas", "maria", "Lia"]
orden = []

for i in range(len(estudiantes)):
    pos = random.randint(0, len(estudiantes)-1)

    while estudiantes[pos] in orden:
        pos = random.randint(0, len(estudiantes)-1)

    orden.append(estudiantes[pos])
    print(estudiantes[pos])
