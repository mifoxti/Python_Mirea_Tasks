class Num:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Num({self.value})'

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Add({self.left}, {self.right})'

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Mul({self.left}, {self.right})'

# Пример использования
ast = Add(Num(7), Mul(Num(3), Num(2)))
print(ast)  # Вывод: Add(Num(7), Mul(Num(3), Num(2)))
