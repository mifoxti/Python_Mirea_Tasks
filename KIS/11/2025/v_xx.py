class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'b4'

        self.conditional_transitions = {
            'b4': {
                'join': [({}, 'b4', 'n1')],
                'tweak': [({}, 'b3', 'n2')],
            },
            'b3': {
                'sit': [({}, 'b2', 'n1'), ],
            },
            'b2': {
                'paste': [({}, 'b5', 'n2')],
                'tweak': [({}, 'b2', 'n1')],
                'join': [({}, 'b4', 'n1')],
            },
            'b5': {
                'sit': [({}, 'b6', 'n3'), ],
            },
            'b6': {
                'tweak': [({}, 'b5', 'n2'), ],
                'shade': [({}, 'b0', 'n3')],
            },
            'b0': {
                'tweak': [({}, 'b1', 'n3')],
            },
            'test': {
                'debug': [({'d': 1}, 'none', 'none'), ],
            },
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['b4']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def move(self, command):
        if not self._trigger_exists(command):
            raise StateMachineException('unknown')

        current_transitions = self.conditional_transitions.get(self.state, {})
        if command not in current_transitions:
            raise StateMachineException('unsupported')

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
        raise StateMachineException('unsupported')

    def seen_method(self, method_name):
        return True if method_name in self.executed_methods else False

    def part_of_loop(self):
        return True if self.state not in ['b0', 'b1'] else False

    def get_output(self):
        return self.last_output


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def main():
    return MealyAutomat()


def test():
    obj = main()
    assert obj.move('tweak') is None
    assert obj.get_output() == 'n2'
    assert obj.part_of_loop() is True
    assert obj.move('sit') is None
    assert obj.part_of_loop() is True
    assert obj.get_output() == 'n1'
    assert obj.seen_method('join') is False
    assert obj.move('paste') is None
    assert obj.get_output() == 'n2'
    assert obj.move('sit') is None
    assert obj.part_of_loop() is True
    assert obj.get_output() == 'n3'
    assert obj.move('shade') is None
    assert obj.get_output() == 'n3'
    assert obj.move('tweak') is None
    assert obj.seen_method('shade') is True
    assert obj.get_output() == 'n3'
    assert obj.seen_method('sit') is True
    obj.state = 'test'
    raises(lambda: obj.move('tweak'), StateMachineException)
    raises(lambda: obj.move('debug'), StateMachineException)
    raises(lambda: obj.move('none'), StateMachineException)
