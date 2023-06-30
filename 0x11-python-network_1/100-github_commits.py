#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits")

    resp = requests.get(url)
    commits = resp.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
