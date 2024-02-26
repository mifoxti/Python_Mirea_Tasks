import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    val = perlin(x, y, 0.05)
    return val, val, val


def perlin(x, y, freq):
    cx = math.floor(x / freq) * freq
    fx = (x - cx) / freq

    cy = math.floor(y / freq) * freq
    fy = (y - cy) / freq

    p00 = noise(cx, cy)
    p01 = noise(cx + freq, cy)
    p10 = noise(cx, cy + freq)
    p11 = noise(cx + freq, cy + freq)

    return bilerp(p00, p01, p10, p11, func(fx), func(fy))


def lerp(a, b, t):
    return a + (b - a) * t


def bilerp(p00, p01, p10, p11, tx, ty):
    return lerp(lerp(p00, p01, tx), lerp(p10, p11, tx), ty)


def func(t):
    return ((t - 0.5) * 1.4 / (0.2 + abs(t - 0.5)) + 1) * 0.5


def noise(x, y):
    val = math.sin(x * 12.9898 + y * 78.233) * 43758.5453
    return val - math.floor(val)


main(shader)
