#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter

Usage: ./2-post_email.py <URL> <EMAIL>
"""
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    post = {"email": email}

    with request.urlopen(url + "?" + parse.urlencode(post)) as resp:
        print(resp.read().decode("utf-8"))
