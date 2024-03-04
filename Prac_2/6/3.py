import random

def generate_random_name():
    first_names = ['Иван', 'Алексей', 'Мария', 'Анна', 'Николай', 'Сергей', 'Елена', 'Андрей', 'Ольга', 'Дмитрий']
    last_names = ['Белов', 'Краснов', 'Сидорова', 'Петрова', 'Иванов', 'Кузнецов', 'Соколова', 'Попов', 'Новикова', 'Смирнов']
    middle_names = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И',  'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ю', 'Я']
    return random.choice(first_names) + ' ' + random.choice(middle_names) + '. ' + random.choice(last_names)

for _ in range(10):
    print(generate_random_name())

