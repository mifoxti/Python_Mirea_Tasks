class MyHashTable:
    def __init__(self):
        self.table = []

    def __getitem__(self, key):
        for k, v in self.table:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                self.table[i] = (key, value)
                return
        self.table.append((key, value))

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                del self.table[i]
                return
        raise KeyError(key)

    def __len__(self):
        return len(self.table)

    def __iter__(self):
        return iter(self.table)

    def __contains__(self, key):
        for k, _ in self.table:
            if k == key:
                return True
        return False

    def keys(self):
        return [k for k, v in self.table]

    def values(self):
        return [v for k, v in self.table]

    def items(self):
        return self.table

# Тестирование

my_dict = MyHashTable()

my_dict['a'] = 1
my_dict['b'] = 2
assert my_dict['a'] == 1
assert my_dict['b'] == 2

assert len(my_dict) == 2

del my_dict['a']
assert 'a' not in my_dict

my_dict['c'] = 3
assert 'c' in my_dict
assert ('b', 2) in my_dict.items()

for key in my_dict:
    print(key)
