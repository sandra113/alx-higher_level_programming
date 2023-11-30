#!/bin/bash
# Displays all HTTP methods the server will accept
curl -X OPTIONS "$1"
