import random
import ast
import inspect

class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, int) or isinstance(node.value, float):
            node.value = random.uniform(-1000, 1000)  # Генерация случайной константы
        return node

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            node.op = random.choice([ast.Sub(), ast.Mult(), ast.Div()])  # Замена операции сложения случайной бинарной операцией
        elif isinstance(node.op, ast.Sub):
            node.op = random.choice([ast.Add(), ast.Mult(), ast.Div()])
        return node

def mutate_code(src):
    tree = ast.parse(src)
    Mutator().visit(tree)
    return ast.unparse(tree)

def make_mutants(func, size):
    src = inspect.getsource(func)
    mutants = set()
    for _ in range(size):
        mutant = mutate_code(src)
        mutants.add(mutant)
    return [ast.fix_missing_locations(ast.parse(m)) for m in mutants]

def sort_list(arr):
    arr.sort()
    return arr

def test_sort_list():
    assert sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def mut_test(func, test, size=20):
    survived = []
    mutants = make_mutants(func, size)
    for mutant_ast in mutants:
        try:
            mutant_code = compile(mutant_ast, filename=inspect.getsourcefile(func), mode='exec')
            exec(mutant_code, globals())
            test()
            survived.append(mutant_ast)
        except AssertionError:
            pass
        except Exception as e:
            pass
    return survived

if __name__ == "__main__":
    print("Testing original function:")
    test_sort_list()

    print("\nMutating and testing:")
    survived_mutants = mut_test(sort_list, test_sort_list)
    print("\nSurvived mutants:", survived_mutants)