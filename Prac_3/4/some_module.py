# some_module.py
def func1():
    print("Function 1")


def func2():
    print("Function 2")


def func3():
    print("Function 3")


# Определите __all__, чтобы управлять экспортом при использовании *
__all__ = ['func1', 'func2']
