#!/bin/bash
# parses the content length and displays it
curl -sI $1 | grep "content-length" | cut -d " " -f 2
