#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
adding an input letter using the requests package

Usage: ./8-json_api.py <letter>
"""
import requests
import sys

if __name__ == "__main__":
    value = {"q": ""}
    if len(sys.argv) > 1:
        value["q"] = sys.argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data=value).json()
    try:
        if resp == {} or resp is None:
            print("No result")
        else:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
    except ValueError:
        print("Not a valid JSON")
