#!/bin/bash
# displays the allowed methods for a given URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
