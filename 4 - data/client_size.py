#import socket
import socket
from fungsi2 import send_size, recv_size

#inisiasi objek
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim req koneksi ke server
tcp_sock.connect(("127.0.0.1", 6667))

#kirim data
data = "Pada perkuliahan berikut"
send_size(tcp_sock, data)

#baca data yg dikirim balik oelh serer
data = recv_size(tcp_sock)
print(data)

tcp_sock.close
