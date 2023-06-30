#!/bin/bash
# receives a url as input and displays the content size
curl -s "$1" | wc -c
