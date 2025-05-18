import ipaddress

def get_ip_address(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False

ip = input("Enter the IP: ")
print(f"Is {ip} private? {get_ip_address(ip)}")
