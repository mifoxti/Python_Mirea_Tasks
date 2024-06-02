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
    offset = 3
    a1, offset = parse(buffer, offset, 'uint32')
    a2, offset = parse(buffer, offset, 'uint8')
    a3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse_b(buffer, adr_offset)
        a3.append(val)
    a4 = ''
    for _ in range(4):
        val, offset = parse(buffer, offset, 'char')
        a4 += val.decode()
    a5, offset = parse(buffer, offset, 'int32')
    a6_offset, offset = parse(buffer, offset, 'uint16')
    a6, _ = parse_d(buffer, a6_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1 = ''
    for _ in range(7):
        val, offset = parse(buffer, offset, 'char')
        b1 += val.decode()
    b2, offset = parse(buffer, offset, 'uint32')
    b3, offset = parse(buffer, offset, 'uint32')
    b4, offset = parse(buffer, offset, 'uint8')
    b5, offset = parse_c(buffer, offset)
    b6, offset = parse(buffer, offset, 'int64')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint32')
    c2, offset = parse(buffer, offset, 'int64')
    c3, offset = parse(buffer, offset, 'int8')
    c4, offset = parse(buffer, offset, 'double')
    c5, offset = parse(buffer, offset, 'int64')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'uint8')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'int8')
    d3, offset = parse(buffer, offset, 'uint64')
    d4, offset = parse(buffer, offset, 'int32')
    d5, offset = parse(buffer, offset, 'float')
    d6, offset = parse(buffer, offset, 'uint64')
    d7, offset = parse(buffer, offset, 'uint64')
    return {'D1': d1, 'D2': d2, 'D4': d4, 'D5': d5,
            'D6': d6, 'D7': d7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'HWK\xffB\xed\xf3g\x02\x00\x00\x00\x18\x00psxo\xa2\xe2Cm\x82\x00hojjpemm'
            b'W<\xae\xc26\xc9\xc9\x92\xd0\x1fa\xff\xd8yxm\x9d\xb02\xa3ZH\x88\xcf'
            b'\xba\xeeU\xef\xbf}\xf2\x02Hh}\x9e\xbf3\xa1\xbbj\xdb\xd4S\xa0dfwcahl'
            b'\xb4t\x89;5\x83\x10GwS\x9d\xd8/\xf3\xd0\xc9\xddRdeB\xae0P\x86\x9dBc'
            b'\xe8\xbf\x83\x89\xf5\xb8r\xcau\xfe+b\\-\xe7\xcc\xd6r\xf1B\x19\xaf\xbd\xac'
            b'\xdek\xc6\xd0\x88]\xdd\x10I\x1a\xb5\xd0K\xc1>_G#\xe3\xe5\xcb\xee\xf0\xbb'
            b'\to|\x94\x9e[>'))
