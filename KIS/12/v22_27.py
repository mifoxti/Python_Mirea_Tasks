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
    offset = 4
    a1 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        a1_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_b(buffer, a1_offset)
        a1.append(val)
    a2, offset = parse(buffer, offset, 'uint8')
    a3, offset = parse(buffer, offset, 'int32')
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_c(buffer, a4_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int32')
    b2, offset = parse(buffer, offset, 'int32')
    b3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint32')
        b3.append(val)
    b4, offset = parse(buffer, offset, 'float')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse_d(buffer, offset)
    c2, offset = parse(buffer, offset, 'int32')
    c3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        c3.append(val)
    c4, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int32')
        d1.append(val)
    d2 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'uint32')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'double')
    d4, offset = parse(buffer, offset, 'uint64')
    d5, offset = parse(buffer, offset, 'uint8')
    d6, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5, 'D6': d6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'KBC\xd7\x00\x00\x00\x02\x00\x00\x00KRon\x01b\x00]\xb4\xa5\xca^@\xd3\xb7r1'
 b'\xda;\x9c\xc3\x1ab\xb9\xae%\xab\xb7\x00\x03\x00\x13>\xda\x97\x89\x15'
 b'\x0eo\xa2\xfe_I\xf1Oz|\x17<O\xe6L3p\xa21\x00\x03\x00/=\xd9\x02p\x00'
 b'\x00\x00\x1f\x00\x00\x00;\x0bW\xd9Io+y\xdfj`\xd0\xc0\xe2\xbb\xfa}\xb8'
 b'\xa0\xdat\xbe\xfb\xdaQ7/\xb4z\xde5F\xa3\xf1??\xc1?\xcdch\xbc\x88\x05\x13\x86'
 b'{]\xbd\xc6p\xa1\t\x02OSB\xda\tl\x00\x00\x00\x05\x00\x00\x00SCs'))
