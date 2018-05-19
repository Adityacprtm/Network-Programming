#import socket
import socket
from threading import Thread

#inisialisasi socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind
tcp_sock.bind(('0.0.0.0', 6668))

#listen sebanyak 100 permintaan koneksi
tcp_sock.listen(100)

def handle_thread(conn):
    while True:
        try :
            #terima string dari detector
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "IP attacker " + data
            #print hasil report
            print(data)
        except(socket.error):
            print("Koneksi tertutup")
            break
            #tutup koneksi
            conn.close()

while True:
    #terima permintaan
    conn, client_address = tcp_sock.accept()
    #buat thread baru untuk setiap permintaan baru
    t = Thread(target=handle_thread, args=(conn, ))
    #start thread
    t.start()

    