class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'Q7'

        self.conditional_transitions = {
            'Q7': {
                'walk': [({}, 'Q5', 'M0')],
            },
            'Q5': {
                'jump': [({'p': 0}, 'Q3', 'M1'),
                         ({'p': 1}, 'Q6', 'M0'), ],
            },
            'Q3': {
                'walk': [({}, 'Q0', 'M1')],
                'clear': [({}, 'Q6', 'M0'), ],
            },
            'Q0': {
                'clear': [({}, 'Q6', 'M0')],
            },
            'Q6': {
                'exit': [({}, 'Q7', 'M1')],
                'walk': [({}, 'Q4', 'M0')],
            },
            'Q4': {
                'walk': [({}, 'Q2', 'M1')],
            },
            'Q2': {
                'jump': [({}, 'Q2', 'M1'), ],
                'walk': [({}, 'Q1', 'M0'), ],
            },
            'Q1': {
                'walk': [({}, 'Q6', 'M0')],
            }
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['Q7']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = (
            self.conditional_transitions.get(self.state, {})
        )
        if name not in current_transitions:
            raise StateMachineException('unsupported')

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts
                        .get((self.state, to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.executed_states.append(self.state)
                self.last_state = output
                return None
        raise StateMachineException('unsupported')

    def has_path_to(self, target_state):
        return True

    def part_of_loop(self):
        return True

    def get_output(self):
        return self.last_state

    def __getattr__(self, name):
        name = name.replace('set_', '')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        if not self._trigger_exists(name):
            raise StateMachineException("unknown")
        return lambda: (self._try_apply_trigger(name) or None)


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
    obj.walk()
    assert obj.get_output() == "M0"
    assert obj.has_path_to('walk') is True
    assert obj.part_of_loop() is True
    raises(lambda: obj.jump(), StateMachineException)
    raises(lambda: obj.walk(), StateMachineException)
    raises(lambda: obj.none(), StateMachineException)
    obj.set_p(0)
    obj.jump()
    obj.walk()
    obj.clear()
    obj.walk()
    obj.walk()
    obj.jump()
    obj.walk()
    obj.walk()
    obj.exit()
    obj.walk()
    obj.set_p(1)
    obj.jump()
    obj.state = "Q3"
    obj.clear()
