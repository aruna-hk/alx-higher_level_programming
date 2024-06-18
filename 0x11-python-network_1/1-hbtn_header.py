#!/usr/bin/python3
"""
    takes url as args and return header filed with
    X-Request-Id
"""
import sys
import urllib

from urllib import request

with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.info()
    print(headers['X-Request-Id'])
