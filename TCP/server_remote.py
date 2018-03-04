import socket, os

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind( ("0.0.0.0", 6668) )

tcp_sock.listen(100)

while True:
    conn, client_addr = tcp_sock.accept()
    data = conn.recv(1000)
    data = data.decode('utf-8')
    data = data.split(" ",1)
    cmd = data[0]
    namaFile = data[1]
    print(namaFile)
    if cmd == "new":
        try:
            f = open(namaFile,"w+")
            msg = "OK"
            for i in range(5):
                f.write("This is line %d\r\n" % (i+1))
            conn.send(msg.encode('utf-8'))
            print(cmd)
            f.close()
        except:
            msg = 'Something went wrong!'
            conn.send(msg.encode('utf-8'))
    elif cmd == "read":
        try:
            f = open(namaFile, "r")
            contents = f.read()
            conn.send(contents.encode('utf-8'))
            print(cmd)
            f.close()
        except:
            msg = 'Something went wrong!'
            conn.send(msg.encode('utf-8'))
    elif cmd == "del":
        if os.path.exists(namaFile):
            os.remove(namaFile)
            msg = "OK"
            conn.send(msg.encode('utf-8'))
            print(cmd)
        else:
            msg = "Sorry, can not remove %s file." % "test.txt" 
            conn.send(msg.encode('utf-8'))
    else:
        msg = "input not available"
        conn.send(msg.encode('utf-8'))
    conn.close()