import socket
import os
from threading import Thread

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(("0.0.0.0", 7778))

tcp_sock.listen(5)

def handle_thread(conn):
    while True:
        try:
            data = conn.recv(1024)
            data = data.decode('utf-8')
            if data == "":
                conn.send(data.encode('utf-8'))
            else:                
                data_split = data.split("#")
                nama = data_split[0]
                alamat = data_split[1]
                print("Pesan!")
                print("nama pengirim : " + nama + "\nalamat pengirim : " + alamat)
        except:
            conn.close()

while True:
    conn, client_addr = tcp_sock.accept()
    t = Thread(target=handle_thread, args=(conn,))
    t.start()
