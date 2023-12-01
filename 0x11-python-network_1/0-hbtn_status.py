#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body_byte = response.read()
        body_utf = body_byte.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(body_byte)))
        print("\t- content: {}".format(body_byte))
        print("\t- utf8 content: {}".format(body_utf))

except urllib.error.URLError as e:
    print("Error accessing the URL:", e)
