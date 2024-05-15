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
    offset = 5
    a1, offset = parse(buffer, offset, 'uint64')
    a2, offset = parse(buffer, offset, 'uint16')
    a3_offset, offset = parse(buffer, offset, 'uint16')
    a3, _ = parse_b(buffer, a3_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint16')
    b2_offset, offset = parse(buffer, offset, 'uint16')
    b2, _ = parse_c(buffer, b2_offset)
    b3, offset = parse(buffer, offset, 'int32')
    b4, offset = parse(buffer, offset, 'int8')
    b5, offset = parse(buffer, offset, 'int16')
    b6 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        b6_char, adr_offset = parse(buffer, adr_offset, 'char')
        b6 += b6_char.decode()
    b8 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        b8.append(val)
    b7_offset, offset = parse(buffer, offset, 'uint16')
    b7, _ = parse_e(buffer, b7_offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b8, 'B8': b7}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int16')
    b3size, offset = parse(buffer, offset, 'uint16')
    b3offs, offset = parse(buffer, offset, 'uint32')
    c2 = []
    for _ in range(b3size):
        val, b3offs = parse_d(buffer, b3offs)
        c2.append(val)
    c3, offset = parse(buffer, offset, 'uint32')
    c4, offset = parse(buffer, offset, 'double')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint8')
    d2, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint16')
    e2, offset = parse(buffer, offset, 'int64')
    e3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        e3.append(val)
    e4, offset = parse(buffer, offset, 'uint64')
    e5, offset = parse(buffer, offset, 'double')
    e6, offset = parse(buffer, offset, 'uint32')
    e7, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4, 'E5': e5, 'E6': e6, 'E7': e7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main((b'ERNS\x06\x12 \xb61\x80\x8a\x84\x91\x03c\x00of=\x80\xa9ZQ?o[\xa0\xf9'
             b'8\x00\x02\x00\x00\x00\x11*\xaa\xba9?\xea\xd1V\xdb\xb3\xf5Lqv\x14\xc3F\xbf[%?'
             b'\x14\xcd\xf4\xbe\xb6\x03\xdc\xbc|\xf6p\xbd-kbz%\xda\x1a\x0b\x19\xf2\xcap'
             b';\x00\x00\x00\x04\x00\x00\x007\xf2L\xab]\xe7-1x?\x9c\x0f\xfcz\xf0\xc7'
             b'\x80^\xfe\x85\xc2\xbc\x1c\x92\xb7\x00\x1bw9)\x10\xa9\x86c\x00\x02'
             b'\x00/\x00\x03\x001\x00G')))
