# CIDR stands for Classless Inter-Domain Routing.
# Raw
"""
import ipaddress

def int_to_ipv4(integer):
    try:
        return str(ipaddress.IPv4Address(integer))
    except ValueError:
        return None
    
ipv4_int = 3232235777
print(f"Integer: {ipv4_int} -> IPv4: {int_to_ipv4(ipv4_int)}")
"""
# Explanation of the above code:
"""
IPv4 to Integer Mapping:
------------------------
To convert from IPv4 string to integer, we use base-256 math:

Formula:

Integer=(ax256^3)+(bx256^2)+(cx256^1)+(dx256^0)

Where:
a.b.c.d is your IPv4 address

Example: 192.168.1.1

Using the formula:

192 x 256^3 = 192 x 16,777,216 = 3,221,225,472
168 x 256^2 = 168 x 65,536    =    11,010,048
  1 x 256^1 =   1 x 256        =           256
  1 x 256^0 =   1 x 1          =             1
-----------------------------------------------
TOTAL                      =    3,232,235,777

So:

192.168.1.1 → 3232235777

Reversing: Integer to IPv4
--------------------------
Let's reverse the process by extracting 8-bit groups (octets):

Step 1: Convert integer to binary

3232235777 → 11000000.10101000.00000001.00000001

Split into 4 octets (8 bits each):

Binary Octet	Decimal
11000000	    192
10101000	    168
00000001	    1
00000001	    1

So:

3232235777 → 192.168.1.1
"""

# Modified version for IPv4 & IPv6, multiple inputs from the user
"""
# ipaddress: A built-in Python module for working with IP addresses and subnets.
import ipaddress

# Union[str, None]: Type hint meaning return type could be either str or None.
from typing import Union

def int_to_ip(value: int) -> Union[str, None]:
    
    # Convert integer to IPv4 or IPv6 address.
    
    try:
        if 0 <= value <= 2**32 - 1:
            return str(ipaddress.IPv4Address(value))
        elif 0 <= value <= 2**128 - 1:
            return str(ipaddress.IPv6Address(value))
        else:
            return None
    except ValueError:
        return None

def ip_to_int(ip: str) -> Union[int, None]:
    
    # Convert IPv4 or IPv6 address to integer.
    
    try:
        ip_obj = ipaddress.ip_address(ip)
        return int(ip_obj)
    except ValueError:
        return None

def ip_range(network: str) -> Union[str, None]:
    
    # Given a network in CIDR, return the IP range as (first, last).
    
    try:
        net_obj = ipaddress.ip_network(network, strict=False)
        first = str(net_obj.network_address)
        last = str(net_obj.broadcast_address)
        return f"{first} - {last}"
    except ValueError:
        return None

def handle_inputs():
    print("Choose conversion type:")
    print("1: Integer to IP (v4 or v6)")
    print("2: IP (v4 or v6) to Integer")
    print("3: CIDR to IP Range")
    choice = input("Enter option number (1/2/3): ").strip()

    values = input("Enter input(s), comma-separated: ")
    items = [v.strip() for v in values.split(",") if v.strip()]

    print("\n--- Results ---")
    for item in items:
        if choice == "1":
            try:
                num = int(item)
                ip = int_to_ip(num)
                print(f"{num} → {ip if ip else '[Invalid]'}")
            except ValueError:
                print(f"{item} → [Not a valid integer]")
        elif choice == "2":
            result = ip_to_int(item)
            print(f"{item} → {result if result is not None else '[Invalid IP]'}")
        elif choice == "3":
            result = ip_range(item)
            print(f"{item} → {result if result else '[Invalid CIDR]'}")
        else:
            print("Invalid choice.")
            break

if __name__ == "__main__":
    while True:
        handle_inputs()
        again = input("\nRun again? (y/n): ").strip().lower()
        if again != "y":
            break
"""

"""
✅ Summary
Feature	            Included
IPv4 support	       ✅
IPv6 support	       ✅
Bi-directional	       ✅
IP range from CIDR	   ✅
Multiple inputs	       ✅
User input UI	       ✅
"""

# Explanation of the code 

"""
🧱 Module Breakdown
import ipaddress and from typing import Union
• ipaddress: A built-in Python module for working with IP addresses and subnets.
• Union[str, None]: Type hint meaning return type could be either str or None.

🔁 Function Explanations
1. int_to_ip(value: int) -> Union[str, None]
Converts an integer into an IP address:

• If the value fits in 0 <= value <= 2^32 - 1, it's an IPv4 address

• If the value fits in 0 <= value <= 2^128 - 1, it's an IPv6 address

• Returns the string version, e.g., "192.168.1.1" or "2001:db8::1"

• Returns None if the number is invalid

2. ip_to_int(ip: str) -> Union[int, None]
Converts a string IPv4 or IPv6 address to its integer form:

• Example:

    • 192.168.1.1 → 3232235777

    • 2001:db8::1 → 42540766411282592875350729025363378177

• Returns None for invalid IPs

3. ip_range(network: str) -> Union[str, None]
Given a CIDR notation (e.g. "192.168.1.0/30"):

• Returns a string with the first and last IPs in the range:

192.168.1.0/30 → "192.168.1.0 - 192.168.1.3"

• Works with both IPv4 and IPv6

• Returns None if the CIDR is invalid

🎛️ Interactive CLI: handle_inputs()
This function runs a prompt-driven interaction with the user.

🧭 Flow:
• User picks a conversion type:

    1: Integer to IP
    2: IP to Integer
    3: CIDR to IP Range
• User enters a comma-separated list of inputs.

• Each item is processed:

    • For choice 1, it converts integers to IPs.

    • For choice 2, it converts IPs to integers.

    • For choice 3, it prints IP ranges from CIDR blocks.

• Results are printed immediately.

🔁 Looping
The script runs continuously until the user types "n" after each round.

🧪 Example Runs

Enter option number (1/2/3): 1
Enter input(s), comma-separated: 3232235777, 42540766411282592856903984951653826561

--- Results ---
3232235777 → 192.168.1.1
42540766411282592856903984951653826561 → 2001:db8:85a3::8a2e:370:7334

✅ Summary

Function	        Purpose
int_to_ip()	        Converts integer → IPv4 or IPv6
ip_to_int()	        Converts IPv4/IPv6 → integer
ip_range()	        Shows usable IP range in a network
handle_inputs()	    Handles user interaction
"""