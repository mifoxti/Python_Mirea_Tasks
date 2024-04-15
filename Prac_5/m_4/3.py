import deal


@deal.has()
class MyClass:
    def __init__(self, x):
        self.x = x

    @deal.ensure(lambda self, result: result > 0)
    def double(self):
        return self.x * 2
