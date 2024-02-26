user_input = input()
item_to_find = input()
print([i for i, item in enumerate(user_input) if item == item_to_find])
