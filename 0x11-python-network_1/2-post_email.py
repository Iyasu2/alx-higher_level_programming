#!/usr/bin/python3
"""
this module contains code that sends a request
by passing an email as argument
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    param = {
            "email": email
            }
    query_string = urllib.parse.urlencode(param)
    data = query_string.encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("urf-8"))
