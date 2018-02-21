#import socket
import socket

#inisiasi objek socket UDP IP4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#IP 0.0.0.0 bisa di akses dari mana saja, sebaliknya IP tertentu + port tertentu
sock.bind( ("0.0.0.0", 6666) )

#baca data yg diterima dari client
data, client_address = sock.recvfrom(1000)
print(data)

#ubah data
data = "OK " + data.decode('ascii')

#kirim ke client
sock.sendto(data.encode('ascii'), client_address)