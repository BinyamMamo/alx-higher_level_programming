#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter
using the requests package
Usage: ./6-post_email.py <URL> <EMAIL>
"""
import sys
import requests

if __name__ == "__main__":
    req = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    with requests.get(req.url) as resp:
        print(resp.text)
