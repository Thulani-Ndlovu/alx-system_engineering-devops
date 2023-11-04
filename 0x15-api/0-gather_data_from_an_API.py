#!/usr/bin/python3
'''
    Script for a given employee ID, returns information
    about his/her TODO list progress
'''
from requests import get
from sys import argv

if __name__ == '__main__':
    apiURL = "https://jsonplaceholder.typicode.com/"
    todoURL = apiURL + "user/{}/todos".format(argv[1])
    nameURL = apiURL + "user/{}".format(argv[1])
    todoRes = get(todoURL).json()
    nameRes = get(nameURL).json()

    todoNumber = len(todoRes)
    todoCompleted = len([i for i in todoRes
                         if i.get("completed")])
    name = nameRes.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todoCompleted, todoNumber))
    for i in todoRes:
        if (i.get("completed")):
            print("\t {}".format(i.get("title")))
