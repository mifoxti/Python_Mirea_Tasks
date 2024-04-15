# -*- coding: utf-8 -*-

from collections import deque


def make_model(game, start_state):
    """
    Создает граф состояний игры.

    Args:
    - game (dict): Описание игры. Ключи - это комнаты, а значения - это словари с доступными действиями.
    - start_state (dict): Начальное состояние игры.

    Returns:
    - dict: Граф состояний игры, где ключи - это состояния игры, а значения - это словари действий и следующих состояний.
    """
    graph = {}  # Инициализируем пустой граф

    visited = set()  # Множество для отслеживания посещенных состояний
    queue = deque([start_state])  # Очередь для BFS

    while queue:
        current_state = queue.popleft()  # Извлекаем текущее состояние из очереди
        visited.add(tuple(current_state.items()))  # Добавляем состояние во множество посещенных

        # Получаем доступные действия для текущей комнаты
        actions = game.get(current_state['room'], {})

        # Добавляем текущее состояние в граф
        graph[tuple(current_state.items())] = {}

        for action, transition_func in actions.items():
            # Применяем функцию перехода к текущему состоянию
            next_state = transition_func(current_state)

            # Если следующее состояние еще не было посещено
            if tuple(next_state.items()) not in visited:
                graph[tuple(current_state.items())][action] = tuple(next_state.items())
                queue.append(next_state)  # Добавляем следующее состояние в очередь

    return graph


# Функция перехода в другую комнату
def go(room):
    def func(state):
        return dict(state, room=room)

    return func


# Описание игры
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

# Начальное состояние
START_STATE = dict(room='room0')


def is_goal_state(state):
    '''
    Проверяет, является ли состояние целевым.
    '''
    return state['room'] == 'room2'


def get_current_room(state):
    '''
    Возвращает текущую комнату, в которой находится игрок.
    '''
    return state['room']


def find_dead_ends(graph):
    """    Находит тупики в графе.    Args:    - graph (dict): Граф состояний игры.    Returns:    - list: Список тупиков.    """
    dead_ends = []

    for state, actions in graph.items():
        if len(actions) == 0:  # Условие добавлено для учета тупиковых состояний без выходящих связей
            dead_ends.append(state)

        if len(actions) == 1:
            next_state = list(actions.values())[0]
            if len(graph[next_state]) == 1:
                dead_ends.append(state)

    return dead_ends


# Создание модели игры
graph = make_model(game, START_STATE)
print("Graph of states of the game:", graph)

dead_ends = find_dead_ends(graph)
print("Dead end:", dead_ends)

import matplotlib.pyplot as plt
import networkx as nx

# Создание графа из словаря состояний игры
G = nx.DiGraph()

# Добавление узлов (состояний) в граф
for state, actions in graph.items():
    G.add_node(state)

# Добавление ребер (действий) в граф
for state, actions in graph.items():
    for action, next_state in actions.items():
        G.add_edge(state, next_state, action=action)

# Визуализация графа
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)  # Положения узлов на графе
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold',
        arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'action')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)
plt.title("Graph of States of the Game")
plt.show()

# Визуализация тупиков
plt.figure(figsize=(8, 6))
G_dead_ends = G.subgraph(dead_ends)  # Создание подграфа только с тупиками
nx.draw(G_dead_ends, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title("Dead Ends")
plt.show()
