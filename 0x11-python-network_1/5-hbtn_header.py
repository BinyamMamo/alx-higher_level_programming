#!/usr/bin/python3
"""fetches data from the URL provided in the first argument
using the requests package
and displays X-Request-Id

Usage: ./5-hbtn_header.py <URL>
"""
import requests
import sys

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as resp:
        print(resp.headers['X-Request-Id'])
