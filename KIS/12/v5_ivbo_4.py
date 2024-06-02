from struct import *


# РАБОТАЕТ
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
    offset = 4
    a1, offset = parse(buffer, offset, 'int32')
    a2_offset, offset = parse(buffer, offset, 'uint32')
    a2, _ = parse_b(buffer, a2_offset)
    a3, offset = parse(buffer, offset, 'int64')
    a4, offset = parse_d(buffer, offset)
    a5, offset = parse_e(buffer, offset)
    a6, offset = parse(buffer, offset, 'int64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int64')
    b2, offset = parse(buffer, offset, 'int8')
    b3 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b3 += (val.decode())
    b4 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        b4_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_c(buffer, b4_offset)
        b4.append(val)
    b5, offset = parse(buffer, offset, 'uint32')
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'uint32')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'int8')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'double')
    d3, offset = parse(buffer, offset, 'int16')
    d4, offset = parse(buffer, offset, 'uint16')
    d5, offset = parse(buffer, offset, 'uint32')
    d6, offset = parse(buffer, offset, 'double')
    d7, offset = parse(buffer, offset, 'int16')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int8')
    e2, offset = parse(buffer, offset, 'uint32')
    e3, offset = parse(buffer, offset, 'int32')
    e4, offset = parse(buffer, offset, 'uint32')
    e5, offset = parse(buffer, offset, 'uint16')
    e6, offset = parse(buffer, offset, 'uint64')
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4, 'E5': e5, 'E6': e6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'VNW\xd6\xe0\xe4\x98\t\x00\x00\x00\x8c\xc0[k\xb7\x13\xaf\xfbC\x00\x03\x00\xa7'
            b'?\xe7\xcf\xe5\x1f\xa8\x00\xa8(\x01\x13W\x7f\xc0\x9f\xe8?\xe12D'
            b'\x04\x8a\xd4\x88\x0e\xf4H\xf5\xf5\xc0H\xfd\x83\xd1-\x9b#r\x05\xc4\x02\x03F<'
            b'\x0c7\xa9\xad\xc9\xc6<\x0fh\xec8\xf01cpywosu}O\x99\x19f\xf8\x1e\xa6'
            b'\x9e\xc2\xbc:\xf9L\xa8\xe3\xf1\x06a\xb2y\xb6\xb6//5\x0f\xc9\xa4\xecd\xb2'
            b'"\xb0\xecQ\x00\x00\x00X\x00\x00\x00a\x00\x00\x00j\x00\x00\x00s\xb7POz'
            b'\x1d\xbf\xa4\x07M\x00\x00\x00\x07\x00\x00\x00Q\x00\x04\x00\x00\x00|\xd9'
            b'\x110\x91\xc8\xc3\xe3'))
