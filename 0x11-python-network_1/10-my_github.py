#!/usr/bin/python3
"""
This script uses the GitHub API to display your GitHub user id.
"""

import requests
from sys import argv

if __name__ == "__main__":
    username, password = argv[1], argv[2]

    url = "https://api.github.com/user"
    auth = (username, password)

    resp = requests.get(url, auth=auth)
    print(resp.json().get("id", None))
