#!/usr/bin/python3
"""this module fetches from url using the urllib package"""

if __name__ == "__main__":
    import urllib.request
    import sys

# Check if a URL is provided as a command-line argument
    if len(sys.argv) < 2:
        sys.exit()

# Get the URL from the command-line argument
    url = sys.argv[1]

    try:
    # Use the with statement to open the URL and create a response object
        with urllib.request.urlopen(url) as response:
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")

    except urllib.error.URLError as e:
        print("Error accessing the URL:", e)
