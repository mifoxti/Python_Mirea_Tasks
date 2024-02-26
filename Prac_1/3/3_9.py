def fast_mul_gen(y):
    s = "def f(x):\n"
    s += "    result = 0\n"
    while y > 0:
        if y & 1 == 1:
            s += "    result = result + x\n"
        y >>= 1
        if y > 0:
            s += "    x = x + x\n"
    s += "    return result"
    return s


def test_fast_mul_gen():
    needed_str = """def f(x):
result = 0
result = result + x
x = x + x
result = result + x
x = x + x
result = result + x
x = x + x
result = result + x
return result
"""
    assert needed_str.strip() == fast_mul_gen(15).strip()


test_fast_mul_gen()