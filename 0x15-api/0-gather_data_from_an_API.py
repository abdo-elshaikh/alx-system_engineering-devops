#!/usr/bin/python3
""" 0-gather_data_from_an_API.py """
import sys
import requests

userId = sys.argv[1]
res = requests.get("https://jsonplaceholder.typicode.com/users/"
                   + userId + "/todos")

if res.status_code == 200:
    todos = res.json()
    userName = requests.get("https://jsonplaceholder.typicode.com/users/"
                            + userId).json().get("name")
    completed = 0
    total = 0
    for todo in todos:
        if todo.get("completed"):
            completed += 1
        total += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(userName, completed, total))
    for todo in todos:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))
else:
    print("Error code: {}".format(res.status_code))
