class FSMException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'e2'

        self.conditional_transitions = {
            'e2': {
                'carve': [({'u': 0}, 'e3', 'K1'),
                          ({'u': 1}, 'e6', 'K0'), ],
            },
            'e3': {
                'pan': [({'v': 0}, 'e2', 'K1'),
                        ({'v': 1}, 'e4', 'K1'), ],
            },
            'e4': {
                'spin': [({}, 'e5', 'K1')],
            },
            'e5': {
                'melt': [({}, 'e1', 'K0'), ],
            },
            'e1': {
                'pan': [({}, 'e0', 'K0'), ],
            },
            'e0': {
                'pan': [({}, 'e4', 'K1')],
                'melt': [({}, 'e6', 'K0'), ],
            },
            'e6': {
                'pan': [({}, 'e0', 'K0'), ],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['e2']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def run(self, command):
        if not self._trigger_exists(command):
            raise FSMException('unknown')

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            raise FSMException('unsupported')

        transitions = current_transitions[command]

        for conds, next_state, output in transitions:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, next_state)] = (
                        self.transition_counts.get((self.state,
                                                    next_state), 0) + 1
                )
                self.state = next_state
                self.step_count += 1
                self.executed_methods.add(command)
                self.last_output = output
                return None
        raise FSMException('unsupported')

    def has_path_to(self, state):
        paths = {
            'e2': ['e2', 'e3', 'e4', 'e5', 'e1', 'e0', 'e6'],
            'e3': ['e2', 'e3', 'e4', 'e5', 'e1', 'e0', 'e6'],
            'e4': ['e4', 'e5', 'e1', 'e0', 'e6'],
            'e5': ['e4', 'e5', 'e1', 'e0', 'e6'],
            'e1': ['e4', 'e5', 'e1', 'e0', 'e6'],
            'e0': ['e4', 'e5', 'e1', 'e0', 'e6'],
            'e6': ['e4', 'e5', 'e1', 'e0', 'e6'],
        }
        return True if state in paths[self.state] else False

    def part_of_loop(self):
        return True

    def get_output(self):
        return self.last_output

    def __getattr__(self, name):
        name = name.lstrip('assign_')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        return lambda *args, **kwargs: self.run(name)


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
    raises(lambda: obj.run('carve'), FSMException)
    raises(lambda: obj.run('pan'), FSMException)
    raises(lambda: obj.run('admins.say.mooo'), FSMException)
    obj.u(1)
    obj.run('carve')
    assert obj.get_output() == 'K0'
    assert obj.part_of_loop() is True
    assert obj.has_path_to('e0') is True
    obj.pan()
