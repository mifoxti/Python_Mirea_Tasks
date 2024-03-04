import re

# Структура данных для представления игрового мира
game_world = {
    "current_room": None,
    "rooms": {},
}

game_map = [
    {
        'название': 'Начало лабиринта',
        'метка': 'начало',
        'описание': 'Вы в начале лабиринта. Сможете ли из него выбраться?',
        'действия': [
            {'номер': 1, 'опция': 'Проход на запад.', 'метка_перехода': 'комната_2'}
        ]
    },
    {
        'название': 'Комната №2',
        'метка': 'комната_2',
        'описание': 'Вы находитесь в комнате №2.',
        'действия': [
            {'номер': 1, 'опция': 'Проход на запад.', 'метка_перехода': 'комната_3'},
            {'номер': 2, 'опция': 'Проход на восток.', 'метка_перехода': 'комната_1'}
        ]
    },
    {
        'название': 'Комната №3',
        'метка': 'комната_3',
        'описание': 'Вы находитесь в комнате №3.',
        'действия': [
            {'номер': 1, 'опция': 'Проход на север.', 'метка_перехода': 'комната_2'},
            {'номер': 2, 'опция': 'Проход на восток.', 'метка_перехода': 'конец'}
        ]
    },
    # Добавьте другие комнаты по мере необходимости
    {
        'название': 'Конец лабиринта',
        'метка': 'конец',
        'описание': 'Вы достигли конца лабиринта. Поздравляю!',
        'действия': []  # Конец игры, действий нет
    }
]

# Текущая комната, с которой начинается игра
current_room = game_map[0]

# Регулярные выражения для разбора ввода
start_regex = re.compile(r"Начало лабиринта")
room_regex = re.compile(r"Комната №(\d+)")
description_regex = re.compile(r"([^1-9].+)")
action_regex = re.compile(r"(\d+)\. (.+)")


# Функция для разбора строки с использованием регулярных выражений
# Функция для разбора строки с использованием регулярных выражений
def parse_line(line):
    if start_regex.match(line):
        game_world["current_room"] = None
    elif room_regex.match(line):
        match = room_regex.match(line)
        room_number = int(match.group(1))
        game_world["current_room"] = room_number
        game_world["rooms"][room_number] = {"description": "", "actions": {}}
    elif description_regex.match(line):
        match = description_regex.match(line)
        current_room = game_world["current_room"]
        game_world["rooms"][current_room]["description"] = match.group(1)
    elif action_regex.match(line):
        match = action_regex.match(line)
        action_number = int(match.group(1))
        action_text = match.group(2)
        current_room = game_world["current_room"]
        game_world["rooms"][current_room]["actions"][action_number] = action_text


# Пример описания игрового мира
game_description = """
Начало лабиринта

Вы в начале лабиринта. Сможете ли из него выбраться?

1. Проход на запад.

...

Комната №2

Вы находитесь в комнате №2.

1. Проход на запад.
2. Проход на восток.

> 1

...

Комната №3

Вы находитесь в комнате №3.

1. Проход на север.
2. Проход на восток.
"""

# Разбор описания игрового мира
for line in game_description.split("\n"):
    parse_line(line)


# Функция для вывода текущей комнаты и действий
def print_current_room():
    current_room = game_world["current_room"]
    if current_room is not None:
        room_info = game_world["rooms"][current_room]
        print(f"\n{room_info['description']}")
        for action_number, action_text in room_info["actions"].items():
            print(f"{action_number}. {action_text}")

# Интерпретатор игрового движка (продолжение)
while True:
    print_current_room()
    user_input = input("> ")

    if user_input.lower() == "exit":
        print("Выход из игры.")
        break

    try:
        selected_action = int(user_input)
        current_room_info = game_world["rooms"][game_world["current_room"]]
        if selected_action in current_room_info["actions"]:
            # Обновление текущей комнаты
            game_world["current_room"] += 1
            print("\nПереход в следующую комнату...")
        else:
            print("Неверное действие. Пожалуйста, выберите из предложенных вариантов.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")

# Завершение игры
print("Игра завершена.")