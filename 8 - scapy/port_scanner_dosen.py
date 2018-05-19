from scapy.all import *
import sys
import time

ip = sys.argv[1]

for i in range(70,75):
    tcp = IP(dst=ip)/TCP(dport=i)
    ans = sr1(tcp, retry=-1, verbose=False)
    if ans is None:
        print("Port " + str(i) + " . . . Closed")
    else:
        if TCP in ans:
            print("Port " + str(i) + " . . . Open")
        else:
            print("Port " + str(i) + " . . . Closed")
    time.sleep(2)
