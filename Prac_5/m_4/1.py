import deal


@deal.pre(lambda a, b: b != 0)
@deal.ensure(lambda a, b, result: abs(result * b - a) < 1e-6)
def divide(a, b):
    return a / b
