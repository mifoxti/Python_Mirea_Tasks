class MealyAutomat:
    def __init__(self):
        self.state = 'E5'

        self.conditional_transitions = {
            'E5': {
                'chalk': [({}, 'E4', 't1'), ],
            },
            'E4': {
                'make': [({}, 'E1', 't4'), ],
            },
            'E1': {
                'make': [({}, 'E1', 't4'), ],
                'drag': [({}, 'E2', 't2'), ],
            },
            'E2': {
                'etch': [({}, 'E2', 't2')],
                'make': [({}, 'E3', 't2'), ],
                'pull': [({}, 'E0', 't2'), ],
            },
            'E3': {
                'pull': [({}, 'E0', 't2')],
                'drag': [({}, 'E4', 't1'), ],
            },
            'test': {
                'debug': [({'i': 1}, 'none', 'none')],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.method_call_counts = {}
        self.executed_states = ['E5']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

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
                self.last_output = output
                self.executed_states.append(next_state)
                self.method_call_counts[command] = (
                        self.method_call_counts.get(command, 0) + 1)
                return None
        return 'unsupported'

    def seen_method(self, method_name):
        return True if self.method_call_counts.get(method_name, 0) else False

    def seen_state(self, state_name):
        return self.executed_states.count(state_name)

    def get_output(self):
        return self.last_output


def main():
    return MealyAutomat()


def test():
    obj = main()
    obj.run('chalk')
    assert obj.get_output() == 't1'
    obj.run('make')
    obj.run('make')
    obj.run('drag')
    obj.run('etch')
    obj.run('make')
    obj.run('drag')
    obj.state = 'E3'
    obj.run('pull')
    obj.state = 'E2'
    obj.run('pull')
    assert obj.seen_state('E1') == 2
    assert obj.seen_method('chalk') is True
    assert obj.run('pull') == 'unsupported'
    obj.state = 'test'
    assert obj.run('debug') == 'unsupported'
    assert obj.run('none') == 'unknown'
