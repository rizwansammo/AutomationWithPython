import socket

def port_scanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()

target_ip = input("Enter IP address: ")
for port in range(1, 1025):
    port_scanner(target_ip, port)
