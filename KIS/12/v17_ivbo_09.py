from struct import *


# РАБОТАЕТ
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
    offset = 5
    a1, offset = parse(buffer, offset, 'uint64')
    a2, offset = parse(buffer, offset, 'int8')
    a3, offset = parse_b(buffer, offset)
    a4, offset = parse(buffer, offset, 'int8')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2, offset = parse(buffer, offset, 'int64')
    b3 = []
    for _ in range(3):
        b, offset = parse_c(buffer, offset)
        b3.append(b)
    b4 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'float')
        b4.append(val)
    b5, offset = parse(buffer, offset, 'uint8')
    b6_offset, offset = parse(buffer, offset, 'uint16')
    b6, _ = parse_d(buffer, b6_offset)
    b7, offset = parse(buffer, offset, 'int8')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5,
            'B6': b6, 'B7': b7}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int32')
    d2, offset = parse(buffer, offset, 'int16')
    d3, offset = parse(buffer, offset, 'int16')
    d4, offset = parse(buffer, offset, 'int64')
    d5, offset = parse(buffer, offset, 'int32')
    d6, offset = parse(buffer, offset, 'uint8')
    d7, offset = parse(buffer, offset, 'uint8')
    d8 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        d8.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7, 'D8': d8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'TUII\x9d\x98\x92\xecP*\xa3\xcc\x17\xfc4\xd8\xb0\\\x89\xab\xe2?\xc0\xe9eUYh'
            b'e\x9a\x02\x00\x00\x00U\x00\x00\x00\xa5\x9b\x05\x00\x00\x00]\x00\x00\x00'
            b'\t\r\x04\x00\x00\x00q\x00\x00\x00\xadC&\xe9l\xbe\x99S\xcd>;y&?'
            b'\xb2\xb3\x0e\xbf-\xb0o>7\x8f\x00n\xcd$\xe9\xa7\xbe\xada\t?)\xe4\xb2'
            b'\xbeO\xffu\xbe\x06!9\xbeG|-\xbf\xf4\xb6\x1b\xbf\xde\x9f\x88>\xd9!\x19?K\x83b'
            b'\xbf\x14 >\xbf\xe0@Zv>{\xe3,MJZ\xa6\xd98\x9c\xfbyn\xf0\xb2\xdc\x06\xbc'
            b'T\x889H\xe4\xee\xe6\xf7P5\x00\x10\xed\x07\x00\x00\x00\x81\x00'))
