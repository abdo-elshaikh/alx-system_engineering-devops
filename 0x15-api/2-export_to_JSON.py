#!/usr/bin/python3
""" 2-export_to_JSON.py """
import json
import requests
from sys import argv

if __name__ == '__main__':
    employeeId = argv[1]
    res = requests.get("https://jsonplaceholder.typicode.com/users/" +
                       employeeId)
    if res.status_code == 200:
        employeeName = res.json().get("username")
        res = requests.get("https://jsonplaceholder.typicode.com/users/" +
                           employeeId + "/todos")
        if res.status_code == 200:
            employeeTodos = res.json()
            with open(employeeId + '.json', 'w') as jsonFile:
                json.dump({employeeId: [{
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                    'username': employeeName
                } for todo in employeeTodos]}, jsonFile)
        else:
            print("Error code: {}".format(res.status_code))
    else:
        print("Error code: {}".format(res.status_code))

    jsonFile.close()
