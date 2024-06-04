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
    a1 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a1 += (val.decode())
    a2 = []
    for _ in range(8):
        b3_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_b(buffer, b3_offset)
        a2.append(val)
    a3, offset = parse(buffer, offset, 'uint32')
    a4, offset = parse_c(buffer, offset)
    a5, offset = parse(buffer, offset, 'uint32')
    a6, offset = parse_d(buffer, offset)
    a7, offset = parse(buffer, offset, 'int16')
    a8, offset = parse(buffer, offset, 'uint8')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2, offset = parse(buffer, offset, 'int8')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2, offset = parse(buffer, offset, 'uint16')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint32')
    d2_offset, offset = parse(buffer, offset, 'uint16')
    d2, _ = parse_e(buffer, d2_offset)
    d3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        d3.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint16')
        e1.append(val)
    e2, offset = parse(buffer, offset, 'uint8')
    return {'E1': e1, 'E2': e2}, offset


def main(data):
    result, _ = parse_a(data, 4)
    return result


from pprint import pprint

pprint(main(b'QKZR\x07\x00\x00\x00O\x00\x00\x00V\x00\x00\x00_\x00\x00\x00h\x00\x00\x00'
            b'q\x00\x00\x00z\x00\x00\x00\x83\x00\x00\x00\x8c\x00\x00\x00\x95\x00\x00\x00'
            b'f,)\x80\xd0\xeeD3\xc0\x0b\xbc?p~\xd8x\xb6;\xaf\xbd\xb0_\x9e\x00'
            b'\x05\x00\x00\x00\xa5\x00\x00\x006:\xafckejqxb\xea\x9d\x81\x8do;\xed?\x7f\x10'
            b'\xdd+\x08\xfdT\xbf\xbf\xdcZ\x95\x9c\xfe\x06\t\xef?e\xaeb\x1a/\xb6\xbc\xea'
            b'?\xa6\x80\xc5w\x1a\xd0\\\xef?\x93\xf0\xd5\x89\xaa\x8bq\xb5?\xba'
            b'\x10\x15\xea\x08\x96=\xc6\xbf\x15j\xafI\xbd\xa1\xa8\xe0\xbfv\x10\x8e\x0cLdf'
            b'X\xd5\xf8\xe0n\xa5'))
