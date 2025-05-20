class FSMError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'g2'

        self.conditional_transitions = {
            'g2': {
                'click': [({}, 'g0', 'P1')],
                'link': [({}, 'g7', 'P1')],
            },
            'g0': {
                'link': [({}, 'g7', 'P0'), ],
            },
            'g7': {
                'begin': [({}, 'g6', 'P0')],
            },
            'g6': {
                'type': [({'d': 0}, 'g3', 'P0'),
                         ({'d': 1}, 'g1', 'P1'), ],
            },
            'g3': {
                'click': [({'p': 0}, 'g0', 'P1'),
                          ({'p': 1}, 'g1', 'P0'), ],
            },
            'g1': {
                'tread': [({}, 'g4', 'P1')],
            },
            'g4': {
                'type': [({}, 'g5', 'P0'), ],
            },
            'g5': {
                'link': [({'r': 0}, 'g3', 'P0'),
                         ({'r': 1}, 'g1', 'P1'), ],
            }
        }
        self.transition_counts = {}
        self.vars = {}
        self.executed_methods = set()
        self.step_count = 0
        self.last_output = None
        self.executed_states = ['g2']

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions
                   in self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = (
            self.conditional_transitions.get(self.state, {})
        )
        if name not in current_transitions:
            raise FSMError('unsupported')

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
                return output
        raise FSMError('unsupported')

    def has_max_in_edges(self):
        return True if self.state == 'g1' else False

    def seen_state(self, state):
        return self.executed_states.count(state)

    def has_path_to(self, to_state):
        return True if to_state != 'g2' else False

    def __getattr__(self, name):
        name = name.replace('run_', '')
        if len(name) == 1:
            def set_var(val):
                self.vars[name] = val
                return None

            return set_var
        if not self._trigger_exists(name):
            raise FSMError("unknown")
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
    obj.click()
    assert obj.has_path_to('g3')
    obj.link()
    obj.begin()
    raises(lambda: obj.type(), FSMError)
    raises(lambda: obj.begin(), FSMError)
    raises(lambda: obj.loh(), FSMError)
    assert obj.seen_state('g7') == 1
    obj.d(1)
    obj.type()
    assert obj.has_max_in_edges() is True
