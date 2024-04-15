from collections import deque


def make_model(game, start_state):
    """
    ������� ���� ���� ��������� ��������� ����.

    Args:
    - game (dict): ��������� ����. ������� � ���������� � ��� ��������.
    - start_state (dict): ��������� ��������� ����.

    Returns:
    - dict: ���� ���� ��������� ��������� ����, ��� ������� �������� ���������,
            � ���������� - ����� ��������� ��������� ���������.
    """
    graph = {}  # ������� ������ ����

    visited = set()  # ��������� ��� ������������ ���������� ���������
    queue = deque([start_state])  # ������� ��� ������ � ������

    while queue:
        current_state = queue.popleft()  # ����� ������ ��������� �� �������
        visited.add(tuple(current_state.items()))  # ��������� ������� ��������� � ����������

        # �������� ��������� �������� ��� ������� �������
        actions = game.get(current_state['room'], {})

        # ��������� ������� ��������� � ����
        graph[tuple(current_state.items())] = {}

        for action, transition_func in actions.items():
            # ��������� �������� � �������� ���������
            next_state = transition_func(current_state)

            # ��������� ������� � ����, ���� ��������� ��� �� ��������
            if tuple(next_state.items()) not in visited:
                graph[tuple(current_state.items())][action] = tuple(next_state.items())
                queue.append(next_state)  # ��������� ��������� ��������� � �������

    return graph


# ������� �������� �� ������� � �������
def go(room):
    def func(state):
        return dict(state, room=room)

    return func


# ��������� ����. ������� � ���������� � ��� ��������
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

# ��������� ���������
START_STATE = dict(room='room0')


def is_goal_state(state):
    '''
    ���������, �������� �� ��������� �������.
    '''
    return state['room'] == 'room2'


def get_current_room(state):
    '''
    ������ �������, � ������� ��������� �����.
    '''
    return state['room']


# ������ �������������
graph = make_model(game, START_STATE)
print(graph)
