import tkinter as tk
import math

def lerp_color(color1, color2, t):
    # Линейная интерполяция между двумя цветами
    r = int((1 - t) * color1[0] + t * color2[0])
    g = int((1 - t) * color1[1] + t * color2[1])
    b = int((1 - t) * color1[2] + t * color2[2])
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def circle_sdf(x, y, center_x, center_y, radius):
    # Уравнение окружности в SDF форме
    return math.sqrt((x - center_x)**2 + (y - center_y)**2) - radius

def shader(x, y):
    d = circle_sdf(x, y, 0.5, 0.5, 0.45)
    is_inside = d < 0  # Изменено условие
    if is_inside:
        gradient_value = min(1, max(0, abs(d) * 3))  # Ограничиваем значение от 0 до 1
        color = lerp_color((0, 0, 0), (0, 255, 0), gradient_value)
    else:
        # Градиент от красного к желтому только в угловых областях
        gradient_value = min(1, max(0, (math.sqrt((x - 0.5)**2 + (y - 0.5)**2) - 0.45) * 3))
        color = lerp_color((255, 0, 0), (255, 255, 0), gradient_value)

    return is_inside, color, 0

def draw_circle(canvas, width, height):
    for i in range(width):
        for j in range(height):
            _, color, _ = shader(i / width, j / height)
            canvas.create_rectangle(i, j, i + 1, j + 1, fill=color, outline="")

def main():
    width, height = 300, 300

    root = tk.Tk()
    root.title("SDF Circle Gradient with Tkinter")

    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    draw_circle(canvas, width, height)

    root.mainloop()

if __name__ == "__main__":
    main()
