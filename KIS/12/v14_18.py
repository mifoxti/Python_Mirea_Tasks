from struct import *


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
    a1_offset, offset = parse(buffer, offset, 'uint32')
    a1, _ = parse_b(buffer, a1_offset)
    a2_offset, offset = parse(buffer, offset, 'uint16')
    a2, _ = parse_f(buffer, a2_offset)
    a3 = ''
    for _ in range(6):
        val, offset = parse(buffer, offset, 'char')
        a3 += (val.decode())
    a4, offset = parse(buffer, offset, 'float')
    a5, offset = parse(buffer, offset, 'int32')
    a6, offset = parse(buffer, offset, 'int32')
    a7 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int8')
        a7.append(val)
    a8 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint32')
        a8.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1_offset, offset = parse(buffer, offset, 'uint16')
    b1, _ = parse_c(buffer, b1_offset)
    b2, offset = parse_d(buffer, offset)
    b3, offset = parse(buffer, offset, 'double')
    b4, offset = parse(buffer, offset, 'double')
    b5 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b5 += (val.decode())
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int32')
    c2, offset = parse(buffer, offset, 'uint8')
    c3, offset = parse(buffer, offset, 'uint64')
    c4, offset = parse(buffer, offset, 'uint64')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int8')
    d2, offset = parse_e(buffer, offset)
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'float')
    e2, offset = parse(buffer, offset, 'uint16')
    e3, offset = parse(buffer, offset, 'double')
    e4, offset = parse(buffer, offset, 'int64')
    e5, offset = parse(buffer, offset, 'int32')
    e6, offset = parse(buffer, offset, 'int32')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'int16')
    f2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_g(buffer, adr_offset)
        f2.append(val)
    return {'F1': f1, 'F2': f2}, offset


def parse_g(buffer, offset):
    g1, offset = parse(buffer, offset, 'uint16')
    g2, offset = parse(buffer, offset, 'int16')
    g3, offset = parse(buffer, offset, 'uint8')
    return {'G1': g1, 'G2': g2, 'G3': g3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'EGYK\xaf\x00\x00\x00P\x00\xaazbfmgu\xbfH\xb0\x1a_e6D!\x17E\xb95f\xc2'
        b"\xc5\xa7\x9a\xa6\xe9g'\xee\xc6FHx\xab\xc2\xcaX\xc2\xb2u\x83\x9f4\xc7i"
        b'\x17)s\x8a\xdb\x12Zn\xf1\xd4\xf5\xb6\xa2\xcei\xf5\xf2}\xc4qftdm\x006\x14\xbf'
        b')T\xb7\x80\xb0?\xc4\xc5\xe3\xc3W!P[\x87L\xc8\xa1\xb2\xf1\xafN\xd9\xfc'
        b'+\xc5\xf2\xb1\xae?\xd9F\xcb\xcb\xe2\x83\x98?\xe4\x0e\xb2\xe2qMV\x00\x00\x00'
        b'\x05\x00K\xbf\x95p;.\trX\xddv\xca\xf8d\x82\x8b:?"\x8f/$\xff]\x94T'
        b'\x08<\x88\xc9\xfc\xed\xc1Wo\xb3\x1e=\x00\x00\x00\x07\x00\x00\x00\x87')
from pprint import pprint

pprint(main(data))
