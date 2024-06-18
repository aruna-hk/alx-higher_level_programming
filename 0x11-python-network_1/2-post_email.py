#!/usr/bin/python3
"""
    takes url and email as url
    send request email as data
    display response
"""

import sys
import urllib.request
import urllib.parse
url = sys.argv[1]
values = {"email": sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data=data)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.get_method = lambda: 'POST'

with urllib.request.urlopen(req) as response:
    print(response.read())
