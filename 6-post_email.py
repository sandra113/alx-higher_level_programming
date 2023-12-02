#!/usr/bin/python3
"""This script sends a request to the URL with the email as a parameter."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print("Body response:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("Error accessing the URL:", e)
