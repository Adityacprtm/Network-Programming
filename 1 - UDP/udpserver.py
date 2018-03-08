import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind( ("0.0.0.0",1111) )
while True:
    data,client_address = sock.recvfrom(1000)
    print(data)
    data="OK "+data.decode('ascii')
    sock.sendto(data.encode('ascii'),client_address)
