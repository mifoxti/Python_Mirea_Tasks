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
    offset = 4
    a1_offset, offset = parse(buffer, offset, 'uint16')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'uint16')
    a3, offset = parse_e(buffer, offset)
    a4, offset = parse(buffer, offset, 'uint16')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_c(buffer, a3_offset)
        b1.append(val)
    b2, offset = parse(buffer, offset, 'int64')
    b3_offset, offset = parse(buffer, offset, 'uint16')
    b3, _ = parse_d(buffer, b3_offset)
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'uint64')
    c3, offset = parse(buffer, offset, 'uint8')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'double')
    d2 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int64')
        d2.append(val)
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int16')
    e2 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint32')
        e2.append(val)
    e3, offset = parse(buffer, offset, 'float')
    return {'E1': e1, 'E2': e2, 'E3': e3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\xf9DGU\x00\x9e<\xce\x0fd\x9fA\x10Wk3\xc5\xdc>\x9f\xcd\x12?R\x13}\xee\xb5'
            b'\x88g5\xab\x00\x00\x05\x00\x00\x00\x1c\xbd\x97\x80\x82\xc3\x83D\xaa\x98'
            b')_\x00\x02\x00\x00\x000\t\x1c\xc9r\xfcsV\x82\x12Kg\x81\x19l\x02\xf3'
            b'<\x00\x08\x00\x00\x00A\xb9\xab\x17\xdd\xa5\xbd\xcb\x90\xf1\x00!\x002'
            b'\x00I\xbf\xda\x1ee\xb8#\x1cT\x04[mi\x7f%\xce\xe6\xe1\x84r\xc3\xb1\x00'
            b'k\x02S\x94\xe3\xf6\xb0\xc4\xf1}V\x802\xac\x89\xe0\xf76\xdb\xa5VZhr'
            b'\xfb\xe0\xdcq=~\xc0\xda\xa5\xe6y!/\x1d\xb6\x7f\xe4~\x00\x00\x00\x03\x00X'
            b'q\xe8\x04\xe5\xd5x$\xcb\x00^'))
