#import socket
import socket
from fungsi import send_termination, recv_termination

#inisiasi objek
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim req koneksi ke server
tcp_sock.connect(("127.0.0.1", 6667))

#kirim data
data = "Pada perkuliahan berikutnya, kita akan membahas mengenai komunikasi antar entitas menggunakan mekanisme Indirect Communication. Untuk kelengkapan praktek, sebelum kuliah berlangsung, mahasiswa diharuska memasang beberapa perangkat lunak dan library, antara lain"
send_termination(tcp_sock, data)

#baca data yg dikirim balik oelh serer
data = recv_termination(tcp_sock)
print(data)

tcp_sock.close
