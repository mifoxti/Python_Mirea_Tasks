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
    a1, offset = parse(buffer, offset, 'double')
    a2, offset = parse_b(buffer, offset)
    a3, offset = parse(buffer, offset, 'uint8')
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_g(buffer, a4_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int8')
    b2, offset = parse(buffer, offset, 'int8')
    b3_offset, offset = parse(buffer, offset, 'uint32')
    b3, _ = parse_c(buffer, b3_offset)
    b4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b4.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int64')
    c2, offset = parse(buffer, offset, 'int64')
    c3, offset = parse(buffer, offset, 'int8')
    c4 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        c4_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_d(buffer, c4_offset)
        c4.append(val)
    c5, offset = parse(buffer, offset, 'uint32')
    c6, offset = parse_e(buffer, offset)
    b3_offset, offset = parse(buffer, offset, 'uint32')
    b3, _ = parse_f(buffer, b3_offset)
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5, 'C6': c6, 'C7': b3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int8')
    d2, offset = parse(buffer, offset, 'uint8')
    d3, offset = parse(buffer, offset, 'uint16')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int32')
        e1.append(val)
    e2, offset = parse(buffer, offset, 'uint16')
    e3 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'double')
        e3.append(val)
    e4, offset = parse(buffer, offset, 'uint64')
    e5, offset = parse(buffer, offset, 'double')
    e6, offset = parse(buffer, offset, 'double')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'uint8')
    f2, offset = parse(buffer, offset, 'double')
    return {'F1': f1, 'F2': f2}, offset


def parse_g(buffer, offset):
    g1, offset = parse(buffer, offset, 'uint16')
    g2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        g2.append(val)
    g3, offset = parse(buffer, offset, 'float')
    return {'G1': g1, 'G2': g2, 'G3': g3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'AIE\x90\xbf\xd6\x99\xa6\xb6gi\xa4\xb6^\x00\x00\x00>\x00\x00\x00\x03\x00\x00'
            b'\x00\x99\xe1\x00\xa0\xc2jM$\xe9\xffk\xacI}\xf4\xa4\xfa\xa6\x16'
            b'\xe1\x00\x1d\x00!\x00%\x00)P?\xed\xdb.\xdclH"*\x03$\x91\x895\x92Z\x99\x0f'
            b'\xbe\x9e\xaf$D=z\x00\x04\x00-!\tPM|3\xab\xda\x1bO\x8fr\x1d\xaa\xc9\x8b"'
            b'57\xbd\x13GU\xb0\r\x9a?\xe0\xfc\x04\xa5\x10\xa8\x84\xbf\xdd\xed]P\xb3V'
            b'\xbca\xfb\xa1\xfa\xff\x89\xed}?\xe4E\x04W\xc8\xf4 \xbf\xdd\x92\xc0?b\x99'
            b"\xe8\x00\x00\x005t\xf90\xa0\xa7\x81\x99'\x8a\x00\x04\x00\x9c=\xf48\x16"))
