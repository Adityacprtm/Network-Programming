from scapy.all import *

# Fungsi untuk handle packet masuk


def handle_packet(packet):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print("Paket dari IP "+src_ip+" ke "+dst_ip +
              " src_port "+str(src_port)+" d_port"+str(dst_port))
    else:
        print("Bukan paket TCP")
    return packet.summary()


sniff(iface="en0", filter="ip", prn=handle_packet)
