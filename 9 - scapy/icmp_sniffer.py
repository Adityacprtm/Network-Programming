from scapy.all import *

# Fungsi untuk handle packet masuk
def handle_packet(packet):

    # unutuk mengambil src IP dari paket
    src_ip = packet[IP].src
    # unutuk mengambil dst IP dari paket
    dst_ip = packet[IP].dst
    # unutuk mengambil frag offset dari paket
    frag = packet[IP].frag
    # unutuk mengambil payload dari paket
    pay = len(packet[IP].payload)

    # mengambil informasi dari paket data terakhir
    # jika dikirim 50000 byte paket terakhir -> fragment offset = 6105 | payload >= 1160
    if frag == 6105 and pay >= (50000 - (6105*8)):
        print("Terdapat sebuah serangan ICMP flood dari IP " + src_ip)
    return

sniff(filter="icmp", prn=handle_packet) 
