import graphviz

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

def find_dead_ends(graph, start_state):
    '''
    Найти тупиковые узлы в графе состояний игры.

    Параметры:
        graph (dict): Граф всех возможных состояний игры.
        start_state (str): Начальное состояние игры.

    Возвращает:
        list: Список тупиковых узлов графа.
    '''
    dead_ends = []
    visited = set()

    def dfs(current_state):
        nonlocal dead_ends
        if current_state in visited:
            return
        visited.add(current_state)

        if current_state not in graph:
            dead_ends.append(current_state)
            return

        for next_state in graph[current_state].values():
            dfs(next_state)

    dfs(start_state)
    return dead_ends

def print_dot(graph, start_key):
    # Найти тупики
    dead_ends = find_dead_ends(graph, start_key)
    print('digraph {')
    graph_keys = list(graph.keys())
    for x in graph:
        n = graph_keys.index(x)
        if x == start_key:
            print(f'n{n} [style="filled",fillcolor="dodgerblue",shape="circle"]')
        elif x in dead_ends:
            print(f'n{n} [style="filled",fillcolor="red",shape="circle"]')
        else:
            print(f'n{n} [shape="circle"]')
    for x in graph:
        n1 = graph_keys.index(x)
        if graph[x] is not None:  # Проверка на существование связей
            for y in graph[x]:
                n2 = graph_keys.index(y)
                print(f'n{n1} -> n{n2}')
    print('}')

# Пример использования
game_graph = {
    0: {1: None, 2: None},
    1: {3: None},
    2: {4: None},
    3: {5: None},
    4: {5: None},
    5: {6: None},
    6: None
}

START_STATE = 0

print_dot(game_graph, START_STATE)

def save_dot_file(graph, filename):
    dot = graphviz.Digraph()
    for node in graph:
        dot.node(str(node))
        if graph[node] is not None:
            for neighbor in graph[node]:
                dot.edge(str(node), str(neighbor))
    dot.render(filename, format='png')

# Пример использования
game_graph = {
    0: {1: None, 2: None},
    1: {3: None},
    2: {4: None},
    3: {5: None},
    4: {5: None},
    5: {6: None},
    6: None
}

save_dot_file(game_graph, 'graph')
