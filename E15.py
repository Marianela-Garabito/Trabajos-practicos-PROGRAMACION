from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


imagen = Image.open("descarga.jpg")
imagen = imagen.convert('L')
imagen =np.array(imagen)
dimensiones = np.shape(imagen)

filas, col=imagen.shape

for i in range(filas):
    for j in range(col // 2):
        aux = imagen[i][j]
        imagen[i][j] = imagen[i][col - 1 - j]
        imagen[i][col - 1 - j] = aux

#imagen volteada
plt.imshow(imagen, cmap="gray")
plt.show()

#imagen original
print("imagen original")
imagen = Image.open("descarga.jpg")
imagen = imagen.convert('L')
plt.imshow(imagen, cmap="gray")
plt.show()