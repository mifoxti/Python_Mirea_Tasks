class Option:
    def __init__(self, next_node, token):
        self.next_node = next_node
        self.token = token


class Node:
    def __init__(self, val_data, options, index):
        self.value = val_data
        self.options = options
        self.index = index


# Создание узлов
nodes = [
    Node(None,
         [
             Option(
                 Node(13, [], -1),
                 2015
             ),
             Option(
                 Node(12, [], -1),
                 1991
             ),
             Option(
                 Node(None, [
                     Option(
                         Node(None, [
                             Option(Node(7, [], -1), 1976),
                             Option(Node(None, [
                                 Option(Node(8, [], -1), 2017),
                                 Option(Node(9, [], -1), 1980),
                                 Option(Node(10, [], -1), 2019)
                             ], 1), 1975),
                             Option(Node(11, [], -1), 1971)
                         ], 0), 2015),
                     Option(Node(None, [
                         Option(Node(None, [
                             Option(Node(6, [], -1), 1971),
                             Option(Node(5, [], -1), 1975),
                             Option(Node(4, [], -1), 1976)
                         ], 0), 2019),
                         Option(Node(3, [], -1), 1980),
                         Option(Node(None, [
                             Option(Node(0, [], -1), 1976),
                             Option(Node(1, [], -1), 1975),
                             Option(Node(2, [], -1), 1971)
                         ], 0), 2017)
                     ], 1), 1981)
                 ], 3), 1986)], 2)]


def get_option_for_current_token(options, token):
    for option in options:
        if token == option.token:
            return option


def process_graph(tokens):
    current_token = tokens[2]
    current_node = nodes[0]
    while True:
        option = get_option_for_current_token(
            current_node.options,
            current_token
        )
        if len(option.next_node.options) == 0:
            return option.next_node.value
        else:
            current_node = option.next_node
            current_token = tokens[current_node.index]


def main(tokens):
    return process_graph(tokens)


# Примеры использования
print(main([1971, 2019, 2015, 1981, 'VALA']))  # Ожидаемый результат: 13
print(main([1975, 1980, 1991, 1981, 'URWEB']))  # Ожидаемый результат: 12
print(main([1975, 2019, 1986, 1981, 'URWEB']))  # Ожидаемый результат: 5
print(main([1971, 2019, 1986, 1981, 'URWEB']))  # Ожидаемый результат: 6
print(main([1975, 1980, 1986, 1981, 'URWEB']))  # Ожидаемый результат: 3
