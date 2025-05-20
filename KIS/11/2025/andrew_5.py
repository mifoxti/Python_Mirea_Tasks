class MealyAutomat:
    def __init__(self):
        self.state = 'z5'

        self.conditional_transitions = {
            'z5': {
                'clean': [({}, 'z1', 'E0'), ],
            },
            'z1': {
                'spin': [({'r': 1}, 'z0', 'E1'),
                         ({'r': 2}, 'z1', 'E0'),
                         ({'r': 0}, 'z6', 'E1'), ],
            },
            'z0': {
                'show': [({}, 'z4', 'E0')],
            },
            'z4': {
                'forge': [({}, 'z7', 'E0')],
            },
            'z7': {
                'play': [({}, 'z2', 'E1')],
                'clean': [({}, 'z6', 'E1')],
            },
            'z2': {
                'play': [({}, 'z6', 'E1'), ],
            },
            'z6': {
                'spin': [({'g': 1}, 'z0', 'E1'),
                         ({'g': 0}, 'z3', 'E0'), ],
            },
            'z3': {
                'show': [({}, 'z3', 'E1')],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = []
        self.executed_states = ['z5']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            return "unsupported"

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.last_output = output
                self.executed_methods.append(name)
                self.executed_states.append(to_state)
                return output
        return "unsupported"

    def seen_method(self, method):
        return True if method in self.executed_methods else False

    def assign_var(self, name, value):
        self.vars[name] = value

    def seen_state(self, state):
        return True if self.executed_states.count(state) else False

    def seen_edge(self, from_state, to_state):
        return True if ((from_state, to_state)
                        in self.transition_counts) else False

    def __getattr__(self, name):
        if not self._trigger_exists(name):
            return lambda: "unknown"
        return lambda: (self._try_apply_trigger(name) or None)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.show() == 'unsupported'
    assert obj.gay() == 'unknown'
    assert obj.seen_edge('z5', 'z1') is False
    assert obj.seen_method('forge') is False
    assert obj.assign_var('g', 0) is None
    assert obj.forge() == 'unsupported'
    assert obj.clean() == 'E0'
    assert obj.seen_state('z3') is False
    assert obj.seen_edge('z2', 'z6') is False
    assert obj.spin() == 'unsupported'
    assert obj.assign_var('r', 0) is None
    assert obj.spin() == 'E1'
    assert obj.spin() == 'E0'
    assert obj.show() == 'E1'
    assert obj.seen_method('show') is True
