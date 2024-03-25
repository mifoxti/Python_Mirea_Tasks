''' В Python порядок наследования очень важен, и нельзя множественно наследовать от двух классов, если один из них наследуется от другого.
 В нашем случае класс C наследует и от A, и от B, при этом B сам наследует от A.
 Это приводит к проблеме с множественным наследованием (diamond inheritance problem).'''

# Вот несколько возможных вариантов исправления:

# Используйте только один родительский класс:

class A:
    pass

class B(A):
    pass

class C(B):
    pass


# Измените структуру наследования:

class A:
    pass

class B(A):
    pass

class C(A):
    pass
