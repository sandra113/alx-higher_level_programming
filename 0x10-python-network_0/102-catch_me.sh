#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch me
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me
