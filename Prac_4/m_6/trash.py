x = 5
y = 4
print((((y * 10) - (x if x >= 4 else 4)) - (y % 1 if x >= 1 else x % 2)) + (y if y > 1 else x - 2))