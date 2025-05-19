# Calculate the Network Range from a CIDR Notation
# Given input
"""
import ipaddress

def get_network_range(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return (network.network_address, network.broadcast_address)
    except ValueError:
        return "Invalid CIDR Notation"

cidr = "192.168.1.0/24"
network_range = get_network_range(cidr)

if isinstance(network_range, tuple):
    print(f"Network range: {network_range[0]} - {network_range[1]}")
else:
    print(network_range)
"""
# User input:
"""
import ipaddress

def get_network_range(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return (network.network_address, network.broadcast_address)
    except ValueError:
        return "Invalid CIDR Notation"

# Accept CIDR input from the user
cidr = input("Enter a CIDR notation: ")

network_range = get_network_range(cidr)

if isinstance(network_range, tuple):
    print(f"Network range: {network_range[0]} - {network_range[1]}")
else:
    print(network_range)
"""
# CIDR tool showing network info: range, hosts, version.

import ipaddress

def get_network_details(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        total_ips = network.num_addresses

        # Usable IPs (exclude first and last for IPv4 with more than 2 IPs)
        if total_ips > 2 and isinstance(network, ipaddress.IPv4Network):
            first_usable = list(network.hosts())[0]
            last_usable = list(network.hosts())[-1]
        else:
            first_usable = last_usable = "N/A"

        return {
            "version": network.version,
            "network": str(network),
            "network_address": network_address,
            "broadcast_address": broadcast_address,
            "total_ips": total_ips,
            "first_usable": first_usable,
            "last_usable": last_usable,
            "usable_hosts": total_ips - 2 if total_ips > 2 else 0
        }

    except ValueError:
        return "Invalid CIDR Notation"

# User input
cidr = input("Enter a CIDR notation: ")

# Get and display results
details = get_network_details(cidr)

if isinstance(details, dict):
    print(f"\nCIDR: {details['network']}")
    print(f"IP Version: IPv{details['version']}")
    print(f"Network Address: {details['network_address']}")
    print(f"Broadcast Address: {details['broadcast_address']}")
    print(f"Total IPs: {details['total_ips']}")
    print(f"Usable Hosts: {details['usable_hosts']}")
    print(f"Usable IP Range: {details['first_usable']} - {details['last_usable']}")
else:
    print(details)

"""
• This script takes a CIDR notation as input, parses it, and displays the network details.
• It handles both IPv4 and IPv6 CIDRs and provides information about the network address, broadcast address, total number of IPs, and usable hosts.
• For IPv4 networks with more than 2 usable hosts , it also identifies the first and last usable IP addresses.
• If the input CIDR notation is invalid, it displays an error message.

# Example 1: Standard IPv4 /24

Enter a CIDR notation: 192.168.1.0/24

CIDR: 192.168.1.0/24
IP Version: IPv4
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Total IPs: 256
Usable Hosts: 254
Usable IP Range: 192.168.1.1 - 192.168.1.254

# Example 2: Small IPv4 /30 (Only 2 usable IPs)

Enter a CIDR notation: 10.0.0.0/30

CIDR: 10.0.0.0/30
IP Version: IPv4
Network Address: 10.0.0.0
Broadcast Address: 10.0.0.3
Total IPs: 4
Usable Hosts: 2
Usable IP Range: 10.0.0.1 - 10.0.0.2

# Example 3: Host-only /32

Enter a CIDR notation: 192.168.0.10/32

CIDR: 192.168.0.10/32
IP Version: IPv4
Network Address: 192.168.0.10
Broadcast Address: 192.168.0.10
Total IPs: 1
Usable Hosts: 0
Usable IP Range: N/A - N/A

# Example 4: IPv6 Address

Enter a CIDR notation: 2001:db8::/126

CIDR: 2001:db8::/126
IP Version: IPv6
Network Address: 2001:db8::
Broadcast Address: 2001:db8::3
Total IPs: 4
Usable Hosts: 2
Usable IP Range: N/A - N/A

# Example 5: Invalid Input

Enter a CIDR notation: not.a.cidr
Invalid CIDR Notation
"""