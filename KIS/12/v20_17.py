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
    a1, offset = parse(buffer, offset, 'int8')
    a2, offset = parse_b(buffer, offset)
    a3, offset = parse_c(buffer, offset)
    a4, offset = parse(buffer, offset, 'uint16')
    a5, offset = parse(buffer, offset, 'int64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint32')
    b2, offset = parse(buffer, offset, 'int32')
    b3, offset = parse(buffer, offset, 'uint16')
    b4 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b4 += (val.decode())
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_d(buffer, adr_offset)
        c1.append(val)
    c2, offset = parse(buffer, offset, 'float')
    c3, offset = parse_e(buffer, offset)
    c4, offset = parse(buffer, offset, 'int64')
    return {'C1': c1, 'C2': c2,
            'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'uint16')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int32')
        e1.append(val)
    e2, offset = parse(buffer, offset, 'int8')
    e3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        e3.append(val)
    e4, offset = parse(buffer, offset, 'int64')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\xfdVJXW\xd9\xfe2\xd2q\x18\xff2\x95B\xdd\x03\x00\x00\x00g\x00\x00\x00'
            b'\x03\x00\x00\x00j\x00\x00\x00\xddzb\xbf1r(\r\xddo\xdf{\xb4\xb08\x05\xdd]\rT'
            b"S@$&\x90\xbdC\xd2'\xb0e\x90\xbd\x08\x00\x85\x00\x00\x00\xea\x16\xedg~D\x93@O"
            b'\xc4n\x9f0\x8a1\xab\x03\xc8@\x10i\xaf\x99\xca\xa3%\xc7\xe4\xaa\xe8\xc3\x1fv'
            b'uk!\x7f\xe0$`CYw\xa6\xca\xac\x96\xce\x15\xbc\xf3y\xc9\xff\xac\x0b\xc1'
            b'\xdf\x99\xcb\xa4\xf9\x99\xb9P\xbc\xe8\rw\xbf\xb6\xc6\x18\xbf\xb2\xfe\xa2'
            b'\xbe\xa7+\x00?c\x05\xcd=\x0f[:\xbf\xf0\xf1\x90\xbe'))
