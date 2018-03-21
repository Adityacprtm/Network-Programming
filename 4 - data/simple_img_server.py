import socket
import os
from threading import Thread
from fungsi import send_img_size, recv_img_size

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind(("0.0.0.0", 6668))

tcp_sock.listen(100)

def handle_thread(conn):
    while True:
        try:
            #data = recv_size(conn)
            data = conn.recv(100)
            data = data.decode('ascii')
            data = data.split(" ", 1)
            cmd = data[0]
            namaFile = data[1] + ".jpg"
            if cmd == "read":
                try:
                    img_file = namaFile
                    f = open(img_file, "rb")
                    data = f.read()
                    #conn.send(data)
                    send_img_size(conn, data)
                    print(cmd)
                    f.close()
                except:
                    msg = 'Sorry, Can\'t read %s file.' % namaFile
                    conn.send(msg)
            elif cmd == "del":
                if os.path.exists(namaFile):
                    os.remove(namaFile)
                    msg = "OK - Deleted"
                    conn.send(msg.encode('ascii'))
                    print(cmd)
                else:
                    msg = "Sorry, can\'t remove %s file." % namaFile
                    conn.send(msg.encode('ascii'))
            elif cmd == "get":
                try:
                    img_file = namaFile
                    fin = open(img_file, "rb")
                    data = fin.read()
                    send_img_size(conn, data)
                    print(cmd)
                    fin.close()
                except IOError:
                    msg = "Image file %s not found" % img_file
                    conn.send(msg.encode('ascii'))
            else:
                msg = "input not available"
                conn.send(msg.encode('ascii'))
        except:
            conn.close()

while True:
    conn, client_addr = tcp_sock.accept()
    t = Thread(target=handle_thread, args=(conn,))
    t.start()
