#!/usr/bin/python3

import urllib.request
import urllib.parse
import urllib.error
import sys

url = "https://alx-intranet.hbtn.io/status"

if len(sys.argv) < 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=data) as response:

        body = response.read().decode('utf-8')
        print("Body response:")
        print(body)

except urllib.error.URLError as e:
    print("Error accessing the URL:", e)
