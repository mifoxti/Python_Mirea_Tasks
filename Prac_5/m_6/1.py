# -*- coding: utf-8 -*-

from collections import deque


def make_model(game, start_state):
    """
    Создает граф всех возможных состояний игры.

    Args:
    - game (dict): Структура игры. Комнаты и допустимые в них действия.
    - start_state (dict): Стартовое состояние игры.

    Returns:
    - dict: Граф всех возможных состояний игры, где ключами являются состояния,
            а значениями - набор возможных следующих состояний.
    """
    graph = {}  # Создаем пустой граф

    visited = set()  # Множество для отслеживания посещенных состояний
    queue = deque([start_state])  # Очередь для обхода в ширину

    while queue:
        current_state = queue.popleft()  # Берем первое состояние из очереди
        visited.add(tuple(current_state.items()))  # Добавляем текущее состояние в посещенные

        # Получаем доступные действия для текущей комнаты
        actions = game.get(current_state['room'], {})

        # Добавляем текущее состояние в граф
        graph[tuple(current_state.items())] = {}

        for action, transition_func in actions.items():
            # Применяем действие к текущему состоянию
            next_state = transition_func(current_state)

            # Добавляем переход в граф, если состояние еще не посещено
            if tuple(next_state.items()) not in visited:
                graph[tuple(current_state.items())][action] = tuple(next_state.items())
                queue.append(next_state)  # Добавляем следующее состояние в очередь

    return graph


# Функция перехода из комнаты в комнату
def go(room):
    def func(state):
        return dict(state, room=room)

    return func


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
    'room2': dict(
    ),
    'room3': dict(
        up=go('room4'),
        right=go('room5')
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

# Стартовое состояние
START_STATE = dict(room='room0')


def is_goal_state(state):
    '''
    Проверить, является ли состояние целевым.
    '''
    return state['room'] == 'room2'


def get_current_room(state):
    '''
    Выдать комнату, в которой находится игрок.
    '''
    return state['room']


# Пример использования
graph = make_model(game, START_STATE)
print(graph)
