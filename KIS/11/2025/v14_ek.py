class MooreException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class MealyAutomat:
    def __init__(self):
        self.state = 'H5'

        self.conditional_transitions = {
            'H5': {
                'merge': [({}, 'H5', 'j2')],
                'crawl': [({}, 'H4', 'j1')],
            },
            'H4': {
                'fetch': [({'d': 2}, 'H5', 'j2'),
                          ({'d': 1}, 'H1', 'j0'),
                          ({'d': 0}, 'H3', 'j3')],
            },
            'H1': {
                'drive': [({}, 'H7', 'j5')],
            },
            'H7': {
                'daub': [({}, 'H4', 'j1')],
                'fetch': [({}, 'H3', 'j3')],
            },
            'H3': {
                'fetch': [({}, 'H6', 'j1')],
            },
            'H6': {
                'fetch': [({'v': 1}, 'H3', 'j3'),
                          ({'v': 0}, 'H2', 'j4')],
            },
            'H2': {
                'sweep': [({}, 'H0', 'j2')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.last_output = None
        self.executed_methods = []

    def _trigger_exists(self, name):
        return any(name in transitions
                   for transitions in
                   self.conditional_transitions.values())

    def _try_apply_trigger(self, name):
        current_transitions = self.conditional_transitions.get(self.state, {})
        if name not in current_transitions:
            raise MooreException("unsupported")

        for conds, to_state, output in current_transitions[name]:
            if all(self.vars.get(k) == v for k, v in conds.items()):
                self.transition_counts[(self.state, to_state)] = (
                        self.transition_counts.get((self.state,
                                                    to_state), 0) + 1
                )
                self.state = to_state
                self.step_count += 1
                self.last_output = output
                return None
        raise MooreException("unsupported")

    def get_output(self):
        return self.last_output

    def has_max_out_edges(self):
        return False if self.state != 'H4' else True

    def store_var(self, name, value):
        self.vars[name] = value

    def seen_edge(self, from_state, to_state):
        return self.transition_counts.get((from_state, to_state), 0)

    def __getattr__(self, name):
        if not self._trigger_exists(name):
            raise MooreException("unknown")
        return lambda: self._try_apply_trigger(name)


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
    assert obj.state == 'H5'
    obj.merge()
    assert obj.get_output() == 'j2'
    obj.crawl()
    assert obj.has_max_out_edges()
    raises(lambda: obj.gone(), MooreException)
    raises(lambda: obj.fetch(), MooreException)
    raises(lambda: obj.sweep(), MooreException)
    obj.store_var('d', 2)
    obj.fetch()
    obj.crawl()
    obj.store_var('d', 1)
    obj.fetch()
    obj.drive()
    obj.daub()
    obj.store_var('d', 0)
    obj.fetch()
    obj.state = 'H7'
    obj.fetch()
    obj.fetch()
    obj.store_var('v', 1)
    obj.fetch()
    obj.fetch()
    obj.store_var('v', 0)
    obj.fetch()
    obj.sweep()
    assert obj.seen_edge('H2', 'H0')
