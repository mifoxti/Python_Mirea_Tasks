class MachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'v6'

        # Граф переходов: {from_state: {input: (to_state, output)}}
        self.transitions = {
            'v6': {'lower': ('v3', 'T1')},
            'v3': {'clear': ('v1', 'T0')},
            'v1': {'stay': ('v5', 'T1'), 'stop': ('v0', 'T1')},
            'v5': {'stop': ('v2', 'T1')},
            'v2': {'code': ('v5', 'T0'), 'lower': ('v0', 'T1')},
            'v0': {'lower': ('v1', 'T1'), 'stop': ('v4', 'T0')},
            'v4': {'lower': ('v4', 'T1')},
        }

        self.transition_counts = {}

    def go(self, command):
        # Проверка: существует ли такая команда вообще
        all_commands = set()
        for cmds in self.transitions.values():
            all_commands.update(cmds.keys())

        if command not in all_commands:
            raise MachineException('unknown')

        current_transitions = self.transitions.get(self.state, {})
        if command not in current_transitions:
            raise MachineException('unsupported')

        next_state, output = current_transitions[command]
        self.transition_counts[(self.state, next_state)] = \
            self.transition_counts.get((self.state, next_state), 0) + 1

        self.state = next_state
        return output

    def reset(self):
        self.state = 'v6'
        return 'reset'

    def seen_edge(self, from_state, to_state):
        return self.transition_counts.get((from_state, to_state), 0)

    def has_max_in_edges(self):
        in_counts = {}
        for from_state, transitions in self.transitions.items():
            for _, (to_state, _) in transitions.items():
                in_counts[to_state] = in_counts.get(to_state, 0) + 1

        max_in = max(in_counts.values(), default=0)
        return in_counts.get(self.state, 0) == max_in

    def has_max_out_edges(self):
        out_counts = {state: len(transitions)
                      for state, transitions in self.transitions.items()}
        max_out = max(out_counts.values(), default=0)
        return out_counts.get(self.state, 0) == max_out

    def __getattr__(self, name):
        raise MachineException(f"unsupported")


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
    automaton = main()
    raises(lambda: automaton.go('clear'), MachineException)
    raises(lambda: automaton.go('stay'), MachineException)
    raises(lambda: automaton.go('code'), MachineException)
    raises(lambda: automaton.go('stop'), MachineException)
    raises(lambda: automaton.notloadedtransaction(), MachineException)
    assert automaton.state == 'v6'
    assert automaton.go('lower') == 'T1'
    raises(lambda: automaton.go('lower'), MachineException)
    assert automaton.state == 'v3'
    assert automaton.seen_edge('v6', 'v3') == 1
    assert automaton.go('clear') == 'T0'
    assert automaton.state == 'v1'
    assert automaton.has_max_out_edges()
    assert automaton.go('stay') == 'T1'
    assert automaton.state == 'v5'
    assert automaton.has_max_in_edges()
    assert automaton.go('stop') == 'T1'
    assert automaton.state == 'v2'
    assert automaton.go('code') == 'T0'
    automaton.state = 'v2'
    assert automaton.go('lower') == 'T1'
    assert automaton.state == 'v0'
    assert automaton.go('lower') == 'T1'
    assert automaton.go('stop') == 'T1'
    assert automaton.go('stop') == 'T0'
    assert automaton.state == 'v4'
    assert automaton.go('lower') == 'T1'
    assert automaton.reset() == 'reset'
    raises(lambda: automaton.go('none'), MachineException)
