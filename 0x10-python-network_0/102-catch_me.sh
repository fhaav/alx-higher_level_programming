#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me using curl, with the data to "user_id=98"
curl -sX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
