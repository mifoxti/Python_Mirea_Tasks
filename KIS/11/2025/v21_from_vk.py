class MooreError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'B1'

        self.conditional_transitions = {
            'B1': {
                'step': [({}, 'B5', 'S1')],
                'shift': [({}, 'B0', 'S0')],
            },
            'B5': {
                'shift': [({}, 'B2', 'S1')],
                'step': [({}, 'B3', 'S0')],
            },
            'B2': {
                'step': [({}, 'B0', 'S0')],
            },
            'B0': {
                'sit': [({}, 'B4', 'S0')],
                'crawl': [({}, 'B1', 'S0')],
            },
            'B4': {
                'sit': [({'r': 0}, 'B6', 'S1'),
                        ({'r': 1}, 'B3', 'S0')],
            },
            'B3': {
                'sit': [({}, 'B6', 'S1')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = set()
        self.method_call_counts = {}
        self.executed_states = ['B1']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise MooreError("unsupported")

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.last_output = output
                self.executed_states.append(to_state)
                return None
        raise MooreError("unsupported")

    def has_path_to(self, path):
        paths = {
            'B1': ['B1', 'B5', 'B2', 'B0', 'B4', 'B3', 'B6'],
            'B5': ['B1', 'B5', 'B2', 'B0', 'B4', 'B3', 'B6'],
            'B2': ['B1', 'B5', 'B2', 'B0', 'B4', 'B3', 'B6'],
            'B0': ['B1', 'B5', 'B2', 'B0', 'B4', 'B3', 'B6'],
            'B4': ['B3', 'B6'],
            'B3': ['B6'],
            'B6': [],
        }
        return True if path in paths[self.state] else False

    def get_output(self):
        return self.last_output

    def part_of_loop(self):
        return True if self.state in ['B1', 'B5',
                                      'B2', 'B0'] else False

    def __getattr__(self, name):
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        if not self._trigger_exists(name):
            raise MooreError("unknown")
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
    obj.step()
    assert obj.part_of_loop() is True
    assert obj.get_output() == 'S1'
    assert obj.has_path_to('B1') is True
    obj.shift()
    obj.step()
    obj.crawl()
    obj.shift()
    obj.sit()
    raises(lambda: obj.sit(), MooreError)
    raises(lambda: obj.step(), MooreError)
    raises(lambda: obj.none(), MooreError)
    obj.r(1)
    obj.sit()
    obj.sit()
    obj.state = 'B4'
    obj.r(0)
    obj.sit()
    obj.state = 'B5'
    obj.step()
