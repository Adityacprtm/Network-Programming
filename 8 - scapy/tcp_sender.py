from scapy.all import *

#tcp_packet = IP(src="192.168.0.4",dst="175.45.184.70")/TCP(sport=7778,dport=80)
tcp_packet = IP(dst="175.45.187.242")/ICMP()/Raw("helllo")
jawaban = sr1(tcp_packet)
jawaban.show()
