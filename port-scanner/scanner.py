import socket
import ipaddress
import sys
# Test cases
test_cases = [
    # IP, domain, ports
    ("93.184.216.34", "example.com", [80]),
    ("142.250.72.14", "google.com", [80]),
    ("1.1.1.1", "cloudflare.com", [80]),
]

#Command should look like: thtai-scanner TARGET. Parsing it
def ParsingCommand(userInput):

    parts = userInput.split()

    if len(parts) < 2 or parts[0] != 'thtai-scanner':
        return None

    target = None
    ports = [80]  # default port
    skip = False

    # parsing ports
    for i, part in enumerate(parts[1:]):

        if skip:
            skip = False
            continue

        if part == '-p':

            if i + 2 < len(parts):

                try:
                    portInput = parts[i + 2]

                    if '-' in portInput:
                        start, end = map(int, portInput.split('-'))

                        if start < 1 or end > 65535 or start > end:
                            return None

                        ports = list(range(start, end + 1))

                    else:
                        ports = [int(port) for port in portInput.split(',')]

                        if any(port < 1 or port > 65535 for port in ports):
                            return None

                    skip = True

                except ValueError:
                    return None

            else:
                return None

        else:
            if target is not None:
                return None

            target = part

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

    return target, ports, ip, domain
    parts = userInput.split()
    if len(parts) < 2 or parts[0] !='thtai-scanner':
        return None

    target = None
    ports = [80]  # default port

    skip = False
    # parsing ports
    for i,part in enumerate(parts[1:]):
        if skip:
            skip = False
            continue
        if '-p' == part:
            if i + 2 < len(parts):
                
                try:
                    portInput = part[i + 2]
                    if '-' in portInput:
                        
                        start, end = map(int,portInput.split('-'))

                        if start < 1 or end > 65535 or start > end:
                            return None
                        
                        ports = list[range(start, end + 1)] 
                except ValueError:
                    return None
            else: 
                try:
                    ports = [int(port) for port in port_input.split(',')]
                    if any(port < 1 or port > 65535 for port in ports):
                        return None
                    else:
                        return None
                except ValueError:
                    return None
        else:
            if target is not None:
                return None

            target = part
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
    return target, ports, ip, domain

def GetInput():
    while True:
        result = ParsingCommand(input('>>> '))
        if result:
            return result
        print("thtai-scanner TARGET [-p PORT]")
#Validating the target
def ValidatingTarget(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False
# Connecting to ports
def ScanPort(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(2)
        s.connect((ip, port))
        return "OPEN"
    except socket.timeout:
        return "TIMEOUT"
    except ConnectionRefusedError:
        return "CLOSED"
    finally:
        s.close()
# Banner Grabbing
def BannerGrabbing(ip,domain, ports):
    request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {domain}\r\n"
    "\r\n"
    )
    #Converting request -> bytes
    request = request.encode()
    for port in ports:
        try:
            #Making connect
            s = socket.socket()
            s.settimeout(5) 
            s.connect((ip, int(port)))
            
            s.sendall(request)

            banner = s.recv(1024).decode(errors="ignore").strip()
            print(f"Banner for {ip}:{port} -> {banner}")
            
        except socket.timeout:
                print(f"{ip}:{port}: Timeout")
        except socket.error as e:
                print(f"{ip}:{port} -> Error: {e}")
        finally: 
            s.close()

for ip, domain,ports in test_cases:
    print(f"\n>>> BannerGrabbing({ip}, {domain},{ports})")
    BannerGrabbing(ip, domain, ports)
target, ports, ip, domain = GetInput()


print("Target: ", domain)
print("IP: ", ip)
print("Port: ", ports)



