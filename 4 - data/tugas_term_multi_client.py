import socket
from fungsi import send_termination, recv_termination

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6668))

# extention di atur default .txt pada server side
while True:
    print('\n')
    input1 = input("command > ")
    input2 = input("File name > ")
    data = input1 + " " + input2
    #send_termination(tcp_sock, data)
    tcp_sock.send(data.encode('ascii'))
    data = recv_termination(tcp_sock)
    #data = tcp_sock.recv(100)
    #data = data.decode('utf-8')
    print(data)

tcp_sock.close()
