import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data= input("masukin: ")
sock.sendto(data.encode('ascii'),('127.0.0.1',6666))

server_data,server_addr=sock.recvfrom(1000)
print(server_data.decode('ascii'))
