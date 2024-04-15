import inspect
from mutator import mutate_code
import ast

def make_mutants(func, size):
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        while mutant in mutants:
            mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1:]

def mut_test(func, test, size=20):
    survived = []
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            pass
    return survived
