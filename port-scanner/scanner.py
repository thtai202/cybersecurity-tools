import socket
import sys



#Command should look like: thtai-scanner TARGET. Parsing it
def ParsingCommand(userInput):
    parts = userInput.split()
    if len(parts) < 2 and parts[0] !='thtai-scanner':
        return None
    target = parts[1]
    port = 80 #default port
    if '-p' in parts:
        i = parts.index('-p')
        if i+1 < len(parts) and parts[i + 1].isdigit():
            port = int(parts[i+1])
        else:
            return None
    return target, port 
            
#Input
def GetInput():
    while True:
        result = ParsingCommand(input('>>> '))
        if result:
            return result
        print("thtai--scanner TARGET [-p PORT]")
                
target, port = GetInput();
print(target, port)

#creating the socket
# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print ("Socket successfully created")
# except socket.error as err:
#     print ("socket creation failed with error %s" %(err))

# try:
#     ip = socket.gethostbyname(TARGET)
# except socket.gaierror:
#     print("hostname could not be resolved.")
#     sys.exit()

#connecting to the server
#s.connect((ip, port))
#print(ip)
#print ("Successfully connect")
