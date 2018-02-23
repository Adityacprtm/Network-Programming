#import socket
import socket
from datetime import timedelta, datetime

#inisiasi objek socket UDP IP4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#IP 0.0.0.0 bisa di akses dari mana saja, sebaliknya IP tertentu + port tertentu
sock.bind( ("0.0.0.0", 6666) )

while True:
    #baca data yg diterima dari client
    data, client_address = sock.recvfrom(1000)
    print(data)
    print(client_address)
    dt = data.decode('utf-8')
    if dt == 'tanggal berapa?':
        tanggal = datetime.today().strftime("%d-%m-%Y")
        sock.sendto(str(tanggal).encode('utf-8'), client_address)
    else:
        sock.sendto("input tidak tersedia".encode('utf-8'), client_address)