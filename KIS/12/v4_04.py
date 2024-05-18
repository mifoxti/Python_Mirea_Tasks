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
    for _ in range(2):
        b2_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_b(buffer, b2_offset)
        a1.append(val)
    a2, offset = parse_c(buffer, offset)
    return {'A1': a1, 'A2': a2}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2, offset = parse(buffer, offset, 'int8')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2 = ''
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        c2 += (val.decode())
    c3, offset = parse(buffer, offset, 'uint16')
    c4 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'int64')
        c4.append(val)
    c5, offset = parse(buffer, offset, 'uint64')
    c6_offset, offset = parse(buffer, offset, 'uint16')
    c6, _ = parse_d(buffer, c6_offset)
    c7 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint32')
        c7.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5, 'C6': c6, 'C7': c7}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint16')
    d2, offset = parse(buffer, offset, 'uint64')
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\x9dPWWc\x00\x00\x00f\x00\x00\x00\xe3uc\x92Z;\xe4\xcb\xc3\x0f\x92\x15BY\x8dg'
            b'(r\x8e9!\xd3\xe2\xfb.\xe8\x1e\xed&RQ\xe2!\xb4FV\xbbc!\x8a\xca\xbd\x18C'
            b'k\x1e]:N\x8e\xc7vb\xca\x845\xf2t\x89c\xbe\xc6\xa8\x8a\xbc\x90\xef\x0e'
            b'\xa7\xbc\xfe\xec)S\xa5\xf7\x9ai\x00\x04\x00\x00\x00s\x00\x00\x00\xf7'
            b'Q\xd9\x0f\xf8w\xc4\xbfb\xbf%\x11\xba\x9e?&\t\x1f".-k\xba\xe8\x98|p\x99a'
            b'\x93\xd5\xa9'))
