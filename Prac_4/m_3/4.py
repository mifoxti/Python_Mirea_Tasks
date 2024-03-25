from first import Add, Mul, Num


class StackVisitor:
    def visit(self, node):
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise RuntimeError(f'No visit_{type(node).__name__} method')

    def visit_Num(self, node):
        return f'PUSH {node.value}'

    def visit_Add(self, node):
        return 'ADD'

    def visit_Mul(self, node):
        return 'MUL'


# Пример использования
ast = Add(Num(7), Mul(Num(3), Num(2)))
sv = StackVisitor()
for node in ast.left, ast.right.left, ast.right.right:
    print(sv.visit(node))
