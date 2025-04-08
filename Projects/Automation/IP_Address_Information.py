"""import os
import urllib.request as urllib2
import json

while True:
    ip = input("What is your target IP: ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print("IP: " + values["query"])
    print("City: " + values["city"])
    print("ISP: " + values["isp"])
    print("Country: " + values["country"])
    print("Region: " + values["region"])
    print("Timezone: " + values["timezone"])

    break"""

#  20/80 Explanation (20% Effort, 80% Understanding)
"""
Key components:

1. urllib2.urlopen(): Sends a request to the API.

2. json.loads(): Converts the API response (JSON) into a Python dictionary.

3. values["key"]: Extracts specific details like city, country, etc.

Flow:

Ask for an IP → Fetch data → Parse and display → Exit.
"""

#  80/20 Explanation (80% Effort, 20% Advanced Understanding)

"""
Imports:

1. urllib.request as urllib2: Used to make HTTP requests.

2. json: Used to parse JSON data returned by the API.

API Request:

1. The URL http://ip-api.com/json/ is combined with the user’s input IP to form a complete API endpoint.

2. urllib2.urlopen() sends a GET request to this endpoint.

Response Handling:

1. response.read() retrieves the raw JSON data.

2. json.loads(data) converts the JSON string into a Python dictionary (values).

Data Extraction:

1. The script accesses specific keys in the dictionary (query, city, isp, etc.) to display the IP details.

Loop and Break:

1. The while True loop keeps the program running, but the break statement exits after one iteration.
"""

# AI

import urllib.request as urllib2
import json

while True:
    ip = input("What is your target IP (or type 'exit' to quit): ")
    if ip.lower() == 'exit':
        print("Exiting the program. Goodbye, RR!")
        break

    url = "http://ip-api.com/json/"
    try:
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)

        if values["status"] == "success":
            print("\nIP: " + values["query"])
            print("City: " + values["city"])
            print("ISP: " + values["isp"])
            print("Country: " + values["country"])
            print("Region: " + values["region"])
            print("Timezone: " + values["timezone"])
        else:
            print("Error: " + values["message"])
    except Exception as e:
        print(f"An error occurred: {e}")

    print("\n" + "="*30 + "\n")


# Explanation
"""
Exit Option:

1. If the user types exit, the program stops. This makes it more user-friendly.

Error Handling:

2. The try-except block catches errors like invalid IPs or no internet connection and prints a helpful message.

API Status Check:

3. The API returns a status key. If it's "success", the data is displayed. Otherwise, an error message is shown.

Loop Continuation:

4. The while True loop keeps the program running until the user decides to exit.

Readability Improvements:

5. Added a separator ("="*30) to make the output cleaner between iterations.

How It Works Now:

1. Run the program.

2. Enter an IP address (e.g., 8.8.8.8 for Google's DNS).

3. See the details (city, country, ISP, etc.).

4. Choose to enter another IP or type exit to quit.
"""