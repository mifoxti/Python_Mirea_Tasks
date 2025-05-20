class MealyAutomat:
    def __init__(self):
        self.state = 'Y3'

        self.conditional_transitions = {
            'Y3': {
                'check': [({}, 'Y4', 'd0')]
            },
            'Y4': {
                'add': [({}, 'Y5', 'd4')],
            },
            'Y5': {
                'pan': [({}, 'Y1', 'd5')],
                'add': [({}, 'Y2', 'd1')],
            },
            'Y1': {
                'dash': [({}, 'Y4', 'd0')],
                'add': [({}, 'Y6', 'd0')],
            },
            'Y6': {
                'check': [({'f': 0}, 'Y2', 'd1'),
                          ({'f': 1}, 'Y3', 'd5'), ],
            },
            'Y2': {
                'check': [({'s': 1}, 'Y0', 'd2'),
                          ({'s': 0}, 'Y6', 'd0'), ],
            },
            'Y0': {
                'pan': [({'r': 0}, 'Y0', 'd2'),
                        ({'r': 1}, 'Y7', 'd3'), ],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_state = None
        self.executed_methods = set()
        self.last_output = None
        self.executed_states = ['Y3']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def run(self, command):
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

    def seen_edge(self, from_state, to_state):
        return True if self.transition_counts.get((from_state,
                                                   to_state), 0) else False

    def assign_var(self, name, value):
        self.vars[name] = value

    def has_max_out_edges(self):
        return True if self.state in ['Y0', 'Y1',
                                      'Y6', 'Y2',
                                      'Y5'] else False

    def get_output(self):
        return self.last_output


def main():
    return MealyAutomat()


def test():
    obj = main()
    obj.run('check')
    obj.run('add')
    obj.run('pan')
    assert obj.has_max_out_edges() is True
    obj.run('dash')
    assert obj.seen_edge('Y1', 'Y4')
    obj.run('add')
    obj.run('add')
    assert obj.get_output() == 'd1'
    assert obj.run('check') == 'unsupported'
    assert obj.run('add') == 'unsupported'
    assert obj.run('penis') == 'unknown'
    obj.assign_var('s', 0)
