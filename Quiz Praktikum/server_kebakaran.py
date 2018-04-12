import socket
import os
import json
from threading import Thread

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(("0.0.0.0", 6667))

tcp_sock.listen(100)

'''
    format lapor
    {
        "command" : "LAPOR",
        "alamat" : "Jl.perawan 5"
    }

    format reg
    {
        "command" : "PETUGAS"
    }
'''

list_petugas = []

def handle_thread(conn):
    while True:
        try:
            data = conn.recv(1024)
            data = data.decode('utf-8')
            data = json.loads(data)
            msg = ""
            if data["command"] == "LAPOR":
                for i in list_petugas:
                    alamat = data["alamat"]
                    i.send(alamat.encode('utf-8'))
                msg = "Laporan berhasil terkirim"
            elif data["command"] == "PETUGAS":
                msg = "Petugas berhasil terdaftar"
                list_petugas.append(conn)
            else:                
                msg = "Command tidat tersedia"
            conn.send(msg.encode('utf-8'))
        except:
            conn.close()

while True:
    conn, client_addr = tcp_sock.accept()
    t = Thread(target=handle_thread, args=(conn,))
    t.start()
