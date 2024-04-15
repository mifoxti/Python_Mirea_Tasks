# encoding_decoding.py
def encode_rle(data):
    encoded = bytearray()
    count = 1
    last_char = data[0]
    for i in range(1, len(data)):
        if data[i] == last_char:
            count += 1
        else:
            encoded.extend([last_char, count])
            count = 1
            last_char = data[i]
    encoded.extend([last_char, count])
    return bytes(encoded)

def decode_rle(data):
    decoded = bytearray()
    i = 0
    while i < len(data):
        count = data[i]
        char = data[i + 1]
        decoded.extend([char]*count)
        i += 2
    return bytes(decoded)

def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# encoding_decoding.py
def triangle_type(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    if a == b == c:
        return "равносторонний"
    elif a == b or a == c or b == c:
        return "равнобедренный"
    else:
        return "разносторонний"

