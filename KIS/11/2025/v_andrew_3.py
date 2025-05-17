class MealyAutomat:
    def __init__(self):
        self.state = 'F0'

        self.conditional_transitions = {
            'F0': {
                'check': [({}, 'F5', 'D0')]
            },
            'F5': {
                'load': [({'p': 0}, 'F1', 'D0'),
                         ({'p': 1}, 'F4', 'D1'), ],
            },
            'F1': {
                'stay': [({}, 'F3', 'D0')],
            },
            'F3': {
                'load': [({'t': 0}, 'F1', 'D0'),
                         ({'t': 1}, 'F4', 'D1'), ],
            },
            'F4': {
                'check': [({}, 'F2', 'D0'), ],
            },
            'F2': {
                'check': [({'w': 0}, 'F3', 'D1'),
                          ({'w': 1}, 'F5', 'D2'), ],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = set()

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

    def go(self, command):
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
                return output
        return 'unsupported'

    def get_step(self):
        return self.step_count

    def has_path_to(self, state):
        return True if state in ['F5', 'F1', 'F2', 'F3', 'F4'] else False

    def __getattr__(self, name):
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        return lambda *args, **kwargs: self.go(name)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.go('roam') == 'unknown'
    assert obj.go('load') == 'unsupported'
    assert obj.go('check') == 'D0'
    assert obj.has_path_to('F3') is True
    assert obj.get_step() == 1
    assert obj.go('load') == 'unsupported'
    obj.p(0)
    obj.go('load')
    obj.go('stay')
    obj.t(0)
    obj.go('load')
    obj.go('stay')
    obj.t(1)
    obj.go('load')
    obj.go('check')
    obj.w(0)
    obj.go('check')
    obj.go('load')
    obj.go('check')
    obj.w(1)
    obj.go('check')
    obj.p(1)
    obj.go('load')
    obj.gone()
