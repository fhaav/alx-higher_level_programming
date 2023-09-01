#!/bin/bash
# Send an OPTIONS request to the specified URL using curl and display the allowed methods.
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
