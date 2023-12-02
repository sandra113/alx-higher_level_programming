#!/usr/bin/python3

import requests
"""this script that fetches https://alx-intranet.hbtn.io/status"""

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

except requests.exceptions.RequestException as e:
    print("Error accessing the URL:", e)
