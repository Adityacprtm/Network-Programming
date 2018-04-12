#import socket
import socket
import json

#inisiasi objek
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#kirim req koneksi ke server
tcp_sock.connect(("127.0.0.1", 6667))

data = {
    "command" : "PETUGAS"
}
data = json.dumps(data)
tcp_sock.send(data.encode('utf-8'))

while True:
    data = tcp_sock.recv(100)
    data = data.decode('utf-8')
    print(data)

tcp_sock.close()
