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

  
## Get Started :
### myNet_scanner - Network Scanner
Python script that scans the network and identifies the IP and MAC address of devices connected to that network. <br>
To use myNet_scanner - ( Network Scanner ) :
1. Clone the repository.
  - -$`git clone https://github.com/ft10101/Python-For-CyberSecurity.git`
2. Change the directory to Python-For-CyberSecurity.
  - -$`cd Python-For-CyberSecurity `
3. Check for Python installation.
  - -$`python --version` or `python3 --version` <br>
Is Python not already installed? Install it by using: <br>
    -$`sudo apt install python3` 
4. Execute the program by running :  
 - -$`python3 myNet_scanner.py -i 192.168.1.0/24 ` <br>
     -i : specifying the IP address range. (0/24 -> all 255)

### myMAC - MAC Address Changer
Python script that changes the MAC Address of a Debian-based Linux system. <br>
To use myMAC - ( MAC Address Changer ) :
1. Clone the repository.
  - -$`git clone https://github.com/ft10101/Python-For-CyberSecurity.git`
2. Change the directory to Python-For-CyberSecurity.
  - -$`cd Python-For-CyberSecurity `
3. Check for Python installation.
  - -$`python --version` or `python3 --version` <br>
Is Python not already installed? Install it by using: <br>
    -$`sudo apt install python3` 
4. Execute the program by running :  
 - -$`python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55 ` <br>
     -i : specifying the interface. <br>
     -m : specifying the new MAC address.
