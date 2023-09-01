#!/bin/bash
# Issue a JSON POST request using curl, specifying JSON content from a file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
