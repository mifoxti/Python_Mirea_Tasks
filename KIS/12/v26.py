from struct import *


def parse(buffer, offset, type, order='<'):
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
    offset = 3
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'int8')
    a3, offset = parse(buffer, offset, 'int64')
    a4 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'uint8')
        a4.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int32')
        b2.append(val)
    b3, offset = parse(buffer, offset, 'int32')
    b4, offset = parse_e(buffer, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        c1_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_d(buffer, c1_offset)
        c1.append(val)
    c2, offset = parse(buffer, offset, 'uint32')
    c3, offset = parse(buffer, offset, 'uint8')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int8')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'int64')
    d4, offset = parse(buffer, offset, 'int16')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int8')
    e2, offset = parse(buffer, offset, 'double')
    e3 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int32')
        e3.append(val)
    e4, offset = parse(buffer, offset, 'int32')
    e5, offset = parse(buffer, offset, 'double')
    e6, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4, 'E5': e5, 'E6': e6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'OHH\x03\x00\x00\x00\x96\x00\x00\x00\x02\x9b\xf2@\x11\xe4i\x8b-S]\x16\xcb'
            b'\x9bVWLQ\xc7\x1d\x1du%\x9a\xf2\xc7\xcb\x8d\xe79:\x01b\xb2j\x8d\xe1'
            b'\xbfU\x08\xdf}\x1dA\xc2\x13\x86#\xa9\xbc.:%\xc9;\x973\xaa\xe3A_n\x19\x89\x8c'
            b'c\x13\xb8\xc0\xb9re\x99*[@\xe1\xbf<d\x0f\x97\xcb\xbd\x9a\x0eX\xfeO\xffw\xfdP'
            b"R\x85\xb2\xcc\xbdQ7TK\xe3\xa2j\xa2\xf1\xe3\x10'\x00\x8f\x14\x92M\x9d\xe0"
            b'F\xe2\xdc\x18\xcf\xcc$Y\x18i3K:e~\x9a-\x96\xeebj\xf9f\x00\x00\x00v\x00'
            b'\x00\x00\x86\x00\x00\x00'))
