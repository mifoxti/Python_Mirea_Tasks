import numpy as np
from PIL import Image, ImageDraw

# Функция val_noise, генерирующая шум Перлина
def val_noise(x, y, octaves=6, persistence=0.5):
    total = 0
    for i in range(octaves):
        freq = 2**i
        amp = persistence**i
        total += amp * np.random.rand(x, y) / freq
    return total

# Функция для генерации "облачных" точек
def generate_cloud_points(width, height, num_points, min_size, max_size):
    points = []
    for _ in range(num_points):
        size = np.random.randint(min_size, max_size)
        x = np.random.randint(0, width - size)
        y = np.random.randint(0, height - size)
        points.append((x, y, size))
    return points

# Параметры
width = 512
height = 512
octaves = 6
persistence = 0.5

# Генерация fBm
fbm = val_noise(width, height, octaves, persistence)

# Добавление случайных вариаций
fbm += np.random.rand(width, height) * 0.1

# Добавление эффекта освещения
light_dir = np.array([1, 0.5])
light_intensity = 0.5

# **Вариант 1: Вычисление освещения внутри цикла val_noise**
for i in range(width):
    for j in range(height):
        light_effect = light_dir[0] * i / width + light_dir[1] * j / height * light_intensity
        fbm[i, j] += light_effect

# **Вариант 2: Вычисление освещения отдельно**
# light_effect = np.outer(np.arange(width) / width, light_dir[0]) + np.outer(np.arange(height) / height, light_dir[1]) * light_intensity
# fbm += light_effect

# **Исправление цвета:**

# 1. Преобразование fbm к диапазону [0, 1]
fbm = (fbm - fbm.min()) / (fbm.max() - fbm.min())

# 2. Определение цвета неба и земли
sky_color = np.array([0.5, 0.7, 1])
ground_color = np.array([0.3, 0.5, 0.7])

# 3. Решейпинг sky_color и ground_color
sky_color_reshaped = sky_color.reshape((1, 1, 3))
ground_color_reshaped = ground_color.reshape((1, 1, 3))

# 4. Расчет градиента цвета
color_gradient = (sky_color_reshaped - ground_color_reshaped)

# 5. Применение градиента к fbm с вещанием
fbm = fbm[..., None] * color_gradient + ground_color_reshaped

# **Генерация "облачных" точек:**

# Параметры облаков
num_points = 500
min_size = 10
max_size = 50

# Генерация "облачных" точек
cloud_points = generate_cloud_points(width, height, num_points, min_size, max_size)

# Преобразование в изображение
image = Image.fromarray((fbm * 255).astype(np.uint8))

# Отрисовка точек
draw = ImageDraw.Draw(image)
for point in cloud_points:
    x, y, size = point
    draw.ellipse((x, y, x + size, y + size), fill="white")

# Отображение изображения
image.show()

# Сохранение изображения
image.save("clouds_modified_fixed4.png")
