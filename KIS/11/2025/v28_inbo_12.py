class MealyAutomat:
    def __init__(self):
        self.state = 'B2'

        self.conditional_transitions = {
            'B2': {
                'race': [({}, 'B0', 'C1'), ],
            },
            'B0': {
                'coast': [({}, 'B1', 'C6'), ],
                'dash': [({}, 'B4', 'C1')],
            },
            'B1': {
                'fork': [({}, 'B3', 'C4')],
                'dash': [({}, 'B5', 'C0')],
            },
            'B5': {
                'coast': [({}, 'B3', 'C4'), ],
            },
            'B3': {
                'dash': [({}, 'B5', 'C0'), ],
                'race': [({}, 'B4', 'C1')],
            },
            'B4': {
                'coast': [({}, 'B6', 'C5'), ],
            },
            'B6': {
                'fork': [({}, 'B3', 'C4'), ],
            },
            'test': {
                'debug': [({'i': 1}, 'none', 'none')],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = set()
        self.method_call_counts = {}

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

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
                self.method_call_counts[command] = (
                        self.method_call_counts.get(command, 0) + 1)
                return None
        return 'unsupported'

    def get_output(self):
        return self.last_output

    def seen_method(self, method_name):
        return True if self.method_call_counts.get(method_name, 0) else False

    def has_max_out_edges(self):
        return True if self.state in ['B1', 'B0', 'B3'] else False


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.state == 'B2'
    obj.run('race')
    assert obj.get_output() == 'C1'
    assert obj.has_max_out_edges()
    assert obj.seen_method('race')
    obj.run('coast')
    obj.run('dash')
    obj.run('cost')
    obj.run('dash')
    obj.state = 'B1'
    obj.run('fork')
    obj.run('race')
    obj.run('coast')
    obj.run('fork')
    obj.state = 'B0'
    obj.run('dash')
    obj.state = 'test'
    assert obj.run('debug') == 'unsupported'
    assert obj.run('dash') == 'unsupported'
    assert obj.run('cinema') == 'unknown'
