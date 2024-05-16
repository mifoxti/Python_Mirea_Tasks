from pprint import pprint
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
    offset = 3
    b3size, offset = parse(buffer, offset, 'uint32')
    b3offs, offset = parse(buffer, offset, 'uint32')
    a1 = []
    for _ in range(b3size):
        val, b3offs = parse_b(buffer, b3offs)
        a1.append(val)
    a2 = []
    for _ in range(3):
        val, offset = parse_d(buffer, offset)
        a2.append(val)
    a3, offset = parse_e(buffer, offset)
    a4, offset = parse(buffer, offset, 'uint32')
    a5, offset = parse(buffer, offset, 'int32')
    a6 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'int32')
        a6.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4, 'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint64')
    b2, offset = parse(buffer, offset, 'uint16')
    b3, offset = parse(buffer, offset, 'uint8')
    b4, offset = parse_c(buffer, offset)
    b5, offset = parse(buffer, offset, 'uint32')
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2, offset = parse(buffer, offset, 'int32')
    c3, offset = parse(buffer, offset, 'uint64')
    c4, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'int32')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'uint16')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'int16')
        e1.append(val)
    e2, offset = parse(buffer, offset, 'uint8')
    e3, offset = parse(buffer, offset, 'uint16')
    e4, offset = parse(buffer, offset, 'uint16')
    e5, offset = parse(buffer, offset, 'int64')
    e6, offset = parse(buffer, offset, 'int8')
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4, 'E5': e5, 'E6': e6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'UPZ\x00\x00\x00\x02\x00\x00\x00g{\nqq\x13\n\xdbq\xd6\x0b_\x14\xbf'
            b"\x17\xe7\xbbc\x9b\xd9\x80\xf3\xab_\x8f'8\xf4\xea\xab0\xe1\x06W\xe7s\xdf\x0e"
            b'j\xfd\x06\x86\x15o]z\xe7\x0e\xd2\xcf\xb0<Q\xcf>\xc4Y\t\xe7\xd3\x8f\r'
            b'\x07\x10\xa3\xd3\x7f\x05u\x03\x07\xaa\x16G\xf5\xb2nUk\x19O\xb2\x0f_@\xc4'
            b'\xae\x92e:\x92\xf3\xc8f\xb0@\x80\x83Bg\xcaj\xef\xd8\xa3\xb4%\xc2s\xb3'
            b'\xe4\x9e\xea\x07>\x1f\xd8e\x9c\x17m\x10\xea\xf9\xda\x85\xc3{\xff\x8f'
            b',\xb59\xd7\xfd\x93\xb3\xfb\xb4\x00\xcc\x181\xf60[3O\x84\x92\xda\x07!'))
