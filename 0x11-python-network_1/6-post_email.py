#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email parameter and
displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]

    payload = {'email': email}
    resp = requests.post(url, data=payload)

    print("Your email is:", email)
    print(resp.text)
