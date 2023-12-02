#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)

    except requests.exceptions.RequestException as e:
        print("Error accessing the URL:", e)
