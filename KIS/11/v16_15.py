class MealyError(Exception):
    pass


class Graph:
    __slots__ = ("state",)

    def __init__(
        self
    ):
        self.state = "A"

    def open(
        self
    ) -> int:
        match self.state:
            case "A":
                self.state = "B"
                return 0
            case "B":
                self.state = "F"
                return 2
            case "C":
                self.state = "G"
                return 4
            case "E":
                self.state = "C"
                return 6
            case "F":
                return 9
            case "G":
                self.state = "D"
                return 11
            case _:
                raise MealyError("open")

    def begin(
        self
    ) -> int:
        match self.state:
            case "F":
                self.state = "G"
                return 7
            case _:
                raise MealyError("begin")

    def dash(
        self
    ) -> int:
        match self.state:
            case "B":
                self.state = "C"
                return 1
            case "C":
                self.state = "D"
                return 3
            case "E":
                self.state = "F"
                return 5
            case "F":
                self.state = "C"
                return 8
            case "G":
                self.state = "H"
                return 10
            case _:
                raise MealyError("dash")


def ignore(call):
    try:
        call()
    except MealyError:
        return


def main() -> Graph:
    return Graph()


def test() -> None:
    g = main()
    g.state = 'A'
    assert g.open() == 0
    g = main()
    g.state = 'B'
    assert g.dash() == 1
    g = main()
    g.state = 'B'
    assert g.open() == 2
    g = main()
    g.state = 'C'
    assert g.dash() == 3
    g = main()
    g.state = 'C'
    assert g.open() == 4
    g = main()
    g.state = 'E'
    assert g.dash() == 5
    g = main()
    g.state = 'E'
    assert g.open() == 6
    g = main()
    g.state = 'F'
    assert g.begin() == 7
    g = main()
    g.state = 'F'
    assert g.dash() == 8
    g = main()
    g.state = 'F'
    assert g.open() == 9
    g = main()
    g.state = 'G'
    assert g.dash() == 10
    g = main()
    g.state = 'G'
    assert g.open() == 11
    g = main()
    g.state = 'D'
    ignore(g.open)
    g = main()
    g.state = 'A'
    ignore(g.begin)
    g = main()
    g.state = 'A'
    ignore(g.dash)
