import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

# Палитра PICO-8
pico8_palette = [
    '#1D2B53', '#7E2553', '#008751', '#AB5236',
    '#5F574F', '#C2C3C7', '#FFF1E8', '#FF004D',
    '#FFA300', '#FFEC27', '#00E436', '#29ADFF',
    '#83769C', '#FF77A8', '#FFCCAA'
]

def generate_random_symmetric_sprite():
    # Создаем случайную половину спрайта размером 5x5 с использованием палитры PICO-8
    sprite_half = np.random.randint(0, len(pico8_palette), size=(5, 3), dtype=int)

    # Симметричное отражение по вертикали и горизонтали
    sprite = np.concatenate([sprite_half, np.fliplr(sprite_half)], axis=1)
    sprite = np.concatenate([sprite, np.flipud(sprite)], axis=0)

    return sprite

def generate_sprite_map(rows, cols, spacing):
    sprite_size = 5
    # Рассчитываем размеры карты спрайтов с учетом пустого пространства
    map_size = (rows * (sprite_size + spacing) - spacing, cols * (sprite_size + spacing) - spacing, 4)
    sprite_map = np.zeros(map_size, dtype=float)

    for i in range(rows):
        for j in range(cols):
            # Получаем случайный симметричный спрайт
            sprite = generate_random_symmetric_sprite()

            # Вычисляем симметричные цвета для каждого цвета в палитре PICO-8
            symmetric_colors = [to_rgba(pico8_palette[idx]) for idx in sprite.flatten()]
            symmetric_colors = [(*color[:3], 1 - color[3]) for color in symmetric_colors]

            # Конвертируем в массив NumPy
            symmetric_colors = np.array(symmetric_colors, dtype=float).reshape(5, 5, 4)

            # Рассчитываем координаты для вставки спрайта с учетом пустого пространства
            x_start = i * (sprite_size + spacing)
            x_end = x_start + sprite_size
            y_start = j * (sprite_size + spacing)
            y_end = y_start + sprite_size

            # Помещаем цветной спрайт в соответствующую позицию на карте
            sprite_map[x_start:x_end, y_start:y_end, :] = symmetric_colors

    return sprite_map

# Генерация карты спрайтов 3x3 с пустым пространством
sprite_map = generate_sprite_map(3, 3, 2)

# Вывод карты спрайтов с помощью imshow
plt.imshow(sprite_map)
plt.title('Sprite Map with Spacing')
plt.show()
