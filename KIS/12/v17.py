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


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int8')
    d2, offset = parse(buffer, offset, 'int16')
    return {'D1': d1, 'D2': d2}, offset


def parse_c(buffer, offset):
    c1, offset = parse_d(buffer, offset)
    c2, offset = parse(buffer, offset, 'float')
    c3 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        c3.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_e(buffer, offset):
    e1 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint16')
        e1.append(val)
    e2, offset = parse(buffer, offset, 'int16')
    e3, offset = parse(buffer, offset, 'uint16')
    e4, offset = parse(buffer, offset, 'uint64')
    e5, offset = parse(buffer, offset, 'uint8')
    e6, offset = parse(buffer, offset, 'uint8')
    e7, offset = parse(buffer, offset, 'uint8')
    e8, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7, 'E8': e8}, offset


def parse_b(buffer, offset):
    b1 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        b1_char, adr_offset = parse(buffer, adr_offset, 'char')
        b1 += b1_char.decode()
    b2, offset = parse(buffer, offset, 'int8')
    return {'B1': b1, 'B2': b2}, offset


def parse_a(buffer, offset):
    offset = 3
    a1_offset, offset = parse(buffer, offset, 'uint16')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse_c(buffer, offset)
    a3, offset = parse(buffer, offset, 'double')
    a4, offset = parse(buffer, offset, 'double')
    a5, offset = parse(buffer, offset, 'int32')
    a6 = []
    for _ in range(3):
        e, offset = parse_e(buffer, offset)  # Parse structure E
        a6.append(e)

    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5, 'A6': a6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'VKPv\x00,\x1bT\xd6j\x8f>yn\x8aR-\x11\xc2l\xe0\xbf\x00\t\xd4\xc2P\x8c'
           b'\x8d\xbfK\x89\xb9\x8e!CB\xc4\x91\t\xe7\xfe6\xe0\x01;Fu\xb9N\x00wf\x83\xf9V'
           b'Qq\x82\xd8\x1cc1%\xa2\x0b\x1e=\xf7AR\xf0\xc7\x0f\xa0w\xfd\xe9\xb5*'
           b'\x01\xdc\xc2Dx\xeb\x11"\xff\xa5\xfd+p!\x83>\x9e\r\xf5\xd8(\xbb\xb4\t'
           b'\xa5\x97\xa04\xceT8M\xd0\xa0\x86hst\x03\x00\x00\x00s\x00\xda'))
