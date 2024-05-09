#!/bin/bash
# makes a request to causing server to respond with message containi
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
