#import socket
import socket
import struct

#inisiasi objek
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim req koneksi ke server
tcp_sock.connect(("127.0.0.1", 6667))

#kirim data
data = 50
#representasikan variable data sebagai unsigned int, little endian
tcp_sock.send(struct.pack("<I",data))

#baca data yg dikirim balik oelh serer
data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)

tcp_sock.close
