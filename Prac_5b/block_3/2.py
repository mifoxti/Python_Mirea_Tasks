import random
import ast
import inspect


class Mutator(ast.NodeTransformer) :
    def visit_Constant(self, node) :
        if isinstance(node.value, int) or isinstance(node.value, float) :
            # �������� �������� ��������� ���������� �������
            node.value = random.uniform(-1000, 1000)  # ��������� �������� ��������� �����
        return node


def mutate_code(src) :
    tree = ast.parse(src)
    Mutator().visit(tree)
    return ast.unparse(tree)


def make_mutants(func, size) :
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1 :
        while mutant in mutants :
            mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1 :]


def distance(x1, y1, x2, y2) :
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def test_distance() :
    assert distance(0, 0, 3, 4) == 5.0
    assert distance(1, 2, 4, 6) == 5.0
    assert distance(0, 0, 0, 0) == 0.0


def mut_test(func, test, size=20) :
    survived = []
    mutants = make_mutants(func, size)
    for mutant in mutants :
        try :
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except :
            pass
    return survived


if __name__ == "__main__" :
    print("Testing original function:")
    test_distance()

    print("\nMutating and testing:")
    survived_mutants = mut_test(distance, test_distance)
    print("\nSurvived mutants:", survived_mutants)
