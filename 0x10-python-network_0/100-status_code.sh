#!/bin/bash
# Send a request to the specified URL using curl and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
