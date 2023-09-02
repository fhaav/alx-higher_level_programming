#!/usr/bin/python3
"""
Sends a POST request with an email parameter to a given URL.
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
