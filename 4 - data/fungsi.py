import struct

def send_termination(conn, data):
    term_char = "\r\n"
    data = data + term_char
    conn.send(data.encode('ascii'))

def recv_termination(conn):
    #variable untuk data
    data = ''
    while True:
        #baca data
        buffer = conn.recv(100)
        #ubah jadi string, python pakai byte
        buffer = buffer.decode('ascii')
        # cek jika buffer mengandung term char
        if "\r\n" in buffer :
            #buang term char
            data = data.replace("\r\n", "")
            #tambahkan buffer ke data
            data = data + buffer
            # return (keluar dari fungsi)
            return data
        #tambahkan buffer ke data
        data = data + buffer

def send_size(conn,data):
    #hitung ukuran data
    size = len(data)
    #pack var size
    size = struct.pack("<I", size)
    #encode data
    data = data.encode('ascii')
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
    data = data.decode('ascii')
    return data
