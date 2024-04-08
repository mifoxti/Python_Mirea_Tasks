import math
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# -----------------------------------------------------

def Init(width, height, colorfilename, heightfilename):
    global colorimg, colormap, heightimg, heightmap, pal, screen, screenmap
    colorimg = Image.open(colorfilename)
    colormap = colorimg.load()

    heightimg = Image.open(heightfilename)
    heightmap = heightimg.load()

    # Check if the image is in "P" (palette) mode
    if colorimg.mode == "P":
        # If it's in palette mode, get the palette data
        pal = colorimg.palette.getdata()[1]
    else:
        # If it's not in palette mode, create a default palette
        pal = [(i, i, i) for i in range(256)]

    screen = Image.new("RGB", (width, height))
    screenmap = screen.load()

# -----------------------------------------------------

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# -----------------------------------------------------

def DrawVerticalLine(x, ytop, ybottom, c):
    if (ytop >= ybottom): return
    if (ytop < 0): ytop = 0

    rgb = (pal[c*3+2]<< 16) | (pal[c*3+1] << 8) | pal[c*3+0]
    for j in range(math.floor(ytop), math.floor(ybottom)):
        screenmap[x, j] = rgb

# -----------------------------------------------------

def Store(image, idx):
    image.save("images/out%03d.gif" % idx, "GIF")

# -----------------------------------------------------

def Horline(p1, p2, offset, scale, horizon):
    n = 700
    dx = (p2.x - p1.x) / n
    dy = (p2.y - p1.y) / n
    for i in range(0, n):
        xi = math.floor(p1.x) & 1023
        yi = math.floor(p1.y) & 1023
        DrawVerticalLine(i, (heightmap[xi, yi]+offset)*scale+horizon, 511, colormap[xi, yi])
        p1.x += dx
        p1.y += dy

# -----------------------------------------------------

hidden = np.zeros(700)

def HorlineHidden(p1, p2, offset, scale, horizon):
    n = 700
    dx = (p2.x - p1.x) / n
    dy = (p2.y - p1.y) / n
    for i in range(0, n):
        xi = math.floor(p1.x) & 1023
        yi = math.floor(p1.y) & 1023
        heightonscreen = (heightmap[xi, yi] + offset) * scale + horizon
        DrawVerticalLine(i, heightonscreen, hidden[i], colormap[xi, yi])
        if heightonscreen < hidden[i]:
            hidden[i] = heightonscreen
        p1.x += dx
        p1.y += dy

# -----------------------------------------------------

def Rotate(p, phi):
    xtemp = p.x *  math.cos(phi) + p.y * math.sin(phi)
    ytemp = p.x * -math.sin(phi) + p.y * math.cos(phi)
    return Point(xtemp, ytemp)

# -----------------------------------------------------

def ClearAndDrawMaps():
    for j in range(0, 512):
        for i in range(0, 512):
            h = heightmap[i, j]
            c = colormap[i, j]  # Using colormap instead of pal for color
            screenmap[i,     j] = (pal[c][0]<< 16) | (pal[c][1] << 8) | pal[c][2]  # Accessing elements of pal correctly
            screenmap[i+512, j] = (h<<16) | (h << 8) | h

    for j in range(0, 512):
        for i in range(0, 700):
            screenmap[i+1024, j] = 0xffa366


# -----------------------------------------------------

def DrawBackToFront(p, phi, height, distance):
    ClearAndDrawMaps()
    for z in range(distance, 1, -2):
        pl = Point(-z, -z)
        pr = Point( z, -z)
        pl = Rotate(pl, phi)
        pr = Rotate(pr, phi)
        Horline(
            Point(670 + pl.x, 500 + pl.y),
            Point(670 + pr.x, 500 + pr.y),
            -height, -1./z*240., +120)

# -----------------------------------------------------

def DrawFrontToBack(p, phi, height, distance):
    ClearAndDrawMaps()
    dz = 1
    z = 5

    for i in range(0, 700):
        hidden[i] = 511

    while z < distance:
        pl = Point(-z, -z)
        pr = Point( z, -z)
        pl = Rotate(pl, phi)
        pr = Rotate(pr, phi)
        HorlineHidden(
            Point(670 + pl.x, 500 + pl.y),
            Point(670 + pr.x, 500 + pr.y),
            -height, -1./z*240., +100)
        z += dz

# -----------------------------------------------------

def InitCameraView(texture, x, y, screen_width, z):
    draw = ImageDraw.Draw(texture)
    draw.rectangle([(x - screen_width // 2, y - z), (x + screen_width // 2, y)], outline="red")

# -----------------------------------------------------

# Инициализация текстуры и карты высот
Init(512+512+700, 512, "texture.png", "heightmap.png")

# Инициализация скрытого массива
hidden = np.zeros(700)

# Инициализация индекса сохраненных кадров
idx = 0

# Отображение области обзора камеры на текстуре
InitCameraView(colorimg, 500, 900, 64, 400)

# Отображение ландшафта
DrawFrontToBack(Point(670, 500), 0, 120, 800)

# Сохранение изображения
Store(screen, idx)
