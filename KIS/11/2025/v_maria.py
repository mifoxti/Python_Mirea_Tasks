class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'v5'

        self.conditional_transitions = {
            'v5': {
                'begin': [({}, 'v0', 'j1')],
                'etch': [({}, 'v2', 'j2')],
            },
            'v0': {
                'sort': [({}, 'v4', 'j3')],
                'turn': [({}, 'v1', 'j0')],
            },
            'v4': {
                'etch': [({}, 'v2', 'j2')],
                'sort': [({}, 'v3', 'j0')],
            },
            'v2': {
                'begin': [({}, 'v1', 'j0')],
            },
            'v1': {
                'log': [({}, 'v3', 'j0'), ],
            },
            'v3': {
                'etch': [({}, 'v0', 'j1'), ],
            },
            'debug': {
                'test': [({'lol': 1}, 'none', 'none')],
            }
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_state = None
        self.executed_methods = set()
        self.last_output = None
        self.executed_states = ['v5']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def run(self, command):
        if not self._trigger_exists(command):
            raise StateMachineException("unknown")

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
                self.executed_states.append(next_state)
                self.last_output = output
                return None
        raise StateMachineException('unsupported')

    def get_output(self):
        return self.last_output

    def seen_state(self, state):
        return self.executed_states.count(state)

    def part_of_loop(self):
        return True if self.state != 'v5' else False


def main():
    return MealyAutomat()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


def test():
    obj = main()
    obj.run('begin')
    assert obj.get_output() == 'j1'
    obj.run('sort')
    assert obj.part_of_loop() is True
    assert obj.seen_state('v5') == 1
    obj.run('etch')
    obj.run('begin')
    obj.run('log')
    obj.run('etch')
    obj.run('turn')
    obj.run('log')
    obj.run('etch')
    obj.run('sort')
    obj.run('sort')
    obj.state = 'v5'
    obj.run('etch')
    obj.state = 'debug'
    raises(lambda: obj.run('test'), StateMachineException)
    raises(lambda: obj.run('etch'), StateMachineException)
    raises(lambda: obj.run('getero'), StateMachineException)
