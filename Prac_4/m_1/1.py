class MyClass:
    def __init__(self):
        self.public_field = 1
        self._protected_field = 2
        self.__private_field = 3

def get_public_fields(obj):
    public_fields = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('_')]
    return public_fields

obj = MyClass()
public_fields = get_public_fields(obj)
print("Public fields:")
for field in public_fields:
    print(field)
