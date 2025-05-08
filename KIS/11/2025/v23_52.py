class MealyAutomat:
    def __init__(self):
        self.state = 'R4'

        self.conditional_transitions = {
            'R4': {
                'rig': [({}, 'R6', 'm4')]
            },
            'R6': {
                'tread': [({}, 'R3', 'm0')],
            },
            'R3': {
                'jump': [({}, 'R5', 'm3')],
            },
            'R5': {
                'drag': [({'b': 0}, 'R2', 'm0'),
                         ({'b': 1}, 'R1', 'm0'),
                         ({'b': 2}, 'R0', 'm1'),
                         ({'b': 3}, 'R3', 'm0'), ],
            },
            'R0': {
                'hike': [({}, 'R1', 'm0')],
            },
            'R1': {
                'tread': [({'z': 0}, 'R5', 'm3'),
                          ({'z': 1}, 'R2', 'm0')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_state = None
        self.executed_states = ['R4']

    def has_max_out_edges(self):
        return False if self.state != 'R5' else True

    def has_path_to(self, target_state):
        paths = {
            'R4': ['R6', 'R3', 'R5', 'R0', 'R1', 'R2'],
            'R6': ['R3', 'R5', 'R0', 'R1', 'R2'],
            'R3': ['R5', 'R0', 'R1', 'R2', 'R3'],
            'R5': ['R3', 'R0', 'R1', 'R2', 'R5'],
            'R0': ['R3', 'R0', 'R1', 'R2', 'R5'],
            'R1': ['R1', 'R2', 'R5', 'R3', 'R0'],
            'R2': [],
        }
        return target_state in paths[self.state]

    def seen_state(self, state_name):
        return state_name in self.executed_states

    def set_var(self, key, value):
        self.vars[key] = value

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

    def get_output(self):
        return self.last_state

    def __getattr__(self, name):
        if not self._trigger_exists(name):
            return lambda: 'unknown'
        return lambda: (self._try_apply_trigger(name) or None)


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.state == 'R4'
    assert obj.has_path_to('R2')
    obj.rig()
    assert obj.last_state == 'm4'
    assert obj.seen_state('R6')
    obj.tread()
    assert obj.has_max_out_edges() is False
    obj.jump()
    assert obj.drag() == 'unsupported'
    obj.set_var('b', 3)
    obj.drag()
    obj.get_output()
    obj.jump()
    obj.set_var('b', 2)
    obj.drag()
    obj.hike()
    obj.set_var('z', 0)
    obj.tread()
    obj.set_var('b', 1)
    obj.drag()
    obj.set_var('z', 1)
    obj.tread()
    assert obj.drag() == 'unsupported'
    assert obj.nike() == 'unknown'
    obj.state = 'R5'
    obj.set_var('b', 0)
    obj.drag()
