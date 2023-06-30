#!/usr/bin/python3
"""fetches data from https://intranet.hbtn.io/status
using the requests package

Usage: ./4-hbtn_status.py
"""
import requests

if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.text
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
