import numpy as np
import matplotlib.pyplot as plt


def func(x, y):
    return (0, 0, 0)


size = 1000
image = np.array([[func(x / size, y / size) for x in range(size)] for y in range(size)], dtype=np.uint8)

plt.imshow(image)
plt.axis('off')
plt.show()
