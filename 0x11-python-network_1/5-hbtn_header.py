#!/usr/bin/python3
"""fetches data from the URL provided in the first argument
using the requests package
and displays X-Request-Id

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as resp:
        print(resp.headers.get('X-Request-Id'))
