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
  
## Get Started
### myMAC - MAC Address Changer
Python script that can change the MAC Address of a Debian-based Linux system.
To use myMAC - ( MAC Address Changer ) :
1. Clone the repository.
  - ` git clone https://github.com/ft10101/Python-For-CyberSecurity.git`
2. Change the directory to Python-For-CyberSecurity.
  - ` cd Python-For-CyberSecurity `
3. Check for Python installation.
  - ` python --version` or `python3 --version` <br>
Is Python not already installed? Install it by using: <br>
  ` sudo apt install python3` 
4. Execute the program by running :  
 - ` -$ python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55 ` <br>
     -i specifies the interface <br>
     -m specifies the new MAC address that we want to keep.
   ----
