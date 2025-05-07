class MealyError(Exception):
    """Исключение для Mealy-автомата."""
    pass


class MealyMachine:
    """Mealy-конечный автомат по заданному графу."""

    def __init__(self):
        self.current_state = 'U3'
        self._steps = 0
        self._transitions = {
            'U3': {'crush': ('U3', 'A2'),
                   'file':  ('U7', 'A2'),
                   'slur':  ('U6', 'A1')},
            'U7': {'throw': ('U0', 'A1')},
            'U0': {'send':  ('U6', 'A1')},
            'U6': {'file':  ('U2', 'A1')},
            'U2': {'file':  ('U4', 'A1'),
                   'send':  ('U4', 'A0')},
            'U4': {'hoard': ('U5', 'A1'),
                   'mix':   ('U5', 'A1')},
            'U5': {'slur':  ('U3', 'A1'),
                   'hoard': ('U1', 'A1')},
            'U1': {'hoard': ('U4', 'A1')},
        }
        # алфавит входных символов
        self._alphabet = {
            inp
            for outs in self._transitions.values()
            for inp in outs
        }

    def run(self, inp: str) -> str:
        """
        Выполнить переход по входному слову inp.
        Если inp не в алфавите — MealyError('unknown').
        Если переход не поддерживается — MealyError('unsupported').
        """
        if inp not in self._alphabet:
            raise MealyError('unknown')
        mapping = self._transitions.get(self.current_state, {})
        if inp not in mapping:
            raise MealyError('unsupported')
        new_state, output = mapping[inp]
        self.current_state = new_state
        self._steps += 1
        return output

    def __getattr__(self, name: str):
        """
        Переадресация вызова obj.symbol() в obj.run('symbol').
        Позволяет вызывать методы по именам входных сигналов.
        """
        return lambda: self.run(name)

    def get_step(self) -> int:
        """Вернуть число успешно выполнённых переходов."""
        return self._steps

    def has_max_out_edges(self) -> bool:
        return len(self._transitions[self.current_state]) == 3


def main() -> MealyMachine:
    """Создать и вернуть настроенный MealyMachine."""
    return MealyMachine()


def _raises(fn, msg: str) -> bool:
    """
    Вспомогательная функция:
    возвращает True, если fn() бросает MealyError(msg).
    """
    try:
        fn()
    except MealyError as e:
        return str(e) == msg


def test():
    assert _raises(lambda: main().run('trim'), 'unknown')
    assert _raises(lambda: main().trim(), 'unknown')

    # валидный переход и счётчик
    m1 = main()
    assert m1.run('slur') == 'A1'
    assert m1.current_state == 'U6'
    assert m1.get_step() == 1

    # unsupported в U6
    assert _raises(lambda: m1.run('crush'), 'unsupported')

    # прямые переходы из U3
    m2 = main()
    assert m2.run('file') == 'A2'
    assert m2.run('throw') == 'A1'
    assert m2.run('send') == 'A1'
    assert m2.current_state == 'U6'

    # полный проход через U2→U4→U5→U1→U4
    m3 = main()
    assert m3.run('slur') == 'A1'
    assert m3.run('file') == 'A1'
    assert m3.run('send') == 'A0'
    assert m3.run('hoard') == 'A1'  # U4 → U5
    assert m3.run('hoard') == 'A1'  # U5 → U1
    assert m3.run('hoard') == 'A1'  # U1 → U4
    assert m3.current_state == 'U4'
    assert m3.get_step() == 6

    # проверка has_max_out_edges
    m4 = main()
    assert m4.has_max_out_edges()
    m4.current_state = 'U1'
    assert not m4.has_max_out_edges()
    m5 = main()
    m5._transitions.clear()
    # неизвестное состояние + getattr
    m6 = main()
    m6.current_state = 'X'
    assert _raises(lambda: m6.run('file'), 'unsupported')
    assert _raises(lambda: m6.file(), 'unsupported')
