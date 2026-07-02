from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

imagen=Image.open('images.jpg')
imagen=np.array(imagen)

dimensiones=np.shape(imagen)
print(dimensiones)
grises=np.zeros((dimensiones[0], dimensiones[1]))

for i in range(dimensiones[0]):
    for j in range(dimensiones[1]):
        grises[i][j] = (int)(imagen[i][j][0]*0.2989+ imagen[i][j][1]*0.5870+imagen[i][j][2]*0.1140)
                             
plt.imshow(imagen)
plt.show()

plt.imshow(grises, cmap="gray")
plt.show()