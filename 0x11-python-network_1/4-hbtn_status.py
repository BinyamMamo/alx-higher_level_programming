#!/usr/bin/python3
"""fetches data from https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read().decode('UTF-8')
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
