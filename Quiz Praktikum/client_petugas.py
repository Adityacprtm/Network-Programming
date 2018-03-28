#import socket
import socket

#inisiasi objek
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim req koneksi ke server
tcp_sock.connect(("127.0.0.1", 7778))

while True:
    data = tcp_sock.recv(1024)
    data = data.decode('utf-8')
    data = data.split("#")
    nama = data[0]
    alamat = data[1]
    print("nama pengirim : " + nama + "\nalamat pengirim : " + alamat)

tcp_sock.close()
