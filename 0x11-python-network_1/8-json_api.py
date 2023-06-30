#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
adding an input letter using the requests package

Usage: ./8-json_api.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    value = {"q": ""}
    if len(sys.argv[1]) > 1:
        value["q"] = sys.argv[1]

    resp = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        resp = resp.json()
        if resp == {}:
            print("No result")
        else:
            print(f"[{resp.get('id')}] {resp.get('name')}")
    except ValueError:
        print("Not a valid JSON")
