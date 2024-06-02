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
    a1, offset = parse(buffer, offset, 'float')
    a2_offset, offset = parse(buffer, offset, 'uint16')
    a2, _ = parse_b(buffer, a2_offset)
    a3, offset = parse(buffer, offset, 'double')
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_c(buffer, a4_offset)
    a5, offset = parse(buffer, offset, 'uint64')
    a6, offset = parse(buffer, offset, 'int16')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint16')
    b2, offset = parse(buffer, offset, 'int64')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint16')
    c2, offset = parse(buffer, offset, 'uint64')
    c3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse_d(buffer, adr_offset)
        c3.append(val)
    c4_offset, offset = parse(buffer, offset, 'uint32')
    c4, _ = parse_e(buffer, c4_offset)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint32')
    d2 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'uint8')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint64')
    e2 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'int16')
        e2.append(val)
    e3, offset = parse(buffer, offset, 'int8')
    e4 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int64')
        e4.append(val)
    e5, offset = parse(buffer, offset, 'int16')
    e6, offset = parse(buffer, offset, 'int64')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'YIRP\x91=T\xbe\x1e\x00\x80)_\x0f\xcc\x86\xc2\xbf\x89\x00\xc4\xa4M\x8c\x03^cL'
            b'\\\xf6\x0c\xfe\xb4\xf6t_\xb8D\x87\xa7N\x12\x8c-?.\xa21i\xf4\xb2\xcf'
            b"t\xc2\xd6\xef~&\xf2z\xe4x/\x13l_9'\xe5\xc6\xad\x9e\x15\xda[+\x06\xefX\xe6"
            b' \x1doJ\x01<r\xbb\x9a\xa9&\xe3\xc8\xbf\xf3;d\xa37%\x02s\xf3uM\xaa\x04\xc3'
            b'Fy\xaf\xf9%F\xe1\xf0O\xaa\xfa\xb1M\xd8Y`\x0c\xc7\x16t\x1e\xa9\xbe\xa9.\xb0Bc'
            b'\x8a:F\x1b\x18\x00\x16R\x10\xad\x0f\x02\x00\x00\x00(\x00>\x00\x00\x00'))
