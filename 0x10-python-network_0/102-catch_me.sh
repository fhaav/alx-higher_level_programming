#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me using curl, with the data to "user_id=98"
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
