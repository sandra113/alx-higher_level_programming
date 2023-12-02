#!/usr/bin/python3
"""this module displays the body of the response (decoded in utf-8)."""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')

            # Print the body of the response
            print("Body response:")
            print(body)

    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the HTTP status code
        print("Error code:", e.code)

    except urllib.error.URLError as e:
        print("Error accessing the URL:", e)
