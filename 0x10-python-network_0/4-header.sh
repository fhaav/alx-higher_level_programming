#!/bin/bash
# Execute a GET request to the provided URL, including a specific header.
curl -sH "X-School-User-Id: 98" "$1"
