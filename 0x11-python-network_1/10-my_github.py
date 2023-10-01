#!/usr/bin/python3
"""
this module uses requests
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    passwd = sys.argv[2]

    response = requests.get(url, auth=HTTPBasicAuth(username, passwd))
    json_obj = response.json()
    print(json_obj.get("id"))
