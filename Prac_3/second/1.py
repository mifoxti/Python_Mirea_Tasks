import numpy as np
import matplotlib.pyplot as plt

def generate_random_symmetric_sprite():
    # Создаем случайный спрайт размером 5x5
    sprite = np.random.randint(0, 2, size=(5, 5), dtype=int)

    # Зеркально копируем верхнюю половину спрайта в нижнюю половину
    sprite[3:5, :] = np.flipud(sprite[0:2, :])

    return sprite

# Генерация случайного спрайта
random_sprite = generate_random_symmetric_sprite()

# Вывод спрайта с помощью imshow
plt.imshow(random_sprite, cmap='gray', interpolation='nearest')
plt.title('Random Symmetric Sprite')
plt.show()
