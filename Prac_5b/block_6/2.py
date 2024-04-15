# не работает


def find_dead_ends(game, start_state, is_goal_state):
    """
    Находит тупиковые узлы графа, из которых невозможно достичь цели.

    Args:
    - game (dict): Структура игры. Комнаты и допустимые в них действия.
    - start_state (dict): Стартовое состояние игры.
    - is_goal_state (function): Функция, которая проверяет, является ли состояние целевым.

    Returns:
    - list: Список тупиковых узлов графа.
    """
    graph = make_model(game, start_state)  # Создаем граф всех возможных состояний
    goal_state = tuple(filter(is_goal_state, graph))[0]  # Находим целевое состояние

    dead_ends = []  # Создаем пустой список для тупиковых узлов

    for state in graph:
        if state != goal_state:  # Пропускаем целевое состояние
            # Если из текущего состояния нет переходов, то это тупиковый узел
            if not graph[state]:
                dead_ends.append(state)

    return dead_ends

# Пример использования
dead_ends = find_dead_ends(game, START_STATE, is_goal_state)
print("Тупиковые узлы:", dead_ends)
