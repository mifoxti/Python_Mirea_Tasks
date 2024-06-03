from struct import *


def parse(buffer, offset, type, order='>'):
    pattern = {
        'float': 'f',
        'double': 'd',
        'char': 'c',
        'int8': 'b',
        'uint8': 'B',
        'int16': 'h',
        'uint16': 'H',
        'int32': 'i',
        'uint32': 'I',
        'int64': 'q',
        'uint64': 'Q'
    }[type]
    size = calcsize(order + pattern)
    value = unpack_from(order + pattern, buffer, offset)[0]
    return value, offset + size


def parse_a(buffer, offset):
    offset = 5
    a1_offset, offset = parse(buffer, offset, 'uint32')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'uint16')
    return {'A1': a1, 'A2': a2}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2, offset = parse(buffer, offset, 'int32')
    b3, offset = parse(buffer, offset, 'float')
    b4 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_c(buffer, a3_offset)
        b4.append(val)
    b5, offset = parse(buffer, offset, 'uint16')
    b6_offset, offset = parse(buffer, offset, 'uint16')
    b6, _ = parse_d(buffer, b6_offset)
    b7, offset = parse(buffer, offset, 'uint32')
    return {'B1': b1, 'B2': b2,
            'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6,
            'B7': b7}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'uint8')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'uint32')
    c3, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    c1 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint16')
        c1.append(val)
    c2 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'uint8')
        c2.append(val)
    return {'D1': c1, 'D2': c2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'EQTV\x81\x00\x00\x00<\xf5\xdaL\xc4zI\xee\xff2w\xbex\xb6\x93\x9b\xd9n\xeb\x89'
            b'\xb0\xc6\x06\xbf;;\xa4\x00\x00\x00\x0b\x00\x00\x00\x17\xe1\x03\xe7\x99\xf1'
            b'N\x08\x19)\xe3M?\xd1\x89\xd9\x94}?\xd8\xcb\xf91\xc73t\xe0\xd3`\xfb\xbfQ_\x07'
            b'\x00\x02\x00#\xa1\x1b\x00+\x92\xc2\x0eW'))
