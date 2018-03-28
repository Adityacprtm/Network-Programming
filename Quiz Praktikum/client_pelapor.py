#import socket
import socket

#inisiasi objek
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim req koneksi ke server
tcp_sock.connect(("127.0.0.1", 7778))

while True:
    #kirim data
    nama = input("nama > ")
    alamat = input("alamat > ")
    msg = nama + "#" + alamat
    tcp_sock.send(msg.encode('utf-8'))
    print("Data terkirim . . .")

tcp_sock.close()
