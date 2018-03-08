#import socket
import socket
from threading import Thread

#inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind ke address dan port tertentu
tcp_sock.bind(('0.0.0.0', 6667))

#listen sebanyak 100
tcp_sock.listen(100)

def handle_thread(conn):
    while True:
        try:
            #terima string dari client
            #parameter rcv besaran atau ukuran data yg dibaca
            #Stream block
            data = conn.recv(100)
            data = data.decode('utf-8')

            #tambah data, penyebab masuk except
            data = "OK " + data

            #kirim balik ke client
            conn.send(data.encode('utf-8'))
        except(socket.error):
            print("Koneksi ditutup")
            break
            #tutup koneksi
            conn.close()

while True:
    #terima req keneksi
    conn, client_address = tcp_sock.accept()

    #buat thread baru untuk setiap permintaan koneksi
    t = Thread(target=handle_thread, args=(conn,))

    #start thread
    t.start()