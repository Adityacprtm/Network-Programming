from scapy.all import *

# Fungsi untuk handle packet masuk

def handle_packet(packet):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    frag = packet[IP].frag
    #print(frag)
    pay = len(packet[IP].payload)
    #print(pay)
    if frag == 6105 and pay >= (50000 - (6105*8)):
        print(str(frag)+" "+str(pay))
        print("terdapat serangan ICMP dari IP : " + src_ip)
    return

sniff(filter="icmp", prn=handle_packet) 
