
import scapy.all as scapy

def packet_sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=lambda x: x.summary())

interface = input("Enter interface name: ")
packet_sniffer(interface)