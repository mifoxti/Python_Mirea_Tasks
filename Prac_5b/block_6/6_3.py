import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def go(room):
    def func(state):
        return dict(state, room=room)
    return func

def make_model(game, start_state):
    graph = {}
    visited = set()
    queue = deque([start_state])

    while queue:
        current_state = queue.popleft()
        visited.add(tuple(current_state.items()))

        actions = game.get(current_state['room'], {})

        graph[tuple(current_state.items())] = {}

        for action, transition_func in actions.items():
            next_state = transition_func(current_state)

            if tuple(next_state.items()) not in visited:
                graph[tuple(current_state.items())][action] = tuple(next_state.items())
                queue.append(next_state)

    return graph

def toggle_lever(state):
    if state['room'] == 'room3':
        if state.get('lever', False):
            return dict(state, lever=False, room='room0')
        else:
            return dict(state, lever=True)
    elif state['room'] == 'room0' and state.get('lever', False):
        return dict(state, room='room3')

    return state

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

START_STATE = dict(room='room0')

def is_goal_state(state):
    return state['room'] == 'room2'

def get_current_room(state):
    return state['room']

def find_dead_ends(graph):
    dead_ends = []

    for state, actions in graph.items():
        if len(actions) == 1:
            next_state = list(actions.values())[0]
            if len(graph[next_state]) == 1:
                dead_ends.append(state)

    return dead_ends

graph = make_model(game, START_STATE)
print("Graph of states of the game:", graph)

dead_ends = find_dead_ends(graph)
print("Dead end:", dead_ends)

G = nx.DiGraph()

for state, actions in graph.items():
    G.add_node(state)

for state, actions in graph.items():
    for action, next_state in actions.items():
        G.add_edge(state, next_state, action=action)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'action')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)
plt.title("Graph of States of the Game")
plt.show()

plt.figure(figsize=(8, 6))
G_dead_ends = G.subgraph(dead_ends)
nx.draw(G_dead_ends, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
plt.title("Dead Ends")
plt.show()
