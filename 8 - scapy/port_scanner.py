from scapy.all import *
import sys

ip = "175.45.184.70"
minport = input("min port : ")
maxport = input("max port : ")
ports = range(int(minport), int(maxport)+1)

def checkhost(ip):
    conf.verb = 0  # disbale any output from scapy
    try:
        ping = sr1(IP(dst=ip)/ICMP())
        print("\nTarget is up, Beginning Scan . . .")
    except Exception:
        print("\nCouldn't resolve Target")
        sys.exit(1)

def scanport(port):
    srcport = 7778
    conf.verb = 0  # disbale any output from scapy
    pkt = sr1(IP(dst=ip)/TCP(sport=srcport, dport=port, flags="S"))
    print("Scanning port " + str(port))
    if str(type(pkt)) == "<type 'NoneType'>" :
        return False
    elif pkt.haslayer(TCP) :
        pktFlags = pkt.getlayer(TCP).flags
        if pktFlags == 0x12 :
            return True
        else:
            return False
    RSTpkt = IP(dst=ip)/TCP(sport=srcport,dport=port,flags="R")

checkhost(ip)
list = []
for port in ports:
    status = scanport(port)
    if status == True:
        list.append("port " + str(port) + " : Open")
    else:
        list.append("port " + str(port) + " : Close")

for lists in list:
    print(lists)