#!/usr/bin/python3

""" takes url as args """

import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.info()
    print(headers['X-Request-Id'])
