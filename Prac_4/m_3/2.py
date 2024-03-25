from first import Num, Mul, Add

class PrintVisitor:
    def visit(self, node):
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise RuntimeError(f'No visit_{type(node).__name__} method')

    def visit_Num(self, node):
        return str(node.value)

    def visit_Add(self, node):
        return f'({self.visit(node.left)} + {self.visit(node.right)})'

    def visit_Mul(self, node):
        return f'({self.visit(node.left)} * {self.visit(node.right)})'

# Пример использования
ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
print(pv.visit(ast))  # Вывод: (7 + (3 * 2))
