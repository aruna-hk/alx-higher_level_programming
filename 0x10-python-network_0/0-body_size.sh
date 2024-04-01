#!/bin/bash
#cURL body size
#get the body size of the response

curl -X GET -sI  "$1" | grep -i "Content-Length" | cut -d" " -f2
