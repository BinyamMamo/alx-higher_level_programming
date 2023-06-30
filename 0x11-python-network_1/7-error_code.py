#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter

Usage: ./3-error_code.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    try:
        with requests.get(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as exception:
        print(f'Error code: {exception.code}')
