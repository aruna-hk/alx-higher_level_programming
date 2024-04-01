#!/bin/bash
#methods supported
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
