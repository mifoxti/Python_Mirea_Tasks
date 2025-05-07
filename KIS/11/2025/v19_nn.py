class MealyAutomat:
    def __init__(self):
        self.state = 'b1'

        self.conditional_transitions = {
            'b1': {
                'scan': [({}, 'b2', 'X1')]
            },
            'b2': {
                'cull': [({}, 'b1', 'X0')],
                'push': [({}, 'b2', 'X1')],
                'brake': [({}, 'b0', 'X4')],
                'scan': [({}, 'b5', 'X1')],
            },
            'b0': {
                'push': [({}, 'b6', 'X0')],
                'brake': [({}, 'b4', 'X1')],
            },
            'b6': {
                'scan': [({}, 'b3', 'X1'), ],
            },
            'b3': {
                'cull': [({}, 'b4', 'X2'), ],
            },
            'b4': {
                'cull': [({'h': 1}, 'b1', 'X0'),
                         ({'h': 0}, 'b5', 'X1'), ],
            },
            'b5': {
                'push': [({}, 'b7', 'X2')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_state = None
        self.executed_methods = set()

    def has_max_in_edges(self):
        in_counts = {}
        for transitions in self.conditional_transitions.values():
            for action, variants in transitions.items():
                for (_, target, _) in variants:
                    in_counts[target] = in_counts.get(target, 0) + 1

        max_in = max(in_counts.values(), default=0)
        return in_counts.get(self.state, 0) == max_in

    def has_path_to(self, target_state):
        """Проверяет, можно ли добраться из текущего состояния до target_state."""
        paths = {'b1': ['b2'],
                 'b2': ['b2', 'b1', 'b0', 'b5'],
                 'b0': ['b6', 'b4'],
                 'b6': ['b3'],
                 'b3': ['b4'],
                 'b4': ['b5', 'b1'],
                 'b5': ['b7'],}
        if target_state in paths[self.state]:
            return True
        else:
            return False

    def seen_method(self, method_name):
        """Проверяет, выполнялся ли метод успешно ранее."""
        return method_name.lstrip('go_') in self.executed_methods

    def set_var(self, key, value):
        self.vars[key] = value

    def _trigger_exists(self, name):
        """Проверяет, существует ли триггер в любом состоянии автомата."""
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        """Пытается применить триггер в текущем состоянии."""
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            # self.last_state = ''  # Сбрасываем при неудаче
            return 'unsupported'

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state, to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_methods.add(name)
                self.last_state = output
                return None

        # self.last_state = ''  # Сбрасываем если не нашли подходящих условий
        return 'unsupported'

    def get_output(self):
        return self.last_state

    def __getattr__(self, name):
        name = name.lstrip('go_')
        if not self._trigger_exists(name):
            return lambda: 'unknown'
        return lambda: (self._try_apply_trigger(name) or None)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.state == 'b1'
    assert obj.has_path_to('b2')
    assert obj.has_path_to('b0') is False
    obj.go_scan()
    assert obj.get_output() == 'X1'
    obj.go_cull()
    obj.state = 'b2'
    obj.go_scan()
    obj.state = 'b2'
    obj.go_push()
    assert obj.has_max_in_edges()
    obj.go_brake()
    assert obj.seen_method('go_push')
    obj.go_push() # b6
    obj.go_scan()
    assert obj.go_brake() == 'unsupported'
    assert obj.go_to_the_bar() == 'unknown'
    obj.go_cull()
    obj.state = 'b0'
    obj.go_brake()
    obj.set_var('h', 1)
    obj.go_cull()
    obj.state = 'b4'
    obj.set_var('h', 0)
    obj.go_cull()
    obj.go_push()
    obj.go_scan()
