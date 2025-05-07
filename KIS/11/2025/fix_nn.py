class MealyAutomat:
    def __init__(self):
        self.state = 'H4'
        self.vars = {}
        self.executed_methods = set()
        self.last_output = None

        self.transitions = {
            'H5': {
                'show': [({}, 'H4', 'V1')],
                'tag': [({}, 'H0', 'V0')],
                'speed': [({}, 'H1', 'V0')],
            },
            'H0': {
                'show': [
                    ({'y': 0}, 'H0', 'V0'),
                    ({'y': 1}, 'H4', 'V1'),
                    ({'y': 2}, 'H4', 'V1')
                ],
                'tag': [({}, 'H2', 'V0')],
            },
            'H1': {
                'speed': [({}, 'H5', 'V0')],
            },
            'H2': {
                'march': [({}, 'H3', 'V0')],
            },
            'H3': {},
            'H4': {
                'show': [({}, 'H1', 'V1')],
                'march': [({}, 'H3', 'V1')],
            },
        }

        self.all_states = set(self.transitions.keys())
        self.adjacency = {state: set() for state in self.all_states}
        for src, transitions in self.transitions.items():
            for method, variants in transitions.items():
                for cond, dst, output in variants:
                    self.adjacency[src].add(dst)

    def let_var(self, name, value):
        self.vars[name] = value

    def _method_exists(self, method_name):
        return any(
            method_name in state_transitions
            for state_transitions in self.transitions.values()
        )

    def _apply_method(self, method_name):
        if method_name not in self.transitions.get(self.state, {}):
            if self._method_exists(method_name):
                return 'unsupported'
            return 'unknown'

        variants = self.transitions[self.state][method_name]

        for conditions, next_state, output in variants:
            if all(self.vars.get(k) == v for k, v in conditions.items()):
                self.state = next_state
                self.executed_methods.add(method_name)
                self.last_output = output
                return output

        return 'unsupported'

    def go(self, method_name):
        return self._apply_method(method_name)

    def seen_method(self, method_name):
        return method_name in self.executed_methods

    def has_path_to(self, target_state):
        if target_state not in self.all_states:
            return False

        visited = set()
        queue = [self.state]

        while queue:
            current = queue.pop(0)
            if current == target_state:
                return True
            if current in visited:
                continue
            visited.add(current)
            queue.extend(self.adjacency[current])

        return False

    def has_max_out_edges(self):
        if not self.transitions:
            return False

        max_out = max(
            len(transitions)
            for transitions in self.transitions.values()
        )
        current_out = len(self.transitions.get(self.state, {}))
        return current_out == max_out


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.state == 'H4'
    assert obj.go('nonexistent') == 'unknown'
    assert obj.go('speed') == 'unsupported'
    assert obj.go('show') == 'V1'
    assert obj.go('speed') == 'V0'
    assert obj.go('march') == 'V1'
    obj.state = 'H1'
    assert obj.go('show') == 'V1'



if __name__ == "__main__":
    result = test()
    print(result)
