import socket
import os
from threading import Thread

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(("0.0.0.0", 6668))

tcp_sock.listen(100)

def handle_thread(conn):
    while True:
        try:
            data = conn.recv(1000)
            data = data.decode('utf-8')
            data = data.split(" ", 1)
            cmd = data[0]
            namaFile = data[1] + ".txt"
            if cmd == "new":
                try:
                    f = open(namaFile, "w+")
                    msg = "OK"
                    for i in range(3):
                        f.write("This is line %d\r\n" % (i+1))
                    conn.send(msg.encode('utf-8'))
                    print(cmd)
                    f.close()
                except:
                    msg = 'Something wrong! Can\'t create %s file.' % namaFile
                    conn.send(msg.encode('utf-8'))
            elif cmd == "read":
                try:
                    f = open(namaFile, "r")
                    contents = f.read()
                    conn.send(contents.encode('utf-8'))
                    print(cmd)
                    f.close()
                except:
                    msg = 'Sorry, Can\'t read %s file.' % namaFile
                    conn.send(msg.encode('utf-8'))
            elif cmd == "del":
                if os.path.exists(namaFile):
                    os.remove(namaFile)
                    msg = "OK"
                    conn.send(msg.encode('utf-8'))
                    print(cmd)
                else:
                    msg = "Sorry, can\'t remove %s file." % namaFile
                    conn.send(msg.encode('utf-8'))
            else:
                msg = "input not available"
                conn.send(msg.encode('utf-8'))
        except:
            conn.close()

while True:
    conn, client_addr = tcp_sock.accept()
    t = Thread(target=handle_thread, args=(conn,))
    t.start()