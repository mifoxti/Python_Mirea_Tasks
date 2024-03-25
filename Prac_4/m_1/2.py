class MyClass:
    def method1(self):
        print("Method 1 called")

    def method2(self):
        print("Method 2 called")

def call_method(obj, method_name):
    method = getattr(obj, method_name, None)
    if method:
        method()
    else:
        print(f"Method '{method_name}' not found in class.")

# Создаем объект класса
obj = MyClass()

# Имя метода, который мы хотим вызвать
method_to_call = "method1"

# Вызываем метод
call_method(obj, method_to_call)
