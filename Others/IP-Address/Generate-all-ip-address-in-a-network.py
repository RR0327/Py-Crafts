# Raw 
"""
import ipaddress

def generate_ips_in_network(network):
    try:
        network = ipaddress.ip_network(network, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        return []
    
network = "192.168.1.0/30"
ips = generate_ips_in_network(network)
print(f"Ip addresses in the network {network} are: {ips}")
"""

# Modified Version
"""
import ipaddress
from typing import List

def generate_ips_in_network(network_cidr: str, verbose: bool = False) -> List[str]:
    
    # Generate all usable host IP addresses within a given network.

    # Args:
    #     network_cidr (str): The network in CIDR notation (e.g., '192.168.1.0/24').
    #     verbose (bool): If True, prints error details on invalid input.

    # Returns:
    #     List[str]: List of valid host IPs as strings.
    
    try:
        network = ipaddress.ip_network(network_cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        if verbose:
            print(f"[ERROR] Invalid network input: {e}")
        return []


def main():
    network = input("Enter network in CIDR format (e.g. 192.168.1.0/30): ").strip()
    ips = generate_ips_in_network(network, verbose=True)

    if ips:
        print(f"IP addresses in the network {network} are:")
        for ip in ips:
            print(f" - {ip}")
    else:
        print("No valid host IPs found or input was invalid.")


if __name__ == "__main__":
    main()
"""

# Multiple CIDR Input Support

import ipaddress
from typing import List, Dict

def generate_ips_in_network(network_cidr: str, verbose: bool = False) -> List[str]:
    
    # Generate all usable host IP addresses within a given network.

    # Args:
    #     network_cidr (str): The network in CIDR notation (e.g. '192.168.1.0/24').
    #     verbose (bool): Print error details if True.

    # Returns:
    #     List[str]: List of usable host IP addresses.
    
    try:
        network = ipaddress.ip_network(network_cidr.strip(), strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        if verbose:
            print(f"[ERROR] Invalid network '{network_cidr}': {e}")
        return []

def main():
    input_str = input("Enter one or more CIDR blocks, comma-separated: ")
    cidr_list = [cidr.strip() for cidr in input_str.split(",") if cidr.strip()]
    
    print("\n--- Host IPs Per Network ---")
    for cidr in cidr_list:
        ips = generate_ips_in_network(cidr, verbose=True)
        if ips:
            print(f"\nNetwork: {cidr}")
            for ip in ips:
                print(f" - {ip}")
        else:
            print(f"\nNo usable IPs for network: {cidr}")

if __name__ == "__main__":
    main()
