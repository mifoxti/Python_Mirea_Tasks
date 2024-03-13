from PIL import Image


def read_image(file_name) :
    image = Image.open(file_name).convert("RGB")
    rgb_values = list(image.getdata())

    colors = [tuple(rgb) for rgb in rgb_values]

    unique_colors = list(set(colors))

    return unique_colors


image_file = "image.jpg"
rgb_colors = read_image(image_file)
print(rgb_colors)