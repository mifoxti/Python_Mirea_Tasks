# module1.py
print("Module 1 is loaded.")

import module2

def function_module1():
    print("Function in Module 1")
    module2.function_module2()
