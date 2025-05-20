class MealyAutomat:
    def __init__(self):
        self.state = 'K6'

        self.conditional_transitions = {
            'K6': {
                'post': [({'j': 0}, 'K3', 'c0'),
                         ({'j': 1}, 'K0', 'c1')],
            },
            'K3': {
                'shade': [({}, 'K3', 'c1'), ],
                'post': [({}, 'K0', 'c1')],
            },
            'K0': {
                'push': [({}, 'K4', 'c3')],
            },
            'K4': {
                'shade': [({'m': 0}, 'K5', 'c0'),
                          ({'m': 1}, 'K7', 'c1')],
            },
            'K5': {
                'blame': [({'p': 0}, 'K1', 'c2'),
                          ({'p': 1}, 'K6', 'c1')],
            },
            'K1': {
                'post': [({}, 'K2', 'c1'), ],
            },
            'K2': {
                'post': [({}, 'K1', 'c1'), ],
                'push': [({}, 'K7', 'c3')],
            },
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
                self.method_call_counts[command] = (
                        self.method_call_counts.get(command, 0) + 1)
                return output
        return 'unsupported'

    def part_of_loop(self):
        return True if self.state != 'K7' else False

    def has_path_to(self, state):
        if self.state == 'K7':
            return False
        elif self.state in ('K1', 'K2') and state not in ['K1', "K2", 'K7']:
            return False
        return True

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
    assert obj.go('post') == 'unsupported'
    assert obj.go('push') == 'unsupported'
    assert obj.go('none') == 'unknown'
    obj.j(0)
    assert obj.go('post') == 'c0'
    assert obj.part_of_loop() is True
    assert obj.has_path_to('K7') is True
    obj.go('shade')
    obj.go('post')
    obj.go('push')
    obj.m(0)
    obj.go('shade')
    obj.p(1)
    obj.go('blame')
    obj.j(1)
    obj.go('post')
    obj.go('push')
    obj.go('shade')
    obj.p(0)
    obj.go('blame')
    obj.go('post')
    obj.go('post')
    obj.go('post')
    obj.go('push')
    obj.m(1)
    obj.state = "K4"
    obj.go('shade')
    obj.none()
    obj.state = "K1"
    obj.has_path_to('K3')
    obj.state = "K7"
    obj.has_path_to('K3')
