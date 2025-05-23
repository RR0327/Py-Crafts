# Raw version
"""
import ipaddress

def ip_in_network(ip, network):
    try:
        network_obj = ipaddress.ip_network(network, strict=False)
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj in network_obj
    except ValueError:
        return False
    
ip = "192.168.1.10"
network = "192.168.1.0/24"
print(f"Is {ip} in network {network} ? {ip_in_network(ip, network)}")  # Output: True
"""

# Modified version
"""
import ipaddress
from typing import Union

def ip_in_network(ip: str, network: str) -> bool:
    
    # Check whether a given IP address belongs to the specified network.

    # Args:
    #     ip (str): The IP address to check (IPv4 or IPv6).
    #     network (str): The network in CIDR notation (e.g., '192.168.1.0/24').

    # Returns:
    #     bool: True if the IP is in the network, False otherwise.
    
    try:
        ip_obj = ipaddress.ip_address(ip)
        network_obj = ipaddress.ip_network(network, strict=False)
        return ip_obj in network_obj
    except ValueError as e:
        print(f"[ERROR] Invalid IP or network: {e}")
        return False


if __name__ == "__main__":
    ip = "192.168.1.10"
    network = "192.168.1.0/24"
    result = ip_in_network(ip, network)
    print(f"Is {ip} in network {network}? {result}")
"""

# More Modified version
"""
import ipaddress
from typing import Union, List, Dict

def check_ips_in_networks(
    ips: Union[str, List[str]],
    networks: Union[str, List[str]]
) -> Dict[str, List[str]]:

    # Checks which networks each IP address belongs to.

    # Args:
    #     ips (str or List[str]): IP address or list of IP addresses.
    #     networks (str or List[str]): Network or list of networks in CIDR format.

    # Returns:
    #     Dict[str, List[str]]: Mapping of each IP to the list of networks it belongs to.
    
    if isinstance(ips, str):
        ips = [ips]
    if isinstance(networks, str):
        networks = [networks]

    result = {}
    for ip in ips:
        try:
            ip_obj = ipaddress.ip_address(ip)
        except ValueError as e:
            result[ip] = [f"[Invalid IP: {e}]"]
            continue

        matches = []
        for net in networks:
            try:
                net_obj = ipaddress.ip_network(net, strict=False)
                if ip_obj in net_obj:
                    matches.append(net)
            except ValueError as e:
                continue  # skip invalid network

        result[ip] = matches

    return result


if __name__ == "__main__":
    ips = ["192.168.1.10", "10.0.0.5", "172.16.5.4"]
    networks = ["192.168.1.0/24", "10.0.0.0/8", "172.16.0.0/16"]
    results = check_ips_in_networks(ips, networks)

    for ip, matched_networks in results.items():
        print(f"{ip} is in networks: {matched_networks}")
"""

# User input acceptable
"""
import ipaddress

def check_ips_in_networks(ips, networks):
    
    # Check which networks each IP belongs to.
    # Returns a dictionary mapping each IP to its matched networks.
    
    result = {}

    for ip in ips:
        try:
            ip_obj = ipaddress.ip_address(ip)
        except ValueError as e:
            result[ip] = [f"[Invalid IP: {e}]"]
            continue

        matched = []
        for net in networks:
            try:
                net_obj = ipaddress.ip_network(net, strict=False)
                if ip_obj in net_obj:
                    matched.append(net)
            except ValueError:
                continue  # ignore invalid network

        result[ip] = matched

    return result


def main():
    ip_input = input("Enter IP address(es), comma-separated: ")
    network_input = input("Enter network(s) in CIDR format, comma-separated: ")

    ips = [ip.strip() for ip in ip_input.split(",") if ip.strip()]
    networks = [net.strip() for net in network_input.split(",") if net.strip()]

    results = check_ips_in_networks(ips, networks)

    print("\n--- Results ---")
    for ip, matched_networks in results.items():
        if matched_networks:
            print(f"{ip} belongs to: {', '.join(matched_networks)}")
        else:
            print(f"{ip} does NOT belong to any of the specified networks.")

if __name__ == "__main__":
    main()
"""