from struct import unpack_from, calcsize


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, data, offset, order=">"):
        self.data = data
        self.offset = offset
        self.order = order

    def jump(self, offset):
        return BinaryReader(self.data, offset, self.order)

    def read(self, pattern):
        data = unpack_from(self.order + pattern, self.data, self.offset)
        self.offset += calcsize(pattern)
        return data[0]


def read_d(reader: BinaryReader):
    d1 = reader.read(Types.int64)
    d2 = reader.read(Types.uint16)
    return dict(D1=d1, D2=d2)


def read_c(reader: BinaryReader):
    c1 = reader.read(Types.double)
    c2 = reader.read(Types.uint16)
    c3 = reader.read(Types.float)
    c4 = [reader.read(Types.uint8) for _ in range(4)]
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader: BinaryReader):
    b1 = reader.read(Types.uint8)
    b2 = reader.read(Types.double)
    b3size = reader.read(Types.uint16)
    b3addr = reader.read(Types.uint32)
    b3reader = reader.jump(b3addr)
    b3 = [read_c(b3reader) for _ in range(b3size)]
    b4 = reader.read(Types.uint8)
    b5 = read_d(reader)
    b6 = reader.read(Types.int16)
    b7size = reader.read(Types.uint32)
    b7address = reader.read(Types.uint32)
    b7reader = reader.jump(b7address)
    b7 = [b7reader.read(Types.uint8) for _ in range(b7size)]
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7)


def read_a(reader: BinaryReader):
    a1 = reader.read(Types.uint32)
    a2 = reader.read(Types.int16)
    a3size = reader.read(Types.uint32)
    a3address = reader.read(Types.uint16)
    a3reader = reader.jump(a3address)
    a3 = [a3reader.read(Types.float) for _ in range(a3size)]
    a4 = reader.read(Types.int8)
    a5 = reader.read(Types.uint64)
    a6 = reader.read(Types.uint64)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)


def main(bytes):
    reader = BinaryReader(bytes, 5, '<')
    return read_a(reader)