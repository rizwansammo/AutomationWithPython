import socket


# Function to scan open ports
def scan_ports(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")

    # Iterate through the range of ports
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Try to connect to the target IP on the current port
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")

        sock.close()


# Input: Target IP and port range
target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the start port number: "))
end_port = int(input("Enter the end port number: "))

# Call the scan_ports function
scan_ports(target_ip, start_port, end_port)
