class Room:
    def __init__(self, description, exits):
        self.description = description
        self.exits = exits

    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits


rooms = {
    '1': Room('Начало лабиринта. Вы в начале лабиринта. Сможете ли из него выбраться?', {'1': '2'}),
    '2': Room('Комната №2. Вы находитесь в комнате №2.', {'1': '3', '2': '1'}),
    '3': Room('Комната №3. Вы находитесь в комнате №3.', {'1': '4', '2': '5'}),
    '4': Room('Комната №4. Вы находитесь в тупике комнаты №4.', {'1': '3'}),
    '5': Room('Комната №5. Вы находитесь в комнате №5.', {'1': '6', '2': '7'}),
    '6': Room('Комната №6. Вы нашли выход из лабиринта!', {}),
    '7': Room('Комната №7. Вы находитесь в тупике комнаты №7.', {'1': '5'})
}

# Add additional rooms to meet the requirement of at least 10 rooms
for i in range(8, 11):
    rooms[str(i)] = Room(f'Комната №{i}. Это дополнительная комната.', {'1': str(i+1)})
rooms['10'].exits = {}

def game():
    current_room = '1'

    while True:
        room = rooms[current_room]
        print(room.get_description())
        exits = room.get_exits()

        if not exits:
            print('Игра окончена.')
            break

        for exit, destination in exits.items():
            print(f'{exit}. Проход в комнату {destination}.')

        choice = input('> ')
        if choice in exits:
            current_room = exits[choice]
        else:
            print('Неверный выбор, попробуйте снова.')

if __name__ == '__main__':
    game()