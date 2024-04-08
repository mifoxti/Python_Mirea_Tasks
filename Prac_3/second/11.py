from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def load_image(image_path):
    return np.array(Image.open(image_path))

def draw_vertical_lines(ax, texture, heightmap, camera_x, camera_y, screen_width, view_depth, horizon):
    # Определяем размеры текстуры и карты высот
    texture_height, texture_width, _ = texture.shape
    heightmap_height, heightmap_width = heightmap.shape

    # Определяем границы обзора камеры
    view_left = camera_x - screen_width // 2
    view_right = view_left + screen_width

    # Определяем границы глубины обзора
    view_start = min(camera_y, view_depth)
    view_end = max(camera_y - view_depth, 0)

    # Рассчитываем координаты линий по x на экране
    line_xs = np.linspace(view_left, view_right, screen_width)

    # Начинаем рисование слоев
    for y in range(view_start, view_end, -1):
        for x in range(view_left, view_right):
            # Получаем значение высоты из карты высот
            height_value = heightmap[y, x]
            # Вычисляем масштабированную высоту текстуры с учетом z и горизонта
            texture_scale = (1 - (y - horizon) / view_depth)
            texture_height_scaled = int(texture_height * texture_scale)
            # Получаем цвет из текстуры
            texture_color = texture[min(texture_height_scaled - 1, int((height_value / heightmap_height) * (texture_height - 1))), int((x - view_left) / screen_width * (texture_width - 1))]
            # Рисуем вертикальную линию на изображении
            ax.plot([x, x], [y, y - 1], color=texture_color)

def visualize_texture_3d(texture_path, heightmap_path, camera_x, camera_y, screen_width, view_depth, horizon):
    # Загружаем текстуру и карту высот
    texture = load_image(texture_path)
    heightmap = load_image(heightmap_path)

    # Создаем новое изображение для визуализации в трехмерном пространстве
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Изобразим текстуру в трехмерном пространстве
    draw_vertical_lines(ax, texture, heightmap, camera_x, camera_y, screen_width, view_depth, horizon)

    # Настройка осей и масштаба
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(camera_x - screen_width // 2, camera_x + screen_width // 2)
    ax.set_ylim(camera_y - view_depth, camera_y)
    ax.set_zlim(0, view_depth)

    plt.show()

# Параметры камеры
camera_x = 500
camera_y = 900
screen_width = 64
view_depth = 400
horizon = 450  # Переменная, задающая положение горизонта

# Пути к текстуре и карте высот
texture_path = "texture.png"
heightmap_path = "heightmap.png"

# Визуализация текстуры в трехмерном пространстве
visualize_texture_3d(texture_path, heightmap_path, camera_x, camera_y, screen_width, view_depth, horizon)
