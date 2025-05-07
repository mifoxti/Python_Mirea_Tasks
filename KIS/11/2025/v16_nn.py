class MealyAutomat:
    def __init__(self):
        self.state = 'J5'

        self.conditional_transitions = {
            'J5': {
                'crawl': [({}, 'J4', 'N4')]
            },
            'J4': {
                'reset': [({}, 'J7', 'N4')],
            },
            'J7': {
                'reset': [({}, 'J1', 'N4')],
            },
            'J1': {
                'load': [({}, 'J3', 'N3')],
            },
            'J3': {
                'crawl': [({}, 'J4', 'N4'), ],
                'draw': [({}, 'J6', 'N2')],
            },
            'J6': {
                'load': [({}, 'J3', 'N3')],
                'mute': [({}, 'J7', 'N4')],
                'walk': [({}, 'J0', 'N2')],
            },
            'J0': {
                'draw': [({'b': 0}, 'J6', 'N2'),
                         ({'b': 1}, 'J2', 'N5')],
            },
            'J2': {
                'erase': [({}, 'J3', 'N3')],
            }

        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = set()

    def part_of_loop(self):
        return self.state != 'J5'

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in self.conditional_transitions.values())

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

    def get_step(self):
        return self.step_count

    def get_output(self):
        return self.last_output

    def __getattr__(self, name):
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
    obj.select('copy')  # 'unknown'
    obj.select('crawl')
    assert obj.get_output() == 'N4'
    assert obj.state == 'J4'
    obj.select('reset')
    obj.select('reset')
    assert obj.part_of_loop() is True
    obj.select('load')
    assert obj.state == 'J3'
    obj.select('crawl')
    obj.state = 'J3'
    obj.select('draw')
    assert obj.state == 'J6'
    obj.select('load')
    obj.state = 'J6'
    obj.select('mute')
    obj.state = 'J6'
    assert obj.select('draw') == 'unsupported'
    obj.select('walk')
    assert obj.select('draw') == 'unsupported'
    assert obj.select('nothing') == 'unknown'
    obj.b(0)
    obj.get_step()
    obj.select('draw')
    obj.state = 'J0'
    obj.b(1)
    obj.select('draw')
    assert obj.state == 'J2'
    obj.select('erase')
    obj.bebra()
