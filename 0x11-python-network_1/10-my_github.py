#!/usr/bin/python3
"""takes GitHub credentials from the first and second
argument and uses the GitHub API to display id

Usage: ./8-json_api.py <letter>
"""
import sys
import requests

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = requests.get("https://api.github.com/user", auth=auth)
    print(resp.json().get("id"))
