import subprocess # module to run commands through python
import optparse # module to add command line options
import re # module for regular expresions

def get_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_obj.add_option("-m","--mac",dest="mac_address",help="new mac address")
    return parse_obj.parse_args()
# function to get input from the user as arguments to this file
# -i with interface -m with mac address that we want to keep

def change_mac(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])
# function to change the mac address by using terminal commands using subprocess

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    
    if new_mac:
        return new_mac.group(0)
    else:
        return None
# funtion to check that our mac has actually changed 
# using regularised expressions / regex

print("myMac Changer started")
(user_input, arguments) = get_input()
change_mac(user_input.interface,user_input.mac_address)
print("myMac Changer changed MAC Address")
final_mac = control_new_mac(str(user_input.interface))

if final_mac == user_input.mac_address:
    print("MAC Changed successfully")
else:
    print("Error")