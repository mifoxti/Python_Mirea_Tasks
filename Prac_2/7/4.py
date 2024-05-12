from flask import Flask, render_template

app = Flask(__name__)


class Room:
    def __init__(self, description, options):
        self.description = description
        self.options = options


def is_dead_end(room, visited, rooms):
    if room.options:
        for next_room_number in room.options.values():
            if next_room_number not in visited:
                visited.add(next_room_number)
                if is_dead_end(rooms[next_room_number], visited, rooms):
                    return True
                visited.remove(next_room_number)
    else:
        return True
    return False


@app.route('/')
def index():
    rooms = {
        1: Room("Вы в начале лабиринта.", {"1": 2}),
        2: Room("Вы находитесь в комнате №2.", {"1": 3, "2": 1}),
        3: Room("Вы находитесь в комнате №3.", {"1": 4, "2": 5}),
        4: Room("Это тупик. Нажмите 1, чтобы вернуться обратно в комнату №3.", {"1": 3}),
        5: Room("Вы находитесь в комнате №5.", {"1": 6, "2": 7}),
        6: Room("Поздравляем! Вы достигли финиша!", {}),
        7: Room("Это тупик. Нажмите 1, чтобы вернуться обратно в комнату №5.", {"1": 5})
    }

    current_room_number = 1  # Начинаем с комнаты 1
    current_room = rooms[current_room_number]

    if is_dead_end(current_room, set(), rooms):
        message = "В игровом мире есть тупики."
    else:
        message = "В игровом мире нет тупиков."

    return render_template('index.html', message=message, room=current_room)


@app.route('/room/<int:next_room_number>')
def move_to_room(next_room_number):
    rooms = {
        1: Room("Вы в начале лабиринта.", {"1": 2}),
        2: Room("Вы находитесь в комнате №2.", {"1": 3, "2": 1}),
        3: Room("Вы находитесь в комнате №3.", {"1": 4, "2": 5}),
        4: Room("Это тупик. Нажмите 1, чтобы вернуться обратно в комнату №3.", {"1": 3}),
        5: Room("Вы находитесь в комнате №5.", {"1": 6, "2": 7}),
        6: Room("Поздравляем! Вы достигли финиша!", {}),
        7: Room("Это тупик. Нажмите 1, чтобы вернуться обратно в комнату №5.", {"1": 5})
    }

    if next_room_number not in rooms:
        return "Invalid room number"

    current_room_number = next_room_number
    current_room = rooms[current_room_number]

    if is_dead_end(current_room, set(), rooms):
        message = "В игровом мире есть тупики."
    else:
        message = "В игровом мире нет тупиков."

    return render_template('index.html', message=message, room=current_room)


if __name__ == "__main__":
    app.rush(debug=True)
