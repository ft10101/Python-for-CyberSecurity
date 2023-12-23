import scapy.all as scapy
from scapy.layers.http import HTTP
import optparse

def get_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-i","--interface", dest="interface",help="Enter interface")
    user_input = parse_obj.parse_args()[0]
    if not user_input.interface:
        print("Enter interface")
    return user_input
    
def listen_packets(interface):
    scapy.sniff(iface=interface,store = False,prn=analyze_packets)
    # prn stands for callback function

def analyze_packets(packet):
    if packet.haslayer(HTTP):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)
            
user_interface = get_input()
listen_packets(user_interface.interface)