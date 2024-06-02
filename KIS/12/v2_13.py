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
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_b(buffer, adr_offset)
        a1.append(val)
    a2_offset, offset = parse(buffer, offset, 'uint32')
    a2, _ = parse_c(buffer, a2_offset)
    a3, offset = parse(buffer, offset, 'int16')
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b1 += (val.decode())
    b2, offset = parse(buffer, offset, 'int32')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint32')
    c2_offset, offset = parse(buffer, offset, 'uint32')
    c2, _ = parse_d(buffer, c2_offset)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int32')
        d2.append(val)
    d3 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'int32')
        d3.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'~QGJ\x00\x03\x00\x00\x00\x16\x00\x00\x00\\I\xefezdchr\x00\x02'
            b'\x00\x00\x00\x10\x1cW\xf3\xff\x00\x02\x00\x00\x00\x12\x05\xb5\xf9g\x00\x02'
            b'\x00\x00\x00\x14+S\xc1\xc8>\xdd\x1a4p\x9c\x82\xf7\x9fP\xe8\xcb\x90\x07\x84X'
            b'\xb3\x02\xe0\xa6\xed\x15\xacD\xf0\xe5\xe7\x0b\xec\t\xc8_\xce\x7f!\x06'
            b'z\x9a\xae\x04\xa6\xf7+\x07\x00\x00\x004'))
