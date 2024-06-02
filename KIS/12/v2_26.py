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
    a1_offset, offset = parse(buffer, offset, 'uint16')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'uint64')
    a3 = ''
    for _ in range(4):
        val, offset = parse(buffer, offset, 'char')
        a3 += (val.decode())
    a4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        a4.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2, offset = parse_c(buffer, offset)
    b3 = []
    for _ in range(8):
        b3_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_e(buffer, b3_offset)
        b3.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse_d(buffer, offset)
    c2, offset = parse(buffer, offset, 'int16')
    c3, offset = parse(buffer, offset, 'int8')
    c4, offset = parse(buffer, offset, 'int8')
    c5, offset = parse(buffer, offset, 'uint8')
    c6, offset = parse(buffer, offset, 'uint16')
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5, 'C6': c6}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint32')
    e2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        e2.append(val)
    return {'E1': e1, 'E2': e2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'PTR\xbd\x8e\x00p\xa6\xf4\xcc\xcf\xe3\xff\xc8xsww\x03\x00\xba\x00\x00\x00'
            b'*3r\xcei\x98ei\x04\x00\x00\x00\x18\x00\x00\x00\xcfQ`\xabl]q\x03\x00\x00\x00('
            b'\x00\x00\x00\x81+\x8bL.\x89\x02\x00\x00\x007\x00\x00\x00\nl5\n\xd3\x86\x02'
            b'\x00\x00\x00E\x00\x00\x004\xe1-\xe9M\xc2\xe7\x03\x00\x00\x00S\x00'
            b'\x00\x00\x06\\\xac}\x94\xdcK\x03\x00\x00\x00b\x00\x00\x00\xa7%\x158u\x92\x07'
            b'\x03\x00\x00\x00q\x00\x00\x00\x03\xdd\xb2\xb9\x93\xc5\x02\x00'
            b'\x00\x00\x80\x00\x00\x00\xae\xe8+\xf0\xd8n\xc2\xbb\xac\x8e5\xdd\x1c\x00'
            b'\x00\x00+\x00\x00\x009\x00\x00\x00G\x00\x00\x00V\x00\x00\x00e\x00'
            b'\x00\x00t\x00\x00\x00\x82\x00\x00\x00\x91\x12\x0b\xbe\x02D\xcb;\xecGX?'))
