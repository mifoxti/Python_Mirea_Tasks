import graphviz
from collections import deque

# Функция перехода из комнаты в комнату
def go(room):
    def func(state):
        return dict(state, room=room)
    return func

# Функция переключения рычага
def toggle_lever(state):
    return dict(state, lever=not state.get('lever', False))

# Структура игры. Комнаты и допустимые в них действия
game = {
    'room0': dict(
        left=go('room1'),
        up=go('room2'),
        right=go('room3')
    ),
    'room1': dict(
        up=go('room2'),
        right=go('room0')
    ),
    'room2': dict(),
    'room3': dict(
        up=go('room4'),
        right=go('room5'),
        lever=toggle_lever
    ),
    'room4': dict(
        down=go('room3'),
        right=go('room5')
    ),
    'room5': dict(
        up=go('room4'),
        left=go('room3')
    )
}

# Функция проверки целевого состояния
def is_goal_state(state):
    '''
    Проверить, является ли состояние целевым.
    '''
    return state['room'] == 'room2'

# Функция получения текущей комнаты
def get_current_room(state):
    '''
    Выдать комнату, в которой находится игрок.
    '''
    return state['room']

# Функция подсчета кратчайшего числа шагов для успешного завершения игры
def shortest_path_length(game_graph, start_state):
    '''
    Подсчитать кратчайшее число шагов для успешного завершения игры.

    Параметры:
        game_graph (dict): Граф всех возможных состояний игры.
        start_state (str): Начальное состояние игры.

    Возвращает:
        int or None: Кратчайшее число шагов или None, если игра не может быть завершена.
    '''
    visited = set()  # Хранит уже посещенные состояния
    queue = deque([(start_state, 0)])  # Очередь для BFS. Каждый элемент - пара (состояние, количество шагов)

    while queue:
        state, steps = queue.popleft()

        if is_goal_state(state):
            return steps

        if state not in visited:
            visited.add(state)
            # Добавляем все соседние состояния в очередь со смещением на 1 шаг
            for next_state_action, next_state_func in game_graph.get(get_current_room(state), {}).items():
                next_state = next_state_func(state)
                queue.append((next_state, steps + 1))

    return None  # Если целевое состояние не было достигнуто

# Пример использования
start_state = {'room': 'room0'}  # Начальное состояние игры
shortest_path = shortest_path_length(game, start_state)
print(f'Кратчайшее число шагов для успешного завершения игры: {shortest_path}')
