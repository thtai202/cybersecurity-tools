import socket
import ipaddress
import sys


#Command should look like: thtai-scanner TARGET. Parsing it
def ParsingCommand(userInput):
    parts = userInput.split()
    if len(parts) < 2 or parts[0] !='thtai-scanner':
        return None
    target = parts[1]
    # Resolve IP
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return None
    # Resolve hostname
    if target == ip:
        try:
            domain = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            domain = None
    else:
        domain = target

    # parsing ports
    ports = [80] #default port
    if '-p' in parts:
        i = parts.index('-p')
        if i+1 < len(parts):
            try:
                ports = [int(port) for port in parts[i + 1].split(',')]
                if any(port < 1 or port > 65535 for port in ports):
                    return None
            except ValueError:
                return None
        else:
            return None
    return target, ports, ip, domain
#Input
def GetInput():
    while True:
        result = ParsingCommand(input('>>> '))
        if result:
            return result
        print("thtai--scanner TARGET [-p PORT]")
#Validating the target
def ValidatingTarget(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False
# Connecting to ports
def ScanPort(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        s.connect((ip, port))
        return "OPEN"

    except socket.timeout:
        return "TIMEOUT"

    except ConnectionRefusedError:
        return "CLOSED"

    finally:
        s.close()

target, ports, ip, domain = GetInput()

if ValidatingTarget(target) == True:
    print("Target is validated.")
    print("Target: ", domain)
    print("IP: ", ip)
    print("Port: ", ports)

    for port in ports:
        result = ScanPort(ip, port)
        print(f"Port {port}: {result}")