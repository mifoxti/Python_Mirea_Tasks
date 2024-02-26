def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16(x, y):
    x0 = x & 0xFF
    x1 = x >> 8
    y0 = y & 0xFF
    y1 = y >> 8

    res_lo = mul_bits(x0, y0, 8)
    res_mid = (mul_bits(x1, y0, 8) + mul_bits(x0, y1, 8)) << 8
    res_hi = mul_bits(x1, y1, 8) << 16

    return res_lo + res_mid + res_hi


def test_mul16():
    assert mul16(10, 20) == 200, "Test Case 1 Failed"

    assert mul16(0, 100) == 0, "Test Case 2 Failed"

    assert mul16(7, 1) == 7, "Test Case 3 Failed"

    assert mul16(32767, 32767) == 1073676289, "Test Case 4 Failed"

    print("Все тесты пройдены успешно!.")


# Run the test cases
test_mul16()
