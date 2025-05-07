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

        # Граф переходов по переменным: {from_state: {method: [(условия, to_state, output)]}}
        self.conditional_transitions = {
            'v6': {
                'unite': [({'a': 2}, 'v1', 'W1')],
            },
            'v1': {
                'glare': [({}, 'v2', 'W1')],
                'bolt':  [({}, 'v3', 'W2')],
            },
            'v3': {
                'unite': [({}, 'v4', 'W2')],
            },
            'v4': {
                'fork': [({}, 'v0', 'W0')],
            },
        }

        self.transition_counts = {}
        self.vars = {}
        self.step_count = 0
        self.executed_methods = set()

    # Пример теста для ошибки: raises(lambda: automaton.go('clear'), MachineException)
    # Пример теста для успеха: assert automaton.go('lower') == 'T1'
    # Пример теста для несуществуещего пути: raises(lambda: automaton.go('none'), MachineException)
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
        self.step_count += 1
        self.state = next_state
        return output

    def seen_method(self, method_name):
        """Проверяет, выполнялся ли метод успешно ранее."""
        return method_name in self.executed_methods

    # Пример теста: assert automaton.reset() == 'reset'
    def reset(self):
        self.state = 'v6'
        self.step_count = 0
        return 'reset'

    # Пример теста: assert automaton.seen_edge('v6', 'v3') == 1
    def seen_edge(self, from_state, to_state):
        return self.transition_counts.get((from_state, to_state), 0)

    # Альтернативная реализация
    def has_max_in_edges1(self):
        in_counts = {}

        # Собираем все target_state из всех переходов
        for transitions in self.conditional_transitions.values():
            for action, variants in transitions.items():
                for (_, target, _) in variants:
                    in_counts[target] = in_counts.get(target, 0) + 1

        max_in = max(in_counts.values(), default=0)
        return in_counts.get(self.state, 0) == max_in

    # Пример теста: assert automaton.has_max_in_edges()
    def has_max_in_edges(self):
        in_counts = {}
        for from_state, transitions in self.transitions.items():
            for _, (to_state, _) in transitions.items():
                in_counts[to_state] = in_counts.get(to_state, 0) + 1
        max_in = max(in_counts.values(), default=0)
        return in_counts.get(self.state, 0) == max_in

    # Считает количество уникальных ВЕТВЕЙ
    # Пример теста: assert automaton.has_max_out_edges()
    def has_max_out_edges1(self):
        out_counts = {}
        for state, transitions in self.conditional_transitions.items():
            count = 0
            for action, variants in transitions.items():
                count += len(variants)
            out_counts[state] = count

        max_out = max(out_counts.values(), default=0)
        return out_counts.get(self.state, 0) == max_out

    # Считает количество уникальных ПЕРЕХОДОВ
    # Пример теста: assert automaton.has_max_out_edges()
    def has_max_out_edges(self):
        out_counts = {state: len(transitions)
                      for state, transitions in self.transitions.items()}
        max_out = max(out_counts.values(), default=0)
        return out_counts.get(self.state, 0) == max_out

    # Пример теста: assert automaton.get_step() == 1
    def get_step(self):
        return self.step_count

    # Пример теста: automaton.let_var('a', 2)
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

    # Альтернативный перехват несуществующих функций
    # def _trigger_exists(self, name):
    #     """Проверяет, существует ли триггер в любом состоянии автомата."""
    #     return any(name in transitions
    #                for transitions in
    #                self.conditional_transitions.values())
    #
    # def _try_apply_trigger(self, name):
    #     """Пытается применить триггер в текущем состоянии."""
    #     current_transitions = self.conditional_transitions.get(self.state, {})
    #     if name not in current_transitions:
    #         return 'unsupported'
    #
    #     for conds, to_state, output in current_transitions[name]:
    #         if all(self.vars.get(k) == v for k, v in conds.items()):
    #             self.transition_counts[(self.state, to_state)] = (
    #                     self.transition_counts.get((self.state,
    #                                                 to_state), 0) + 1
    #             )
    #             self.state = to_state
    #             self.step_count += 1
    #             return output
    #     return 'unsupported'
    #
    # def __getattr__(self, name):
    #     if not self._trigger_exists(name):
    #         return lambda: 'unknown'
    #     return lambda: self._try_apply_trigger(name)

def main():
    return MealyAutomat()


# Пример вспомогательной проверки на исключения
def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
        assert output is None


# Пример тестов
def test():
    obj = main()

    # Переходов ещё не было
    assert obj.get_step() == 0
    assert obj.has_max_out_edges() == False

    # Устанавливаем переменные
    obj.let_var('a', 2)
    obj.let_var('v', 1)  # переменная 'v' в примере может быть лишней

    # Пробуем выполнить несуществующий переход из текущего состояния
    try:
        obj.exit()
    except MachineException as e:
        assert e.message == 'unknown'

    # Выполняем переход по unite (из v6 → v1 при a=2)
    assert obj.unite() == 'W1'
    assert obj.get_step() == 1

    # Переход по glare (всегда возможен из v1)
    assert obj.glare() == 'W1'
    assert obj.get_step() == 2

    # Следующий unite не определён в v2 — ошибка
    try:
        obj.unite()
    except MachineException as e:
        assert e.message == 'unknown'  # unite не определён в состоянии v2

    # bolt возможен из v1, вернёмся в v1 и протестим
    obj.reset()
    obj.let_var('a', 2)
    assert obj.unite() == 'W1'  # v6 → v1
    assert obj.bolt() == 'W2'  # v1 → v3
    assert obj.get_step() == 2

    # unite в v3 — работает
    assert obj.unite() == 'W2'  # v3 → v4

    # Неизвестная команда
    try:
        obj.amble()
    except MachineException as e:
        assert e.message == 'unknown'

    # fork в v4 — работает
    assert obj.fork() == 'W0'

    # has_max_out_edges может быть использован где угодно
    assert obj.has_max_out_edges()

    print("Все тесты пройдены.")
