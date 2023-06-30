#!/usr/bin/python3
"""fetches data from the URL provided in the first argument 
and displays X-Request-Id

Usage: ./1-hbtn_header.py <URL>
"""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as resp:
        print(resp.headers['X-Request-Id'])
