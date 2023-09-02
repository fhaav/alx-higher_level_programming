#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""

import sys
import requests

if __name__ == "__main__":
    repo_name, owner_name = sys.argv[1], sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    commits = requests.get(url).json()

    for commit in commits[:10]:
        sha, author_name = commit["sha"], commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
