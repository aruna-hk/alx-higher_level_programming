#!/usr/bin/python3

"""
  that takes in a URL as argument and
  sends a request to the URL and display X-Request-Id header
  content
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
