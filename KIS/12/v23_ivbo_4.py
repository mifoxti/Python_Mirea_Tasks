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
    a1, offset = parse(buffer, offset, 'double')
    a2, offset = parse(buffer, offset, 'int8')
    a3_offset, offset = parse(buffer, offset, 'uint16')
    a3, _ = parse_b(buffer, a3_offset)
    a4, offset = parse_f(buffer, offset)
    a5, offset = parse_g(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint32')
    b2 = []
    for _ in range(2):
        b2_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_c(buffer, b2_offset)
        b2.append(val)
    b3, offset = parse(buffer, offset, 'uint32')
    b4, offset = parse(buffer, offset, 'int64')
    b5 = ''
    for _ in range(4):
        val, offset = parse(buffer, offset, 'char')
        b5 += (val.decode())
    b6_offset, offset = parse(buffer, offset, 'uint32')
    b6, _ = parse_e(buffer, b6_offset)
    b7, offset = parse(buffer, offset, 'uint16')
    b8, offset = parse(buffer, offset, 'int32')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint64')
    c2, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'double')
    d2, offset = parse(buffer, offset, 'int32')
    d3, offset = parse(buffer, offset, 'uint32')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint32')
    e2, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'int8')
    f2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        f2.append(val)
    f3, offset = parse(buffer, offset, 'double')
    return {'F1': f1, 'F2': f2, 'F3': f3}, offset


def parse_g(buffer, offset):
    g1, offset = parse(buffer, offset, 'float')
    g2 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'int8')
        g2.append(val)
    g3, offset = parse(buffer, offset, 'int8')
    g4, offset = parse(buffer, offset, 'float')
    g5, offset = parse(buffer, offset, 'int64')
    return {'G1': g1, 'G2': g2, 'G3': g3,
            'G4': g4, 'G5': g5}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'WTPK\xe9\x84\xac\x1eZ\x0b*\xeb\xbf\x81l\x00;\x02\x00\x8e\x00\x00\x00\xb6'
            b'\xb8\xb1q?D\xeb?L\xd6\xc7\xbe;K\xfe\x0f<\xbb\x8b\xe4\xd7\xa5\xbe\xa9\xbb'
            b'\x01\x07\xa1\xc4hl\xfb\xd2\xd7g\xb8\xc9\x8e!\xeeF\xc0\x9a\xf5\xa0\xe1?TO'
            b'\xc4>\x84\xf0\xf0\xd9Q\xa9E1\x16\x93\x07$\xc0\x92\x96\x89&7\xa0\xbf\r\xa3'
            b'\x97\xd5\x9a&w\x9dq\x0b`P\x05-X{\x9d\xf46\x00N\x00\x98*\xfa\x1d\x1a\xa8\x17]'
            b'_\xfa\xa4xaugqf\x00\x00\x00\x10\xbeN\xcf\xa5\x12Sz'))
