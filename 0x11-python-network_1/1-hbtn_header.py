#!/usr/bin/python3
"""
this module contains code that sends a request
to a url given as argument
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get("X-Request-Id"))
