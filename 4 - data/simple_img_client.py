import socket
from fungsi import send_img_size, recv_img_size

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.connect(("127.0.0.1", 6668))

# extention di atur default .txt pada server side
while True:
    print('\n')
    input1 = input("command img (read/get/del) > ")
    input2 = input("File name img (hanya nama) > ")
    data = input1 + " " + input2
    tcp_sock.send(data.encode('ascii'))
    #send_size(tcp_sock, data)
    if input1 == "get":
        data = recv_img_size(tcp_sock)
        fh = open("ImgToSave.jpg", "wb")
        fh.write(data)
        fh.close()
    else:
        #data = tcp_sock.recv(1000)
        data = recv_img_size(tcp_sock)
        print(data)

tcp_sock.close()
