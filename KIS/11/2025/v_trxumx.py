class MealyAutomat:
    def __init__(self):
        self.state = 'K1'

        self.conditional_transitions = {
            'K1': {
                'carve': [({}, 'K3', 'G2'), ],
            },
            'K3': {
                'close': [({}, 'K4', 'G5'), ]
            },
            'K4': {
                'close': [({'m': 0}, 'K0', 'G4'),
                          ({'m': 1}, 'K6', 'G5'), ],
                'turn': [({}, 'K2', 'G2')]
            },
            'K2': {
                'fill': [({}, 'K1', 'G6')],
                'crack': [({}, 'K0', 'G4')],
            },
            'K0': {
                'crack': [({}, 'K6', 'G5')],
            },
            'K6': {
                'clear': [({}, 'K0', 'G4')],
                'fill': [({}, 'K5', 'G4')],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['K1']
        self.executed_methods = set()

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def get_step(self):
        return self.step_count

    def has_max_in_edges(self):
        return False if self.state not in ['K0'] else True

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

    def set_var(self, var, value):
        self.vars[var] = value

    def seen_edge(self, from_state, to_state):
        return True if ((from_state, to_state)
                        in self.transition_counts) else False

    def seen_method(self, method_name):
        return True if method_name in self.executed_methods else False

    def get_output(self):
        return self.last_output


def main():
    return MealyAutomat()


def test():
    obj = main()
    obj.run('carve')
    obj.run('close')
    obj.run('turn')
    obj.run('fill')
    obj.state = 'K4'
    assert obj.run('close') == 'unsupported'
    assert obj.run('clear') == 'unsupported'
    assert obj.run('none') == 'unknown'
    obj.set_var('m', 0)
    obj.run('close')
    obj.state = 'K4'
    obj.set_var('m', 1)
    obj.run('close')
    obj.run('clear')
    obj.run('crack')
    obj.run('fill')
    obj.state = 'K2'
    obj.run('crack')
    obj.get_step()
    assert obj.has_max_in_edges() is True
    assert obj.get_output() == 'G4'
    assert obj.seen_method('close') is True
    assert obj.seen_edge('K2', 'K1') is True
