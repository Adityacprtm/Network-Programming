#import socket
import socket

#inisiasi objek socket UDP IP4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#kirim ke server
data = "selamat sore"
sock.sendto( data.encode('utf-8'), ("127.0.0.1", 6666) )

#baca dari server
server_data, server_addr = sock.recvfrom(1000)

#cetak layar
print(server_data.decode('utf-8'))