#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter

Usage: ./3-error_code.py <URL>
"""
from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as exception:
        print(f'Error code: {exception.code}')
