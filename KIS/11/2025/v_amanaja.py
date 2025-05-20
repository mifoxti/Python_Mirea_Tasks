class MealyAutomat:
    def __init__(self):
        self.state = 's4'

        self.conditional_transitions = {
            's4': {
                'swap': [({}, 's3', 'w2')]
            },
            's3': {
                'daub': [({}, 's2', 'w2')],
            },
            's2': {
                'swap': [({}, 's1', 'w5')],
            },
            's1': {
                'daub': [({}, 's5', 'w6')],
            },
            's5': {
                'paste': [({'u': 0}, 's7', 'w0'),
                          ({'u': 1}, 's6', 'w5'),
                          ({'u': 2}, 's5', 'w0'), ],
            },
            's6': {
                'pan': [({'c': 0}, 's7', 'w4'),
                        ({'c': 1}, 's0', 'w2'),
                        ({'c': 2}, 's5', 'w1'), ],
            },
            's7': {
                'swap': [({}, 's0', 'w0')]
            },
            's0': {
                'pan': [({}, 's5', 'w1'), ]
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_state = None
        self.executed_methods = set()
        self.executed_states = ['R4']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def move(self, command):
        if not self._trigger_exists(command):
            return 'unknown'

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            return 'unsupported'

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
                return output
        return 'unsupported'

    def get_step(self):
        return self.step_count

    def seen_method(self, method):
        return True if method in self.executed_methods else False

    def __getattr__(self, name):
        name = name.replace('store_', '')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        return lambda *args, **kwargs: self.move(name)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.move('swap') == 'w2'
    assert obj.move('daub') == 'w2'
    assert obj.move('swap') == 'w5'
    assert obj.move('daub') == 'w6'
    assert obj.state == 's5'
    assert obj.move('paste') == 'unsupported'
    assert obj.move('daub') == 'unsupported'
    assert obj.move('popa') == 'unknown'
    assert obj.store_u(2) is None
    assert obj.move('paste') == 'w0'
    assert obj.store_u(1) is None
    assert obj.move('paste') == 'w5'
    assert obj.store_c(2) is None
    assert obj.move('pan') == 'w1'
    assert obj.store_u(0) is None
    assert obj.move('paste') == 'w0'
    assert obj.move('swap') == 'w0'
    assert obj.move('pan') == 'w1'
    obj.state = 's6'
    assert obj.store_c(0) is None
    assert obj.move('pan') == 'w4'
    obj.state = 's6'
    assert obj.store_c(1) is None
    assert obj.move('pan') == 'w2'
    assert obj.seen_method('daub') is True
    assert obj.get_step() == 12
    assert obj.bomba() == 'unknown'
