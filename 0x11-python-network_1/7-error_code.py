#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter
using the requests package

Usage: ./7-error_code.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code < 400:
        print(resp.read().decode("utf-8"))
    else:
        print(f'Error code: {resp.status_code}')
