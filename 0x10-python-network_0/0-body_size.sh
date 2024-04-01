#!/bin/bash
#cURL body size
curl -X GET -sI  "$1" | grep -i "Content-Length" | cut -d" " -f2
