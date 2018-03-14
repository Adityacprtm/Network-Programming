#import socket
import socket
import struct

#inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind ke address dan port tertentu
tcp_sock.bind(('0.0.0.0', 6667))

#listen sebanyak 100
tcp_sock.listen(100)

while True:
    #terima req keneksi
    conn, client_address = tcp_sock.accept()
    
    #terima string dari client
    #parameter rcv besaran atau ukuran data yg dibaca
    #Stream block
    #4 karena membaca tipe data int 32 bit = 4 byte
    data = conn.recv(4)
    data = struct.unpack("<I",data)[0]
    data = 20 + data

    #tambah data
    data = 'OK ' + str(data)
    
    #kirim balik ke client
    conn.send(data.encode('utf-8'))

    #tutup koneksi
    conn.close()
