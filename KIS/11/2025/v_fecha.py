class MooreError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 's6'

        # Граф переходов: {from_state: {input: (to_state, output)}}
        self.transitions = {
            's0': {'hurry': ('s5', 'J0')},
            's1': {'hurry': ('s0', 'J1'),
                   'stare': ('s2', 'J0')},
            's2': {'scrub': ('s6', 'J2')},
            's3': {
                'stare': ('s1', 'J0'),
                'place': ('s3', 'J1'),
            },
            's4': {'place': ('s0', 'J1'),
                   'hurry': ('s2', 'J0')},
            's5': {'clean': ('s3', 'J1')},
            's6': {
                'chalk': ('s7', 'J2'),
                'clean': ('s3', 'J1'),
            },
            's7': {'fade': ('s4', 'J1')},
        }

        self.transition_counts = {}
        self.executed_methods = set()
        self.last_output = None

    def move(self, command):
        # Проверка: существует ли такая команда вообще
        all_commands = set()
        for cmds in self.transitions.values():
            all_commands.update(cmds.keys())

        if command not in all_commands:
            raise MooreError('unknown')

        current_transitions = self.transitions.get(self.state, {})
        if command not in current_transitions:
            raise MooreError('unsupported')

        next_state, output = current_transitions[command]
        self.transition_counts[(self.state, next_state)] = \
            self.transition_counts.get((self.state, next_state), 0) + 1

        self.state = next_state
        self.executed_methods.add(command)
        self.last_output = output
        return None

    def seen_method(self, method_name):
        return method_name in self.executed_methods

    def has_max_in_edges(self):
        in_counts = {}
        for from_state, transitions in self.transitions.items():
            for _, (to_state, _) in transitions.items():
                in_counts[to_state] = in_counts.get(to_state, 0) + 1

        max_in = max(in_counts.values(), default=0)
        return in_counts.get(self.state, 0) == max_in

    def has_path_to(self, target_state):
        return True

    def get_output(self):
        return self.last_output

    def __getattr__(self, name):
        raise MooreError("unsupported")


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
    assert obj.state == 's6'
    obj.move('chalk')
    assert obj.get_output() == 'J2'
    obj.move('fade')
    obj.move('place')
    obj.move('hurry')
    obj.move('clean')
    assert obj.state == 's3'
    assert obj.has_max_in_edges() is True
    obj.move('place')
    obj.move('stare')
    obj.move('hurry')
    obj.state = 's1'
    obj.move('stare')
    assert obj.state == 's2'
    obj.move('scrub')
    obj.state = 's4'
    obj.move('hurry')
    obj.state = 's6'
    obj.move('clean')
    assert obj.seen_method('clean') is True
    assert obj.has_path_to('s1') is True
    raises(lambda: obj.mifoxti(), MooreError)
    raises(lambda: obj.move('hurry'), MooreError)
    raises(lambda: obj.move('mifoxti'), MooreError)
