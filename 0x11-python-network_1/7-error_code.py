#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL,
and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    status_code = res.status_code
    cont = res.text

    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(cont)
