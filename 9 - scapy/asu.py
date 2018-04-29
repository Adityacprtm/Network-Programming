from scapy.all import *


def handle_packet(packet):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    if ICMP in packet:
        size = len(packet[ICMP].load)
        fr = packet[IP].frag
        print(str(size))
        if fr == 6105 and size >= 50000-(6105*8):
            print("ada serangan dari "+str(src_ip))
        #return packet.show()


sniff(filter="icmp", prn=handle_packet)
