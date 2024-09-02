import subprocess

def change_mac(interface, new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print(f"MAC address for {interface} changed to {new_mac}")

interface = input("Enter interface name: ")
new_mac = input("Enter new MAC address: ")
change_mac(interface, new_mac)
