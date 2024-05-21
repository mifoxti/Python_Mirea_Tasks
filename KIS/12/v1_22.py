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
    a1, offset = parse(buffer, offset, 'float')
    a2, offset = parse(buffer, offset, 'int32')
    a3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_b(buffer, adr_offset)
        a3.append(val)
    a4, offset = parse_c(buffer, offset)
    a5, offset = parse(buffer, offset, 'uint8')
    a6, offset = parse(buffer, offset, 'int8')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1 = ''
    for _ in range(3):
        val, offset = parse(buffer, offset, 'char')
        b1 += (val.decode())
    b2, offset = parse(buffer, offset, 'int8')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse_d(buffer, offset)
    c2, offset = parse(buffer, offset, 'uint8')
    c3, offset = parse(buffer, offset, 'uint8')
    c4, offset = parse(buffer, offset, 'int16')
    c5, offset = parse(buffer, offset, 'double')
    c6, offset = parse(buffer, offset, 'int8')
    c7, offset = parse_e(buffer, offset)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6, 'C7': c7}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2, offset = parse(buffer, offset, 'uint64')
    d3, offset = parse(buffer, offset, 'uint16')
    d4, offset = parse(buffer, offset, 'uint16')
    d5 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'float')
        d5.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int8')
    e2, offset = parse(buffer, offset, 'uint32')
    e3, offset = parse(buffer, offset, 'int64')
    e4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        e4.append(val)
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'BAZO<\xad\x9b\xd8\xe3}\xe6?\x00\x03\x00\x00\x00\\?\n\xe2\xc3\x1a\x14'
 b'\xf4fI\xc00\xaa\xc3\xb0\x99\xfa>\x17\xde(\xbe\x04\x03Y\xbc\xc1\xd1N\xbd\xef'
 b'oR?\x18\xb6<<\x1aZI\x19\xe1c\xf7\xbf\xeae\x9f\xea\x9d\x06p{\xfb\x06:~8'
 b'{\x0c\xafi\x96h\xe4:\x00\x00\x00\x06\x00h\xc4{pba\xfawxb\xe2sfm\xcc'
 b'\x1e(\x86\xf2?^\xc1\x98j\x84\xa5\xc1'))
