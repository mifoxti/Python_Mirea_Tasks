import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree


def voronoi_filter(image, num_points):
    height, width, _ = image.shape
    points = np.random.randint(0, min(height, width), size=(num_points, 2))

    result_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Создание кд-дерева из точек
    tree = cKDTree(points)

    for y in range(height):
        for x in range(width):
            # Находим индекс ближайшей точки с помощью кд-дерева
            min_index = tree.query((x, y), k=1)[1]
            result_image[y, x] = image[points[min_index][1], points[min_index][0]]

    return result_image


image = plt.imread("image.jpg")
num_points = 100
filtered_image = voronoi_filter(image, num_points)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Исходное изображение')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image)
plt.title('Результат фильтрации')
plt.axis('off')

plt.show()
