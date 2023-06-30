#!/usr/bin/python3
"""fetches data from https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        resp.headers['X-Request-Id']
