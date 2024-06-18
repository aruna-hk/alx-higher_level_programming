#!/usr/bin/python3

""" python networking"""

import urllib

from urllib import request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    page = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode('utf-8')))
