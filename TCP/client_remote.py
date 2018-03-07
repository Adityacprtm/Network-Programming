import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6668))

#inputan:new/read/del nama_file.txt
data = input("Masukan perintah: ")
tcp_sock.send(data.encode('utf-8'))

data = tcp_sock.recv(1000)
data = data.decode('utf-8')
print(data)

tcp_sock.close()