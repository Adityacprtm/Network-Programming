import socket ,datetime
from datetime import timedelta,datetime

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind( ("0.0.0.0",6666) )
while True:
    data,client_address = sock.recvfrom(6666)
    dt= data.decode('ascii')
    if dt =='today' :
      tanggal = datetime.today()
      sock.sendto(str(tanggal).encode('ascii'), client_address)
    elif dt == 'yesterday':
        tanggal = datetime.today()-timedelta(days=1)
        sock.sendto(str(tanggal).encode('ascii'), client_address)
    elif dt == 'tommorow':
        tanggal = datetime.today()+timedelta(days=1)
        sock.sendto(str(tanggal).encode('ascii'), client_address)
    else:
        sock.sendto("input tidak tersedia".encode('ascii'), client_address)
