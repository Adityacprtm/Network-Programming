import struct

def send_size(conn, data):
    #hitung ukuran data
    size = len(data)
    #pack var size
    size = struct.pack("<I", size)
    #encode data
    data = data
    #data = data
    data = size + data
    #kirim
    conn.send(data)


def recv_size(conn):
    #baca ukuran data int = 4byte
    size = conn.recv(4)
    size = struct.unpack("<I", size)[0]
    #baca data
    data = conn.recv(size)
    #decode
    data = data
    return data
