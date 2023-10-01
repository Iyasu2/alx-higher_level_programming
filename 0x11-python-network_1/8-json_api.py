#!/usr/bin/python3
"""
this module uses requests
"""
import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": letter})

    try:
        data = response.json()

        if data:
            user_id = data.get("id")
            user_name = data.get("name")
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
