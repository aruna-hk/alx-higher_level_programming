#!/usr/bin/python3

""" python networking"""

import urllib

from urllib import request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    page = response.read()
    print("Body response:")
    print("    - type: {}".format(type(page)))
    print("    - content: {}".format(page))
    print("    - utf content: {}".format(page.decode('utf-8')))
