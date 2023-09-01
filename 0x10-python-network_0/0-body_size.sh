#!/bin/bash
# Measure the byte size of an HTTP response header for a given URL.
curl -s "$1" | wc -c
