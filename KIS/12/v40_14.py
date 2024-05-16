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
    a1, offset = parse(buffer, offset, 'double')
    a2 = ''
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        a2 += (val.decode())
    a3, offset = parse_b(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int32')
    b2 = []
    for _ in range(3):
        b2_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_c(buffer, b2_offset)
        b2.append(val)
    b3, offset = parse(buffer, offset, 'uint32')
    b4, offset = parse(buffer, offset, 'uint32')
    b5, offset = parse_d(buffer, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int32')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'double')
    c3, offset = parse(buffer, offset, 'uint16')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint8')
    d2, offset = parse(buffer, offset, 'double')
    d3, offset = parse(buffer, offset, 'int8')
    d4, offset = parse(buffer, offset, 'float')
    d5, offset = parse(buffer, offset, 'int16')
    d6 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint8')
        d6.append(val)
    d7, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5, 'D6': d6, 'D7': d7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'LNIO<?\xd0\xc2-\xb2\x1d<lgq=\xd8*g\x00:\x00T\x00n\xa9u\n\xec\xbc\xdb\xa3'
            b'\xddg\xbf\xdbq\xbd;\x06U\xa0\xb3\xbf\n\xa9\x84\x1b\x8e\x84\xf8kV\xb6\xbe\x9f'
            b'K\x91e!\xe7\x14\xc4v\x99\x9d\xc6\x81\xf4\xee\xbd\x8b\xaf\x99?\xe9\x9a\xb4Iz'
            b'\x00\xa8\xeb\xb3\xcd\xb3=3/\xea\xe4\x81~J\x97\x02S+\xd5\xd7\xbf\xeb\x13\xa5'
            b'\tU\\Z\x9f\xd7+\x95t B\x1cS\xb9\x82\x8b\x17V\xdeRx\xd8\xbf\xe5{\xed\x97&'
            b'\xf2\x14g\xe5'))
