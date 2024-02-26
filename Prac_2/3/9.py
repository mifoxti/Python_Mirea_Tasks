import itertools

print((lambda s: [(char, len(list(group))) for char, group in itertools.groupby(s)])(input()))
