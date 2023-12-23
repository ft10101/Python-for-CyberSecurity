# Python for Cyber Security
### List of tools :
- DNS_exploration.ipynb  ( Reconnaissance - Domain exploration )
- InitialAccess_AccountDiscovery_pynb.ipynb ( Discovering Credentials )
- InitialAccess_AutoRunUSB.ipynb ( Initial Access - Autorun USB )
- Introduction_to_Scapy.ipynb ( Introduction to Scapy )
- Port_Scanner.ipynb ( Reconnaissance - Port Scanner )
- default-UsrPass.txt (contains a list of default usernames and passwords )
- subdomains.txt ( contains a list of subdomains)
- mac_changer.py (MAC Address Changer)
- myNet_scanner.py (Network scanner)
- myARP_poison.py (ARP spoofing - MITM attacker)

-----------------------------------------------------------------------------------------------------------------
  
### Get Started :
To use any of the following tools, go through these steps:
1. Clone the repository.
  - -$`git clone https://github.com/ft10101/Python-For-CyberSecurity.git`
2. Change the directory to Python-For-CyberSecurity.
  - -$`cd Python-For-CyberSecurity `
3. Check for Python installation.
  - -$`python --version` or `python3 --version` <br>
If Python is not already installed? Install it by using: <br>
    -$`sudo apt install python3`
4. Execute the program by specifying valid arguments.

---------------------------------------------------------------------------------------------------------------------
    
# myNet_scanner - Network Scanner
Python script that scans the network and identifies the IP and MAC address of devices connected to that network. <br>
To use myNet_scanner - ( Network Scanner ) :
Execute the program by running :  
 - -$ `sudo python3 myNet_scanner.py -i 192.168.1.0/24 ` <br>
     -i : specifying the IP address range. (0/24 -> all 255)

----------------------------------------------------------------------------------------------------------------------

# myMAC - MAC Address Changer
Python script that changes the MAC Address of a Debian-based Linux system. <br>
To use myMAC - ( MAC Address Changer ) :
Execute the program by running :  
 - -$ `sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55 ` <br>
     -i : specifying the interface. <br>
     -m : specifying the new MAC address.

--------------------------------------------------------------------------------------------------------------------

# myARP_poison - ARP spoofer
Python script that performs MITM attacks.
To use myARP_poison ( ARP spoofer ) follow the below-mentioned steps:
1. Enable port forwarding by
`echo 1 > /proc/sys/net/ipv4/ip_forward`
2. Execute the script
   -$`sudo python3 myARP_poison.py -t 192.168.1.4 -g 192.168.1.1`
   -t : specifying the target IP address.
   -g : specifying the gateway/router IP address.
