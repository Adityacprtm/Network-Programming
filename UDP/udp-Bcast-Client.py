#import socket
import socket

#inisiasi objek socket UDP IP4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#inisiasi broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#kirim ke server
data = "tanggal berapa?"
sock.sendto( data.encode('utf-8'), ("10.34.223.255", 6666) )
data = "jam berapa?"
sock.sendto(data.encode('utf-8'), ("10.34.223.255", 6666))

while True:
    #baca dari server
    server_data, server_addr = sock.recvfrom(1000)
    #cetak layar
    msg = "answer from " + str(server_addr) + "\n" + server_data.decode('utf-8')
    print(msg)
