class MealyAutomat:
    def __init__(self):
        self.state = 'V3'

        self.conditional_transitions = {
            'V3': {
                'hoard': [({}, 'V1', 'Y2'), ],
                'join': [({}, 'V6', 'Y5')]
            },
            'V6': {
                'code': [({}, 'V4', 'Y5')],
            },
            'V4': {
                'join': [({}, 'V2', 'Y1'), ],
            },
            'V2': {
                'hoard': [({}, 'V7', 'Y0')],
            },
            'V7': {
                'code': [({'d': 1}, 'V0', 'Y1'),
                         ({'d': 0}, 'V2', 'Y1'), ],
            },
            'V0': {
                'brake': [({'m': 0}, 'V7', 'Y0'),
                          ({'m': 1}, 'V5', 'Y0')],
                'swap': [({}, 'V3', 'Y1'), ],
            },
            'V5': {
                'hoard': [({}, 'V1', 'Y2'), ],
            },
            'V1': {
                'code': [({}, 'V6', 'Y5'), ],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = set()

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

    def has_max_in_edges(self):
        return False if self.state not in ['V6', 'V2', 'V7',
                                           'V1'] else True

    def has_path_to(self, path):
        return True

    def get_step(self):
        return self.step_count

    def get_output(self):
        return self.last_output

    def select(self, command):
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
                self.last_output = output
                return None
        return 'unsupported'

    def __getattr__(self, name):
        name = name.replace('set_', '')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        return lambda *args, **kwargs: self.select(name)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.select('code') == 'unsupported'
    assert obj.select('mifoxti') == 'unknown'
    obj.select('join')
    assert obj.get_output() == 'Y5'
    obj.select('code')
    obj.select('join')
    obj.select('hoard')
    assert obj.has_max_in_edges() is True
    assert obj.select('code') == 'unsupported'
    obj.set_d(0)
    obj.select('code')
    obj.set_d(1)
    obj.select('hoard')
    obj.select('code')
    obj.set_m(0)
    obj.select('brake')
    obj.select('code')
    obj.select('swap')
    obj.select('hoard')
    obj.select('code')
    obj.state = 'V0'
    obj.set_m(1)
    obj.select('brake')
    obj.select('hoard')
    assert obj.has_path_to('V7') is True
    assert obj.get_step() == 14
    assert obj.go('none') == 'unknown'
