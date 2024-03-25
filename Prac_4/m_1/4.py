get_inheritance = lambda cls: ' -> '.join(cls.__name__ for cls in cls.__mro__)

print(get_inheritance(OSError))
