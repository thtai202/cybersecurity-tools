import socket
import sys


#command should look like: thtai-scanner TARGET. Parsing it
user_input = ""
while(user_input == ""):
    user_input = input("")
    parts = user_input.split()
    if(parts[0].lower() != "thtai-scanner"):
        user_input = ""

TARGET = parts[1]
#testing first port
port = 80

#creating the socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

try:
    ip = socket.gethostbyname(TARGET)
except socket.gaierror:
    print("hostname could not be resolved.")
    sys.exit()

#connecting to the server
s.connect((ip, port))
print(ip)
print ("The socket has successfully connected to google")