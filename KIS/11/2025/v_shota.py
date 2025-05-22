class MealyAutomat:
    def __init__(self):
        self.state = 'j5'

        self.conditional_transitions = {
            'j5': {
                'pull': [({}, 'j0', 'q1')],
            },
            'j0': {
                'loop': [({'v': 0}, 'j3', 'q1'),
                         ({'v': 1}, 'j2', 'q0'), ],
            },
            'j3': {
                'tail': [({}, 'j4', 'q1')],
                'pull': [({}, 'j2', 'q1'), ],
            },
            'j4': {
                'cue': [({}, 'j3', 'q2'), ],
                'link': [({}, 'j1', 'q0'), ],
            },
            'j1': {
                'loop': [({}, 'j6', 'q0'), ],
            },
            'j6': {
                'hop': [({}, 'j2', 'q1')],
            },
            'j2': {
                'link': [({}, 'j0', 'q1'), ],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['j5']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

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

    def assign_var(self, name, value):
        self.vars[name] = value

    def has_max_out_edges(self):
        return True if self.state in ['j3', 'j0'] else False

    def get_step(self):
        return self.step_count


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.go('tail') == 'unsupported'
    assert obj.has_max_out_edges() is False
    assert obj.go('loop') == 'unsupported'
    assert obj.get_step() == 0
    assert obj.go('show') == 'unknown'
    assert obj.go('pull') == 'q1'
    assert obj.go('loop') == 'unsupported'
    assert obj.assign_var('v', 0) is None
    assert obj.go('loop') == 'q1'
    assert obj.go('tail') == 'q1'
    assert obj.go('cue') == 'q2'
    assert obj.go('pull') == 'q1'
    assert obj.has_max_out_edges() is False
