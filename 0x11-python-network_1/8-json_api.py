#!/usr/bin/python3
"""
This script takes a letter as input, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter,
and displays the results.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    resp = requests.post(url, data={'q': letter})

    try:
        data = resp.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
