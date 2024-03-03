# main.py
from some_module import GLOBAL_VAR

def update_global_var(value):
    from some_module import GLOBAL_VAR
    GLOBAL_VAR = value
    print("Inside update_global_var:", GLOBAL_VAR)

print("Before update_global_var:", GLOBAL_VAR)
update_global_var(42)
print("After update_global_var:", GLOBAL_VAR)