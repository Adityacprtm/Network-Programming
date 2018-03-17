import socket
import os
from threading import Thread
from fungsi import send_termination, recv_termination

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(("0.0.0.0", 6668))

tcp_sock.listen(100)

def handle_thread(conn):
    while True:
        try:
            #data = recv_termination(tcp_sock)
            data = conn.recv(100)
            data = data.decode('ascii')
            data = data.split(" ", 1)
            cmd = data[0]
            namaFile = data[1] + ".txt"
            if cmd == "new":
                try:
                    f = open(namaFile, "w+")
                    msg = "OK - Created"
                    for i in range(0,20):
                        f.write('HELLO WORLD!!! ')
                    send_termination(conn, msg)
                    #conn.send(msg.encode('utf-8'))
                    print(cmd)
                    f.close()
                except:
                    msg = 'Something wrong! Can\'t create %s file.' % namaFile
                    send_termination(conn, msg)
                    #conn.send(msg.encode('utf-8'))
            elif cmd == "read":
                try:
                    f = open(namaFile, "r")
                    contents = f.read()
                    send_termination(conn, contents)
                    #conn.send(contents.encode('utf-8'))
                    print(cmd)
                    f.close()
                except:
                    msg = 'Sorry, Can\'t read %s file.' % namaFile
                    send_termination(conn, msg)
                    #conn.send(msg.encode('utf-8'))
            elif cmd == "del":
                if os.path.exists(namaFile):
                    os.remove(namaFile)
                    msg = "OK - Deleted"
                    send_termination(conn, msg)
                    #conn.send(msg.encode('utf-8'))
                    print(cmd)
                else:
                    msg = "Sorry, can\'t remove %s file." % namaFile
                    send_termination(conn, msg)
                    #conn.send(msg.encode('utf-8'))
            else:
                msg = "input not available"
                send_termination(conn, msg)
                #conn.send(msg.encode('utf-8'))
        except:
            conn.close()


while True:
    conn, client_addr = tcp_sock.accept()
    t = Thread(target=handle_thread, args=(conn,))
    t.start()
