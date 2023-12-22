import scapy.all as scapy
# module that can create arp requests and deals with them
import optparse  
# for getting inputs from the user

def get_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-i","--ipaddress",dest="ip_address",help = "enter IP address")
    
    (user_inputs,arguments) = parse_obj.parse_args()
    if not user_inputs.ip_address:
        print("enter IP address")
    return user_inputs

def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    # creating a arp request for ip ranges 
    # 0/24 specifies all 255 ip's
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # creating a packet for broadcast mac ranges 
    # ff specifies max thus all the mac addresses
    combined_packet = broadcast_packet/arp_request_packet
    # combining two packets using scapyies / method
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    # broadcast to all combined packets of mac and ip addresses 
    answered_list.summary()
    
user_ip_address = get_input()
scan_network(user_ip_address.ip_address)