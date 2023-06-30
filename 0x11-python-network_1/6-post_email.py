#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter
using the requests package
Usage: ./6-post_email.py <URL> <EMAIL>
"""
import sys
import requests

if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], params=params)
    with requests.get(req) as resp:
        print(resp.text)
