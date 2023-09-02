#!/usr/bin/python3
"""
Displays the X-Request-Id header variable from a URL response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = dict(response.headers).get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
