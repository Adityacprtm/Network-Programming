import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6668))

# extention di atur default .txt pada server side

data = "del multi1"
tcp_sock.send(data.encode('utf-8'))
data = tcp_sock.recv(1000)
data = data.decode('utf-8')
print(data)

data = "read multi1"
tcp_sock.send(data.encode('utf-8'))
data = tcp_sock.recv(1000)
data = data.decode('utf-8')
print(data)

tcp_sock.close()