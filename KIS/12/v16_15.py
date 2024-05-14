from pprint import pprint
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
    offset = 4
    a1_offset, offset = parse(buffer, offset, 'uint32')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'uint8')
    a3_offset, offset = parse(buffer, offset, 'uint32')
    a3, _ = parse_d(buffer, a3_offset)
    a4, offset = parse_e(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b1 += (val.decode())
    b2, offset = parse(buffer, offset, 'uint64')
    b3 = []
    for _ in range(3):
        b2_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_c(buffer, b2_offset)
        b3.append(val)
    b4, offset = parse(buffer, offset, 'uint32')
    b5, offset = parse(buffer, offset, 'uint16')
    b6, offset = parse(buffer, offset, 'int32')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'int64')
    c3, offset = parse(buffer, offset, 'int16')
    c4 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int8')
        c4.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'double')
    d2, offset = parse(buffer, offset, 'uint64')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint16')
    e2, offset = parse(buffer, offset, 'uint64')
    e3, offset = parse(buffer, offset, 'uint64')
    e4, offset = parse(buffer, offset, 'float')
    e5, offset = parse(buffer, offset, 'int64')
    e6, offset = parse(buffer, offset, 'uint64')
    e7, offset = parse(buffer, offset, 'uint8')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'YKSV}\x00\x00\x00\xcd\x9f\x00\x00\x00\xa7\xec\xa9\xdb8^\xed\xf4E\x17j'
            b'\x1a$\xbc\xb9R%$x\xfc\xa0\xbc\xed\xf8\xcaox$\x88\xfd\x84/\xc0\x93\x99'
            b'\xb4\xefN0cyP3YL\xf5.E\x07\x006\x00\x00\x00\xa4\xfa\xc0_\xb5\xf9\x96\xe5\xe4'
            b'1\x06@\x05\xe7\xab\xef\x02\x00Q\x00\x00\x00\xa0\x04\xfa\x8c\xe2\xa7\xba'
            b'9w\xee:A3z/4\x02\x00g\x00\x00\x00\x1a\xb1\xb2\xbb\xb8\x97N\xb9\xb0\x8d0\xf1|'
            b'\xf6\x02\x004\x00\x8a S\xbe\x118@\r=\x00\x00\x00S\x00\x00\x00i\x00\x00'
            b"\x00\xaf\xf9}Pc'\xcd\xa8!\xc6\xackF(\xf7\xf7\xdd?\xd1\xe1\\\xf8\x18"
            b'\x90\xf6\x9c'))
