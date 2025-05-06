class MachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'X3'

        self.conditional_transactions = {
            'X3': {
                'unite': [({}, 'X5', 'W1')]
            },
            'X5': {
                'fork': [({}, 'X1', 'W2')],
                'glare': [({}, 'X2', 'W1')],
            },
            'X2': {
                'bolt': [({}, 'X7', 'W2')],
            },
            'X7': {
                'unite': [({'v': 0}, 'X5', 'W0')],
                'unite': [({'v': 1}, 'X1', 'W2')],
            },
            'X1': {
                'fork': [({'a': 1}, 'X6', 'W2')],
                'fork': [({'a': 2}, 'X4', 'W0')],
                'fork': [({'a': 0}, 'X3', 'W0')],
            },
            'X6': {
                'mute': [({}, 'X0', 'W1')],
            },
            'X0': {
                'mute': [({}, 'X6', 'W2')],
                'glare': [({}, 'X4', 'W2')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0

    def has_max_out_edges(self):
        out_counts = {state: len(transitions)
                      for state, transitions
                      in self.conditional_transactions.items()}
        max_out = max(out_counts.values(), default=0)
        return out_counts.get(self.state, 0) == max_out

    def get_step(self):
        return self.step_count

    def let_var(self, key, value):
        self.vars[key] = value

    def __getattr__(self, name):
        def method():
            current = self.conditional_transitions.get(self.state, {})
            if name not in current:
                raise MachineException('unknown')

            for conds, to_state, output in current[name]:
                if all(self.vars.get(k) == v for k, v in conds.items()):
                    self.transition_counts[(self.state, to_state)] = \
                        self.transition_counts.get((self.state, to_state), 0) + 1
                    self.state = to_state
                    self.step_count += 1
                    return output
            raise MachineException('unsupported')
        return method


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
    assert obj.has_max_out_edges() == False
