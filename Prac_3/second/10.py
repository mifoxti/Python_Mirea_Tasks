from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def load_image(image_path):
    return np.array(Image.open(image_path))

def visualize_voxel_landscape(texture, heightmap, camera_x, camera_y, screen_width, view_depth):
    # Определяем размеры текстуры и карты высот
    texture_height, texture_width, _ = texture.shape
    heightmap_height, heightmap_width = heightmap.shape

    # Определяем границы обзора камеры
    view_left = camera_x - screen_width // 2
    view_right = view_left + screen_width

    # Определяем границы глубины обзора
    view_start = min(camera_y, view_depth)
    view_end = max(camera_y - view_depth, 0)

    # Создаем изображение для визуализации
    visualization = np.zeros((view_depth, screen_width, 3), dtype=np.uint8)

    # Начинаем сканирование слоев
    for y in range(view_start, view_end, -1):
        for x in range(view_left, view_right):
            # Получаем значение высоты из карты высот
            height_value = heightmap[y, x]
            # Получаем цвет из текстуры
            texture_color = texture[int((height_value / heightmap_height) * (texture_height - 1)), int((x - view_left) / screen_width * (texture_width - 1))]
            # Задаем цвет пикселя визуализации
            visualization[camera_y - y - 1, x - view_left] = texture_color

    # Создаем изображение для визуализации текстуры с заполненным треугольником, обозначающим область обзора камеры
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.imshow(texture)
    triangle_points = [[camera_x, view_start], [view_left, view_end], [view_right, view_end], [camera_x, view_start]]
    ax.plot([point[0] for point in triangle_points], [point[1] for point in triangle_points], color='r')
    ax.fill([point[0] for point in triangle_points], [point[1] for point in triangle_points], color='r', alpha=0.3)
    ax.set_title("Texture with Camera View")
    plt.show()

    # Визуализируем воксельный ландшафт
    plt.figure(figsize=(10, 5))
    plt.imshow(visualization)
    plt.title("Voxel Landscape Visualization")
    plt.show()

# Загружаем текстуру и карту высот
texture = load_image("texture.png")
heightmap = load_image("heightmap.png")

# Параметры камеры
camera_x = 500
camera_y = 900
screen_width = 64
view_depth = 400

# Визуализируем воксельный ландшафт
visualize_voxel_landscape(texture, heightmap, camera_x, camera_y, screen_width, view_depth)
