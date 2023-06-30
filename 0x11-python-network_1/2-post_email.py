#!/usr/bin/python3
"""fetches data from the URL provided in the first argument
and displays X-Request-Id

Usage: ./1-hbtn_header.py <URL>
"""
from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    post = {"email": email}

    with request.urlopen(url + "?" + parse.urlencode(post)) as resp:
        print(resp.read().decode("UTF-8"))
