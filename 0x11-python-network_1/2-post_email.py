#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter

Usage: ./2-post_email.py <URL> <EMAIL>
"""
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    post = {"email": sys.argv[2]}
    req = request.Request(sys.argv[1], parse.urlencode(post).encode('utf-8'))
    with request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
