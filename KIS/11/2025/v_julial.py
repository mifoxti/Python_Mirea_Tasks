class StateMachineError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'F1'

        self.conditional_transitions = {
            'F1': {
                'peek': [({}, 'F7', 'm0')],
                'snap': [({'r': 0}, 'F0', 'm1'),
                         ({'r': 1}, 'F6', 'm0'), ],
            },
            'F7': {
                'peek': [({}, 'F5', 'm1'), ],
            },
            'F5': {
                'peek': [({}, 'F0', 'm0')],
            },
            'F0': {
                'herd': [({'b': 1}, 'F5', 'm0'),
                         ({'b': 0}, 'F3', 'm1')],
            },
            'F3': {
                'init': [({}, 'F6', 'm1')],
            },
            'F6': {
                'init': [({'h': 0}, 'F6', 'm0'),
                         ({'h': 1}, 'F2', 'm0')],
            },
            'F2': {
                'snap': [({}, 'F4', 'm0'), ],
            },
            'F4': {
                'herd': [({}, 'F5', 'm0'), ],
            }
        }
        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.executed_methods = set()

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise StateMachineError('unsupported')

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_methods.add(name)
                return output

        raise StateMachineError('unsupported')

    def __getattr__(self, name):
        name = name.replace('select_', '')
        if not self._trigger_exists(name):
            raise StateMachineError('unknown')
        return lambda: (self._try_apply_trigger(name) or None)

    def store_var(self, name, value):
        self.vars[name] = value
        return None

    def part_of_loop(self):
        return True if self.state not in ['F1', 'F7'] else False

    def has_path_to(self, to_state):
        paths = {
            'F1': ['F7', 'F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
            'F7': ['F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
            'F5': ['F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
            'F0': ['F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
            'F3': ['F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
            'F6': ['F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
            'F2': ['F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
            'F4': ['F5', 'F0', 'F3', 'F6', 'F2', 'F4'],
        }
        return True if to_state in paths[self.state] else False


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.has_path_to('F7') is True
    assert obj.part_of_loop() is False
    assert obj.select_peek() == 'm0'
    assert obj.select_peek() == 'm1'
    assert obj.select_peek() == 'm0'
    raises(lambda: obj.select_herd(), StateMachineError)
    raises(lambda: obj.select_peek(), StateMachineError)
    raises(lambda: obj.select_osu(), StateMachineError)
    obj.store_var('b', 1)
    assert obj.select_herd() == 'm0'
    assert obj.select_peek() == 'm0'
    obj.store_var('b', 0)
    assert obj.select_herd() == 'm1'
    assert obj.select_init() == 'm1'
    obj.store_var('h', 0)
    assert obj.select_init() == 'm0'
    obj.store_var('h', 1)
    assert obj.select_init() == 'm0'
    assert obj.select_snap() == 'm0'
    assert obj.select_herd() == 'm0'
    obj.state = 'F1'
    obj.store_var('r', 0)
    assert obj.select_snap() == 'm1'
    obj.state = 'F1'
    obj.store_var('r', 1)
    assert obj.select_snap() == 'm0'
