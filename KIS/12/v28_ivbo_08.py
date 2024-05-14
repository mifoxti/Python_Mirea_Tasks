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
    a1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_b(buffer, adr_offset)
        a1.append(val)
    a2, offset = parse_c(buffer, offset)
    a3, offset = parse(buffer, offset, 'float')
    a4, offset = parse_d(buffer, offset)
    a5, offset = parse(buffer, offset, 'int64')
    a6 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'uint32')
        a6.append(val)
    a7 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        a7.append(val)
    a8, offset = parse(buffer, offset, 'uint32')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int32')
    b2 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b2 += (val.decode())
    b3, offset = parse(buffer, offset, 'uint16')
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint64')
    c2, offset = parse(buffer, offset, 'float')
    c3, offset = parse(buffer, offset, 'uint64')
    c4, offset = parse(buffer, offset, 'uint64')
    return {'C1': c1, 'C2': c2,
            'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1_offset, offset = parse(buffer, offset, 'uint32')
    d1, _ = parse_e(buffer, d1_offset)
    d2, offset = parse(buffer, offset, 'int32')
    d3, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint32')
    e2, offset = parse(buffer, offset, 'float')
    return {'E1': e1, 'E2': e2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'TCH\xa0\x05\x00f\x00\x00\x00(f$\x13-\x11\xa3\x03K\xd8\xb5\xbd\x12\xdc'
            b'\xce\xcd\xe7\xb7\xcc\x8f\xd3\xcdn"jw\xd8\xcdYZR?\xa2\x00\x00\x00\x84\xec'
            b"%\xba1\xf9f%7\xfe[\xa6\x9a!\x95\xc7\x96T'\x9fw\xe9\xa8\x80\xbf8:\xeb.\x06"
            b'\x00\xaa\x00\x00\x00\x99z\x99\xadxgbvtyovnszkpotui+\xd7C\xe3\x03\x00'
            b'U\x00\x00\x00)i\xd6\xb0\x1c\xf6\x04\x00X\x00\x00\x00h\x1a\xf7\t\x97|\x04\x00'
            b'\\\x00\x00\x00\xbb7\x102\x0b\xce\x02\x00`\x00\x00\x00+\xdaW\x81'
            b'\xbf\x04\x04\x00b\x00\x00\x008\xc0t\xf7\xc0f\x17\xfe\xc7\xbdp"\x01S\r-'))
