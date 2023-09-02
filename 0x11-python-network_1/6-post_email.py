#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email parameter and
displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]

    res = requests.post(url, data={'email': email})

    print(f"Your email is: {email}")
    print(response.text)
