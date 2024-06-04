from struct import *


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
    a1, offset = parse(buffer, offset, 'uint32')
    a2_offset, offset = parse(buffer, offset, 'uint32')
    a2, _ = parse_b(buffer, a2_offset)
    a3, offset = parse(buffer, offset, 'uint32')
    a4, offset = parse(buffer, offset, 'float')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2, offset = parse(buffer, offset, 'float')
    b3, offset = parse(buffer, offset, 'float')
    b4, offset = parse(buffer, offset, 'int8')
    b5, offset = parse(buffer, offset, 'uint32')
    b6_offset, offset = parse(buffer, offset, 'uint16')
    b6, _ = parse_c(buffer, b6_offset)
    b7_offset, offset = parse(buffer, offset, 'uint32')
    b7, _ = parse_f(buffer, b7_offset)
    b8_offset, offset = parse(buffer, offset, 'uint32')
    b8, _ = parse_g(buffer, b8_offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_d(buffer, a3_offset)
        c1.append(val)
    c2, offset = parse(buffer, offset, 'uint64')
    c3 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int8')
        c3.append(val)
    c4, offset = parse_e(buffer, offset)
    c5, offset = parse(buffer, offset, 'uint32')
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2, offset = parse(buffer, offset, 'uint64')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int16')
    e2 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'int32')
        e2.append(val)
    return {'E1': e1, 'E2': e2}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'int64')
    f2, offset = parse(buffer, offset, 'uint32')
    f3, offset = parse(buffer, offset, 'int16')
    f4 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint16')
        f4.append(val)
    return {'F1': f1, 'F2': f2, 'F3': f3,
            'F4': f4}, offset


def parse_g(buffer, offset):
    g1 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int32')
        g1.append(val)
    g2, offset = parse(buffer, offset, 'uint8')
    g3, offset = parse(buffer, offset, 'int8')
    g4, offset = parse(buffer, offset, 'int8')
    g5, offset = parse(buffer, offset, 'int32')
    g6, offset = parse(buffer, offset, 'int8')
    g7, offset = parse(buffer, offset, 'int16')
    g8, offset = parse(buffer, offset, 'float')
    return {'G1': g1, 'G2': g2, 'G3': g3,
            'G4': g4, 'G5': g5, 'G6': g6,
            'G7': g7, 'G8': g8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'JXTU\x86?\x9b\x18\xa4\x00\x00\x00\xc2\xda\xe1\x08dn\xf3\xbe\xadH\x1d\xbf'
        b'\xd3\xe5\xcf\xed\xb1\xe6.\x9c#\xfe\xe1>\xa4&\xf7\xae\xef\xafA\xc9'
        b'\x14\x00\x00\x00 \x00\x00\x00\x02\x00\x00\x00,\x00\x00\x004 \xea\\'
        b'\xc3s\xc6\x08@\xdc\xa5\xde\xd9\xa7b\x03\xee\xba\xf6\xfe\r\x02\x94~'
        b'\xca\x1b\xfbQ2\x08~m\x93M\xea[\x01\xbe\x8b\x98p\x11r\x8c$\xd1Y\x83'
        b'\xfa\xc85\x1c~TZ\x96p\xbd\xd1s\xd8\xba(\xbb\xbb\xbd\xbb\xd5|i\xf5\x83'
        b'\xc7\xa4\xc3\xc1\x15E7\x99\xf8\xd91:\x12k\xfd\x13\xd5Z\x15&\x0c<\xb7\xc6'
        b'}\xa9\x98\xaen}a?{\x94\x0b\xdc \xbfs\xf9\x1a\xbf\x9a\xf8\xa1\xceT4'
        b'\x00f\x00\x00\x00z\x00\x00\x00')
from pprint import pprint

pprint(main(data))
