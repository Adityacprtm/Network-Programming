from scapy.all import *
import sys

ip_target = sys.argv[1]

for port in range(1,20):
    tcp_packet = IP(dst=ip_target)/TCP(dport=port)
    answer = sr1(tcp_packet, retry=1, verbose=False)

    if answer is None :
        print("Port "+str(port)+"...Closed")
    else :
        if TCP in answer :
            print("Port "+str(port)+"...Open")
        else :
            print("Port "+str(port)+"...Closed")
    time.sleep(1)
