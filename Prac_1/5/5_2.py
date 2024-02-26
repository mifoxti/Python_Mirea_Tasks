import numpy as np
import matplotlib.pyplot as plt


# Функция SDF для круга
def circle(x, y, r):
    """
    Функция SDF для круга.

    Args:
      x: Координата x точки.
      y: Координата y точки.
      r: Радиус круга.

    Returns:
      SDF для круга.
    """
    # Вычисляем расстояние от точки до центра круга.
    d = ((x - 0.5) ** 2 + (y - 0.5) ** 2) ** 0.5 - r
    return d


# Функция SDF для квадрата
def box(x, y, size):
    """
    Функция SDF для квадрата.

    Args:
      x: Координата x точки.
      y: Координата y точки.
      size: Размер квадрата.

    Returns:
      SDF для квадрата.
    """
    # Вычисляем расстояния от точки до каждой стороны квадрата.
    d1 = abs(x - 0.5) - size / 2
    d2 = abs(y - 0.5) - size / 2
    # SDF для квадрата - это максимум из расстояний до каждой стороны.
    return max(d1, d2)


# Функция SDF, используемая в шейдере
def sdf_func(x, y):
    # Пример использования CSG: объединение круга и квадрата
    return min(circle(x, y, 0.4), box(x, y, 0.4))


# Визуализация SDF
x = np.linspace(0, 1, 500)
y = np.linspace(0, 1, 500)

d = np.zeros((len(x), len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        d[i, j] = sdf_func(x[i], y[j])

plt.imshow(d, cmap="gray")
plt.show()
