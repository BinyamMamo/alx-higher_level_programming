#!/bin/bash
# sends a POST request with email and subject variables for a given URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
