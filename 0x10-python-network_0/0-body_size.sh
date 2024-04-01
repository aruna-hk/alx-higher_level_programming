#!/usr/bin/env bash
#cURL body size
#get the body size of the response

curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
