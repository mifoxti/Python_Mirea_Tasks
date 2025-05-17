class MealyAutomat:
    def __init__(self):
        self.state = 'P3'

        self.conditional_transitions = {
            'P3': {
                'flip': [({}, 'P4', 'U4')],
            },
            'P4': {
                'log': [({'k': 1}, 'P0', 'U1'),
                        ({'k': 0}, 'P1', 'U3'), ],
            },
            'P0': {
                'start': [({}, 'P2', 'U3')],
            },
            'P2': {
                'start': [({}, 'P5', 'U3')],
            },
            'P5': {
                'march': [({}, 'P0', 'U1')],
                'cast': [({}, 'P1', 'U3')],
            },
            'P1': {
                'apply': [({}, 'P5', 'U3')],
                'log': [({}, 'P3', 'U2'), ]
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['P3']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = (
            self.conditional_transitions.get(self.state, {})
        )
        if name not in current_transitions:
            return 'unsupported'

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts
                        .get((self.state, to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_states.append(self.state)
                self.last_state = output
                return None
        return 'unsupported'

    def set_var(self, name, value):
        self.vars[name] = value

    def has_path_to(self, target_state):
        return True

    def get_output(self):
        return self.last_state

    def has_max_out_edges(self):
        return True if self.state in ['P4', 'P5', 'P1'] else False

    def has_max_in_edges(self):
        return True if self.state in ['P0', 'P5', 'P1'] else False

    def __getattr__(self, name):
        if not self._trigger_exists(name):
            return lambda: "unknown"
        return lambda: (self._try_apply_trigger(name) or None)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.has_path_to('P3') is True
    obj.flip()
    assert obj.get_output() == "U4"
    assert obj.log() == "unsupported"
    assert obj.none() == "unknown"
    assert obj.start() == "unsupported"
    obj.set_var('k', 1)
    obj.log()
    obj.start()
    obj.start()
    obj.march()
    assert obj.has_max_in_edges() is True
    obj.state = 'P5'
    assert obj.has_max_out_edges() is True
    obj.cast()
    obj.apply()
    obj.cast()
    obj.log()
    obj.state = "P4"
    obj.set_var('k', 0)
    obj.log()
