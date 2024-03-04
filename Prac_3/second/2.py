import numpy as np
import matplotlib.pyplot as plt

def generate_random_symmetric_sprite():
    # Создаем случайный спрайт размером 5x5
    sprite = np.random.randint(0, 2, size=(5, 5), dtype=int)

    # Зеркально копируем верхнюю половину спрайта в нижнюю половину
    sprite[3:5, :] = np.flipud(sprite[0:2, :])

    return sprite

def generate_sprite_map(rows, cols, spacing):
    sprite_size = 5
    # Рассчитываем размеры карты спрайтов с учетом пустого пространства
    map_size = (rows * (sprite_size + spacing) - spacing, cols * (sprite_size + spacing) - spacing)
    sprite_map = np.zeros(map_size, dtype=int)

    for i in range(rows):
        for j in range(cols):
            # Получаем случайный симметричный спрайт
            sprite = generate_random_symmetric_sprite()

            # Рассчитываем координаты для вставки спрайта с учетом пустого пространства
            x_start = i * (sprite_size + spacing)
            x_end = x_start + sprite_size
            y_start = j * (sprite_size + spacing)
            y_end = y_start + sprite_size

            # Помещаем спрайт в соответствующую позицию на карте
            sprite_map[x_start:x_end, y_start:y_end] = sprite

    return sprite_map

# Генерация карты спрайтов 3x3 с пустым пространством
sprite_map = generate_sprite_map(9, 15, 2)

# Вывод карты спрайтов с помощью imshow
plt.imshow(sprite_map, cmap='gray', interpolation='nearest')
plt.title('Sprite Map with Spacing')
plt.show()
