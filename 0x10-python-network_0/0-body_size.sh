#!/bin/bash
#cURL body size
curl -X GET -sI  "$1" | grep -i "Content-Length" | awk '{print $2}'
