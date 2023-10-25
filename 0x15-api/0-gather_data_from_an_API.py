#!/usr/bin/python3
"""
A script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

"""
# Define a function to get data from the API for a specific employee ID
"""
def get_data_api(user_id):
    done = []
    url = "https://jsonplaceholder.typicode.com/"

    """# Get user information by making an HTTP GET request 
        to the API and convert the response to JSON """
    user = get(url + "users/{}".format(user_id)).json()

    """ # Get TODO list tasks for the specified
        user and convert the response to JSON"""
    tasks = get(url + "todos?userId={}".format(user_id)).json()

    """ # Iterate through the tasks and check if they are completed,
        if so, add them to the 'done' list"""
    for task in tasks:
        if task.get("completed"):
            done.append(task.get("title"))

    """ # Print information about the employee's progress,
        including name, completed tasks, and total tasks """
    print("Employee {} is done with tasks({}/{}):"
          .format(user["name"], len(done), len(tasks)))

    """ # List the titles of completed tasks """
    for task in done:
        print("\t {}".format(task))

""" # Check if the script is being executed as the main program """
if __name__ == "__main__":
    """# Extract the employee ID from the command-line arguments
        and call the 'get_data_api' function """
    get_data_api(int(argv[1]))
