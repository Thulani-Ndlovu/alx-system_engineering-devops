#!/usr/bin/python3
'''
    Script for a given employee ID, returns information
    about his/her TODO list progress
'''
import sys
import requests

if __name__ == '__main__':
    apiURL = "https://jsonplaceholder.typicode.com/"
    User = requests.get(apiURL + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(apiURL +
                         "todos", params={"userId: sys.argv[1]"}).json()
    Completed = [t.get('title') for t in todos if t.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        User.get("name"), len(Completed), len(todos)
    ))
    [print("\t {}".format(i)) for i in Completed]
