#import socket
import socket

#inisiasi objek socket UDP IP4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#kirim ke server
data = "tanggal berapa?"
sock.sendto( data.encode('utf-8'), ("192.168.0.255", 6666) )

#baca dari server
server_data, server_addr = sock.recvfrom(1000)

#cetak layar
print(server_data.decode('utf-8'))