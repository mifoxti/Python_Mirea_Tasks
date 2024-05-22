from struct import unpack_from, calcsize


class Types:
    int16 = 'h'
    int64 = 'q'
    int32 = 'i'
    uint8 = 'B'
    uint16 = 'H'
    uint32 = 'I'
    uint64 = 'Q'
    double = 'd'
    float = 'f'


class BinaryReader:
    def __init__(self, stream, offset, order="<"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_d(reader):
    d1 = [reader.read(Types.float) for _ in range(3)]
    # d1 = b''.join(d1).decode('utf-8')
    d2 = reader.read(Types.uint8)
    d3 = reader.read(Types.int32)
    d4 = reader.read(Types.int16)
    d5 = [reader.read(Types.uint16) for _ in range(6)]
    # d5 = b''.join(d5).decode('utf-8')
    d6 = reader.read(Types.uint64)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6)


def read_c(reader):
    c1 = reader.read(Types.uint32)

    c2_size = reader.read(Types.uint32)
    c2_offset = reader.read(Types.uint32)
    c2_reader = reader.jump(c2_offset)
    c2 = [c2_reader.read(Types.double) for _ in range(c2_size)]
    # c2 = b''.join(c2).decode('utf-8')
    return dict(C1=c1, C2=c2)


def read_b(reader):
    c_size = reader.read(Types.uint32)
    c_offset = reader.read(Types.uint16)
    c_reader = reader.jump(c_offset)
    b1 = [read_c(c_reader) for _ in range(c_size)]
    b2 = reader.read(Types.int64)
    b3 = read_d(reader)
    return dict(B1=b1, B2=b2, B3=b3)


def read_a(reader):
    a1_offset = reader.read(Types.uint32)
    a1_reader = reader.jump(a1_offset)
    a1 = read_b(a1_reader)
    a2 = reader.read(Types.int64)
    a3 = reader.read(Types.uint32)
    return dict(A1=a1, A2=a2, A3=a3)


def main(stream):
    return read_a(BinaryReader(stream, 5))


from pprint import pprint

pprint(main(b'\xafSMXGM\x00\x00\x00J\xd6(\x14@f\x1dI-.\xda2\xe4\xdcW\xbf\x865\xd0'
           b'\xbfp\xf0]\x0e\x99\x9d\xbd\xbf\\\x0c*S9+\xd8\xbf\x00\xf0v\xfe\x1d1\xca'
           b'\xbf\xce\x01f\x93\x02\x00\x00\x00\x15\x00\x00\x00d\xbf\xf1H\x02\x00\x00'
           b'\x00%\x00\x00\x00\x02\x00\x00\x005\x00=\xed\xaf|\xae\x1f&\xa1\xd6\xe4\xaf>d'
           b'Wh?\x9d\x8aj?\xa6%\xe2S%\x89%0s?\xa2\xaf\x15}h\xfc^\xc51V\xbe\r\xe7\xe9\xf8'
           b'\xc5\xfd'))
