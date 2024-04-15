import graphviz
from collections import deque

# ������� �������� �� ������� � �������
def go(room):
    def func(state):
        return dict(state, room=room)
    return func

# ������� ������������ ������
def toggle_lever(state):
    return dict(state, lever=not state.get('lever', False))

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

# ������� �������� �������� ���������
def is_goal_state(state):
    '''
    ���������, �������� �� ��������� �������.
    '''
    return state['room'] == 'room2'

# ������� ��������� ������� �������
def get_current_room(state):
    '''
    ������ �������, � ������� ��������� �����.
    '''
    return state['room']

# ������� �������� ����������� ����� ����� ��� ��������� ���������� ����
def shortest_path_length(game_graph, start_state):
    '''
    ���������� ���������� ����� ����� ��� ��������� ���������� ����.

    ���������:
        game_graph (dict): ���� ���� ��������� ��������� ����.
        start_state (str): ��������� ��������� ����.

    ����������:
        int or None: ���������� ����� ����� ��� None, ���� ���� �� ����� ���� ���������.
    '''
    visited = set()  # ������ ��� ���������� ���������
    queue = deque([(start_state, 0)])  # ������� ��� BFS. ������ ������� - ���� (���������, ���������� �����)

    while queue:
        state, steps = queue.popleft()

        if is_goal_state(state):
            return steps

        if state not in visited:
            visited.add(state)
            # ��������� ��� �������� ��������� � ������� �� ��������� �� 1 ���
            for next_state_action, next_state_func in game_graph.get(get_current_room(state), {}).items():
                next_state = next_state_func(state)
                queue.append((next_state, steps + 1))

    return None  # ���� ������� ��������� �� ���� ����������

# ������ �������������
start_state = {'room': 'room0'}  # ��������� ��������� ����
shortest_path = shortest_path_length(game, start_state)
print(f'���������� ����� ����� ��� ��������� ���������� ����: {shortest_path}')
