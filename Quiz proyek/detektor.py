from scapy.all import *
import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect(("127.0.0.1", 6668))

dict_sender = {}

def handle_packet(paket):
    src_ip = paket[IP].src
    dst_ip = paket[IP].dst
    
    if TCP in paket:
        if src_ip not in dict_sender:
            dict_sender[src_ip] = 0
            dict_sender[src_ip] = paket[TCP].dport
        else:
            print(dict_sender[src_ip])
            tcp_sock.send(src_ip.encode('utf-8'))
            dict_sender[src_ip] = 0
            dict_sender[src_ip] = paket[TCP].dport
    else:
        dict_sender[src_ip] = paket[IP].dport

sniff(filter="tcp", prn=handle_packet)
