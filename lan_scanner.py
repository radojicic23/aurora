import scapy.all as scapy
import re


# Regular expression pattern to recognise IPv4 addresses
def lan_scan():
    ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

    # Get the address range to ARP
    while True:
        ip_entered_pattern = input("\n[*] ~ Enter IP Address and Range: ")
        if ip_range_pattern.search(ip_entered_pattern):
            print(f"[*] {ip_entered_pattern} is a valid ip address range.")
            break

    # The arping() method in scapy creates a pakcet with and ARP message
    # and sens it to the broadcast mac address ff:ff:ff:ff:ff:ff.
    arp_result = scapy.arping(ip_entered_pattern)
