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
    a1 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a1 += (val.decode())
    a2_offset, offset = parse(buffer, offset, 'uint16')
    a2, _ = parse_b(buffer, a2_offset)
    return {'A1': a1, 'A2': a2}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int32')
    b2, offset = parse(buffer, offset, 'uint64')
    b3, offset = parse(buffer, offset, 'int16')
    b4 = []
    for _ in range(2):
        b4_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_c(buffer, b4_offset)
        b4.append(val)
    b5 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'double')
        b5.append(val)
    b6, offset = parse(buffer, offset, 'float')
    b7, offset = parse_d(buffer, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5,
            'B6': b6, 'B7': b7}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'uint8')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'float')
    c3, offset = parse(buffer, offset, 'uint32')
    c4, offset = parse(buffer, offset, 'double')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'float')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'MQZ"\x03\x00\n\x00;\x00hhv\xd2\xa3z@\x04`WL\x0bB\xbf\x02\x0e\xab\xb4'
            b"\x90'\xe4\xc8]\xa6\xc1?0\xcd\xc9\xc0\xb2\x8a\x92k\xa9r\xbf\xdb\xd7M\xbb\x90"
            b'\xd2V\xc0\x17\x81\xcf\xbf5\xd9\x83\xb1F}\x85\xed\xfe\xb3C\x05\xe8n\r\x00\x00'
            b'\x00$\x00\x00\x00\xa8\xe5l\x15F\xa9\xea?(\x89\x7f\xa6X\xb7\xc0\xbfTl\x9a'
            b'z\x01\xf4\xe0\xbf\x08\x13p+\xc1\xcc\xe1\xbf\xb8\xa7V\x97r\xaa\xc7?\xac\xdd>'
            b'\xbb\x19\xab\xde\xbf,J(\x16\xd0\x89\xd3\xbf\xb6\xa6g?"\xf2\xfb>\xaa\x19\n'
            b'?\x0f.\xb6>Q$C?4\xdb\x9b>h\x18Y>\xb5\xd0\xba&'))
