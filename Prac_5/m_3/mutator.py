import ast
import random
import string


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            node.value = random.choice([random.randint(-100, 100), random.uniform(-100, 100)])
        elif isinstance(node.value, str):
            node.value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))
        return node

    def visit_BinOp(self, node):
        node.left = self.generic_visit(node.left)
        node.right = self.generic_visit(node.right)
        if isinstance(node.op, ast.Add):
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.Pow()])
        elif isinstance(node.op, ast.Sub):
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.Pow()])
        elif isinstance(node.op, ast.Mult):
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.Pow()])
        elif isinstance(node.op, ast.Div):
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.Pow()])
        elif isinstance(node.op, ast.Pow):
            node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.Pow()])
        return node


def mutate_code(src):
    tree = ast.parse(src)
    Mutator().visit(tree)
    return ast.unparse(tree)
