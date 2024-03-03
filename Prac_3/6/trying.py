import example_pkg.module1 as m1
import example_pkg.module2 as m2
import json

m1.print_module1()  # This is Module 1
m2.print_module2()  # This is Module 2

# Чтение данных из config.json
with open('example_pkg/data/config.json', 'r') as file:
    data = json.load(file)
    print(data)  # {'key': 'value'}
