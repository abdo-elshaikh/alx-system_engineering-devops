#!/usr/bin/python3
""" 1-export_to_CSV.py """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    employeeId = argv[1]
    res = requests.get("https://jsonplaceholder.typicode.com/users/" +
                       employeeId)
    if res.status_code == 200:
        employeeName = res.json().get("username")
        res = requests.get("https://jsonplaceholder.typicode.com/users/" +
                           employeeId + "/todos")
        if res.status_code == 200:
            employeeTodos = res.json()
            with open(employeeId + '.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for todo in employeeTodos:
                    writer.writerow([employeeId, employeeName,
                                     todo.get("completed"),
                                     todo.get("title")])
        else:
            print("Error code: {}".format(res.status_code))
    else:
        print("Error code: {}".format(res.status_code))
