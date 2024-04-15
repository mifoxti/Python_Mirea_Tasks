import unittest


class TestRLE(unittest.TestCase):
    def test_encode_decode(self):
        data = b'AAABBBCCCDDDEEE'
        encoded_data = encode_rle(data)
        decoded_data = decode_rle(encoded_data)
        self.assertEqual(data, decoded_data)

    def test_empty_string(self):
        data = b''
        encoded_data = encode_rle(data)
        decoded_data = decode_rle(encoded_data)
        self.assertEqual(data, decoded_data)

    def test_single_character(self):
        data = b'A'
        encoded_data = encode_rle(data)
        decoded_data = decode_rle(encoded_data)
        self.assertEqual(data, decoded_data)


def encode_rle(data):
    encoded = bytes()
    count = 1
    last_char = data[0]
    for i in range(1, len(data)):
        if data[i] == last_char:
            count += 1
        else:
            encoded += bytes([last_char])
            encoded += bytes([count])
            count = 1
            last_char = data[i]
    encoded += bytes([last_char])
    encoded += bytes([count])
    return encoded


def decode_rle(data):
    decoded = bytes()
    i = 0
    while i < len(data):
        count = data[i]
        char = data[i + 1]
        decoded += bytes([char] * count)
        i += 2
    return decoded


if __name__ == '__main__':
    unittest.main()
