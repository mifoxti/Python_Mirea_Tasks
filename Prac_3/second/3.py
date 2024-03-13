import random

import numpy as np
import matplotlib.pyplot as plt
import random

def generate_colored_sprite():
    # Создаем случайные бинарные значения (0 или 1) для верхней левой части (левая половина) 5x5
    upper_left = np.random.randint(0, 2, size=(3, 3))

    # Задаем цвет для черных пикселей
    black_color = np.array([0, 0, 0])

    # Задаем два случайных цвета для цветной части
    color1 = np.random.rand(3)
    color2 = np.random.rand(3)

    # 3-канальный массив для хранения цвета (RGB)
    sprite = np.zeros((5, 5, 3))

    # Заполняем спрайт с вертикальной симметрией и двумя разными цветами
    for i in range(5):
        for j in range(5):
            if random.choice([True, False]):
                sprite[i, j] = color1
                sprite[i, 4 - j] = color1  # Симметричная часть
            else:
                sprite[i, j] = color2
                sprite[i, 4 - j] = color2  # Симметричная часть

            # Заполняем черные клетки
            if upper_left[i // 2, j // 2] == 0:
                sprite[i, j] = black_color
                sprite[i, 4 - j] = black_color  # Симметричная часть

    return sprite

def generate_sprite_map(rows, cols):
    # Размер каждого спрайта (5x5)
    sprite_size = 5

    # Размер каждой ячейки (включая пространство между спрайтами)
    cell_size = sprite_size + 1

    # Создаем пустую карту спрайтов
    sprite_map = np.zeros((rows * cell_size - 1, cols * cell_size - 1, 3))

    # Заполняем карту спрайтами
    for i in range(rows):
        for j in range(cols):
            sprite_map[i * cell_size: i * cell_size + sprite_size,
            j * cell_size: j * cell_size + sprite_size] = generate_colored_sprite()

    return sprite_map

# Задаем количество строк и столбцов
num_rows = 5
num_cols = 30


# Генерируем карту спрайтов
sprite_map = generate_sprite_map(num_rows, num_cols)

# Отображаем карту спрайтов с помощью imshow
plt.imshow(sprite_map, interpolation='nearest')
plt.title(f'Colored Symmetric Sprite Map ({num_rows}x{num_cols} sprites)')
plt.axis('off')  # Отключаем оси
plt.show()
