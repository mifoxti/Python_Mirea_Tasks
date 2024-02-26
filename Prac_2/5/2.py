def encode_val(k, t, value):
    result = 0
    for i in range(k):
        result |= ((value >> i) & 1) << (3 * i)
        result |= ((value >> i) & 1) << (3 * i + 1)
        result |= ((value >> i) & 1) << (3 * i + 2)
    return result


def decode_val(k, t, encoded_value):
    decoded_value = 0
    for i in range(k):
        decoded_value |= ((encoded_value >> (3 * i + 1)) & 1) << i
    return decoded_value


def correct_and_decode(k, t, values):
    corrected_values = [decode_val(k, t, value) for value in values]
    return corrected_values


encoded_message = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928,
                   2064407, 6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455,
                   1831360, 1936903, 2067967, 2068456]
decoded_message = correct_and_decode(8, 3, encoded_message)

print("Закодированный массив:", encoded_message)
print("Декодированный и скорректированный массив:", decoded_message)
