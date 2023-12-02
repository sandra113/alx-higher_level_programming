#!/usr/bin/python3
"""this module fetches from url using the urllib package"""

if __name__ == "__main__":
    import urllib.request
    import sys

    if len(sys.argv) < 2:
        sys.exit()

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")

    except urllib.error.URLError as e:
        print("Error accessing the URL:", e)
