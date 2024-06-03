from struct import *


# РАБОТАЕТ
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
    a1, offset = parse(buffer, offset, 'int8')
    a2, offset = parse(buffer, offset, 'int16')
    a3, offset = parse_b(buffer, offset)
    a4, offset = parse(buffer, offset, 'int8')
    a5 = []
    for _ in range(3):
        b3_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_c(buffer, b3_offset)
        a5.append(val)
    a6 = ''
    for _ in range(8):
        val, offset = parse(buffer, offset, 'char')
        a6 += (val.decode())
    a7_offset, offset = parse(buffer, offset, 'uint16')
    a7, _ = parse_e(buffer, a7_offset)
    a8, offset = parse(buffer, offset, 'float')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2 = ''
    for _ in range(4):
        val, offset = parse(buffer, offset, 'char')
        b2 += (val.decode())
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'float')
    a7_offset, offset = parse(buffer, offset, 'uint16')
    c2, _ = parse_d(buffer, a7_offset)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int32')
    d2, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint32')
    e2, offset = parse(buffer, offset, 'uint64')
    e3, offset = parse(buffer, offset, 'uint32')
    e4, offset = parse(buffer, offset, 'int8')
    e5 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'double')
        e5.append(val)
    e6, offset = parse(buffer, offset, 'uint8')
    e7, offset = parse(buffer, offset, 'int16')
    e8, offset = parse(buffer, offset, 'uint8')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7, 'E8': e8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\xc3PRLZ\xfa\xad\xbf\xca\xbbG,\xcd2\x90xpbc\xa3\x000\x00>\x00Lakqitmvl\x00j'
            b"?>\xd6\x97\x98\xcc\xe0\xaf\xbe%\xff\x97\xbf\x0ev'\x00(e\x7f^G\xbf6"
            b'\x85\x19\xbf\x17\xc4\xab\x006vF7\xb5?R\x12h\xbf}y\xbd\x00D?\xe01\xef\xa2\xbf'
            b"~N\xbf\xd4\xa3:(\x0b6\xd4\xbf\xc4'\x82y\xff>\x08\xe1\xc5\x87\xd0\xf1J/@\xda="
            b'\x00U<\xaa\n?1\x00\x00\x00\x03\x00Rhz\xa4\xc6'))
